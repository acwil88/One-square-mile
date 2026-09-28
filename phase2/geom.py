import json, math, numpy as np, rasterio, cv2
from pyproj import Transformer
import os
REPO=os.path.dirname(os.path.abspath(__file__))+'/'
BUILD=REPO+'build/'; os.makedirs(BUILD,exist_ok=True)
SCALE=3000.0            # 1:3000
PT_PER_FT=72.0/SCALE*12 # points per ground foot
poly=json.load(open(REPO+'section7-polygon-2277.geojson'))['features'][0]['geometry']['coordinates'][0][:4]
P=np.array([[x,y] for x,y,*_ in poly],float)
# identify SW corner = min (x+y)... use: south side = side with lowest mean y
sides=[(i,(P[i]+P[(i+1)%4])/2) for i in range(4)]
si=min(sides,key=lambda t:t[1][1])[0]   # south side index
A=P[si]; B=P[(si+1)%4]
# ensure A is the west end
if A[0]>B[0]: A,B=B,A
theta=math.atan2(B[1]-A[1],B[0]-A[0])   # radians, angle of south line from grid east
ca,sa=math.cos(theta),math.sin(theta)
def to_local(x,y):
    dx,dy=x-A[0],y-A[1]
    return (dx*ca+dy*sa, -dx*sa+dy*ca)   # feet, x along south line, y toward north
def to_local_arr(xy):
    xy=np.asarray(xy,float); d=xy-A; return np.stack([d[:,0]*ca+d[:,1]*sa, -d[:,0]*sa+d[:,1]*ca],1)
L=to_local_arr(P)   # local corners
loc_minx,loc_miny=L[:,0].min(),L[:,1].min(); loc_maxx,loc_maxy=L[:,0].max(),L[:,1].max()
W_ft=loc_maxx-loc_minx; H_ft=loc_maxy-loc_miny
wgs=Transformer.from_crs('EPSG:2277','EPSG:4326',always_xy=True)
def corner_latlon(i): lon,lat=wgs.transform(P[i][0],P[i][1]); return lat,lon
# order corners by local position: SW, SE, NE, NW
order=sorted(range(4),key=lambda i:(L[i][1]>H_ft/2, L[i][0] if L[i][1]<=H_ft/2 else -L[i][0]))
# order: bottom row sorted by x asc (SW,SE), top row sorted by x desc (NE,NW)
CORN={'SW':order[0],'SE':order[1],'NE':order[2],'NW':order[3]}
def side_len(a,b): return float(np.hypot(*(P[a]-P[b])))
if __name__=='__main__':
    print('theta deg',math.degrees(theta)); print('local corners',L.round(1)); print('extent ft',W_ft,H_ft)
    for k,i in CORN.items(): print(k,corner_latlon(i))
    print('S',side_len(CORN['SW'],CORN['SE']),'E',side_len(CORN['SE'],CORN['NE']),'N',side_len(CORN['NE'],CORN['NW']),'W',side_len(CORN['NW'],CORN['SW']))
