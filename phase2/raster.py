import numpy as np, rasterio, cv2, math
from geom import *
PAD=400.0   # ft of bleed around polygon in local frame
R=1.0       # ft per output px
def local_to_px(x,y):  # local ft -> raster px (u right, v down)
    return ((x-(loc_minx-PAD))/R, ((loc_maxy+PAD)-y)/R)
OW=int((W_ft+2*PAD)/R); OH=int((H_ft+2*PAD)/R)
def warp_to_local(path, out, band=None, gray=True):
    with rasterio.open(path) as d:
        T=d.transform; Ti=~T
        arr=d.read() if band is None else d.read([band])
        if arr.shape[0]>=3: arr=arr[:3]
    # dst px -> local -> grid -> src px ; build 2x3 matrix for cv2 (src = M @ [u,v,1])
    # local x = u*R + (minx-PAD); local y = (maxy+PAD) - v*R
    # grid = A + Rot(theta) @ local
    # src px = Ti @ grid
    def f(u,v):
        lx=u*R+(loc_minx-PAD); ly=(loc_maxy+PAD)-v*R
        gx=A[0]+lx*ca-ly*sa; gy=A[1]+lx*sa+ly*ca
        c,r=Ti*(gx,gy); return c,r
    (c0,r0)=f(0,0); (c1,r1)=f(1,0); (c2,r2)=f(0,1)
    M=np.array([[c1-c0,c2-c0,c0],[r1-r0,r2-r0,r0]],float)
    img=arr.transpose(1,2,0) if arr.shape[0]>1 else arr[0]
    o=cv2.warpAffine(img,M,(OW,OH),flags=cv2.INTER_CUBIC|cv2.WARP_INVERSE_MAP,borderValue=0)
    if gray and o.ndim==3: o=cv2.cvtColor(o,cv2.COLOR_RGB2GRAY)
    cv2.imwrite(out,o); return o
if __name__=='__main__':
    o=warp_to_local(REPO+'naip2024-2277.tif',BUILD+'base_naip.png')
    print(o.shape)
    # polygon mask in px
    pts=np.array([local_to_px(x,y) for x,y in L],np.int32)
    m=np.zeros(o.shape[:2],np.uint8); cv2.fillPoly(m,[pts],255)
    lightened=(255-(255-o.astype(float))*0.38).astype(np.uint8)   # lighten ~45%
    outside=(255-(255-o.astype(float))*0.14).astype(np.uint8)
    base=np.where(m>0,lightened,outside); cv2.imwrite(BUILD+'base_main.png',base)
    chk=cv2.resize(base,(900,int(900*OH/OW))); cv2.polylines(chk,[ (pts*900/OW).astype(np.int32)],True,0,2); cv2.imwrite(BUILD+'chk.png',chk)
    for yr in ['1995','1984','1974','1965','1954','1946']: warp_to_local(REPO+f'ee-{yr}-2277.tif',BUILD+f'base_{yr}.png')

    # 1974: the EarthExplorer scan is mirrored top-to-bottom. Until the scan is re-warped with the flip, mirror the
    # aligned raster about the section's centre row and apply the translation found against 1984 (2026-09-29).
    im=cv2.imread(BUILD+'base_1974.png',0); _,vc=local_to_px(0,(loc_miny+loc_maxy)/2); H_=im.shape[0]
    fl=cv2.flip(im,0); M=np.float32([[1,0,92],[0,1,int(round(2*vc-(H_-1)))+160]]); fl=cv2.warpAffine(fl,M,(im.shape[1],H_),borderValue=0)
    cv2.imwrite(BUILD+'base_1974.png',fl)
