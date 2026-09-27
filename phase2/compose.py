import json, csv, math, numpy as np, cv2
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, Color
from reportlab.pdfbase import pdfmetrics; from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from pyproj import Transformer
from geom import *
from raster import local_to_px, PAD, OW, OH, R
F='/home/claude/build/fonts/'
for n,f in [('Serif','EBGaramond.ttf'),('SerifI','EBGaramond-Italic.ttf'),('Cond','BarlowCondensed-Regular.ttf'),('CondM','BarlowCondensed-Medium.ttf'),('CondB','BarlowCondensed-SemiBold.ttf')]:
    pdfmetrics.registerFont(TTFont(n,F+f))
BLK=HexColor('#1A1A1A'); RED=HexColor('#B3261E'); BLU=HexColor('#4A6FA5'); G40=HexColor('#666666'); G60=HexColor('#999999'); G80=HexColor('#C8C8C8')
W,H=24*inch,36*inch; M=1*inch
PPF=72*12/SCALE  # pt per ft
# vertical stack
title_h=2.4*inch; gap=0.55*inch; strip_h=3.35*inch
panel_w=W_ft*PPF; panel_h=H_ft*PPF
panel_x0=(W-panel_w)/2; panel_y0=H-M-title_h-gap-panel_h
strip_y0=panel_y0-gap-strip_h; text_y0=M; text_h=strip_y0-gap-M
def pg(x,y): return (panel_x0+(x-loc_minx)*PPF, panel_y0+(y-loc_miny)*PPF)
def pg_grid(x,y): return pg(*to_local(x,y))
T=Transformer.from_crs('EPSG:4326','EPSG:2277',always_xy=True)
def load(name): return json.load(open(REPO+name))['features']
def lines_of(geom):
    if geom['type']=='LineString': return [geom['coordinates']]
    if geom['type']=='MultiLineString': return geom['coordinates']
    if geom['type']=='Polygon': return geom['coordinates']
    if geom['type']=='MultiPolygon': return [r for p in geom['coordinates'] for r in p]
    return []
c=canvas.Canvas('/home/claude/build/proof-v2.pdf',pagesize=(W,H)); c.setTitle('Section 7, Block 39, T-1-S — One Square Mile, Desk Edition'); c.setAuthor('Claude (Anthropic) and Skippy (Meta Muse) for a resident of the section'); c.setSubject('First edition, October 2026')
BLEED=90.0  # ft shown beyond the section
def clip_rect():
    x0,y0=pg(loc_minx-BLEED,loc_miny-BLEED); x1,y1=pg(loc_maxx+BLEED,loc_maxy+BLEED); return x0,y0,x1-x0,y1-y0
# ---------- MAIN PANEL ----------
c.saveState(); p=c.beginPath(); p.rect(*clip_rect()); c.clipPath(p,stroke=0)
# base raster
base=cv2.imread('/home/claude/build/base_main.png',0)
from PIL import Image
Image.fromarray(base).save('/home/claude/build/base_main.jpg',quality=85)
bx,by=pg(loc_minx-PAD,loc_miny-PAD); c.drawImage('/home/claude/build/base_main.jpg',bx,by,width=(W_ft+2*PAD)*PPF,height=(H_ft+2*PAD)*PPF)
def draw_lines(feats,color,width,dash=None,close=False):
    c.setStrokeColor(color); c.setLineWidth(width); c.setDash(dash or []); 
    for f in feats:
        for ring in lines_of(f['geometry']):
            pth=c.beginPath(); first=True
            for xy in ring:
                X,Y=pg_grid(xy[0],xy[1]); (pth.moveTo if first else pth.lineTo)(X,Y); first=False
            if close: pth.close()
            c.drawPath(pth,stroke=1,fill=0)
    c.setDash([])
# soils
soils=load('ssurgo-2277.geojson'); draw_lines(soils,G60,0.4,dash=[1,2],close=True)
c.setFont('CondM',7); c.setFillColor(G40)
for f in soils:
    ring=lines_of(f['geometry'])[0]; loc=to_local_arr([r[:2] for r in ring]); cx,cy=loc[:,0].mean(),loc[:,1].mean()
    if 0<cx<W_ft and 0<cy<H_ft and len(ring)>8:
        X,Y=pg(cx,cy); c.drawCentredString(X,Y,f['properties']['muname'].split(',')[0].upper())
# parcels
draw_lines(load('parcels-2277.geojson'),G60,0.3,close=True)
# golf
draw_lines(load('golf-course-2277.geojson'),G40,0.5,close=True)
# streets + names
streets=load('streets-2277.geojson'); draw_lines(streets,G40,0.7)
c.setFont('Cond',6.5); c.setFillColor(G40); done=set()
for f in streets:
    nm=f['properties'].get('name'); 
    if not nm or nm in done: continue
    for ring in lines_of(f['geometry']):
        loc=to_local_arr([r[:2] for r in ring]); 
        if len(loc)<2: continue
        i=len(loc)//2; a,b=loc[max(0,i-1)],loc[min(len(loc)-1,i+1)]; ang=math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]))
        if ang>90: ang-=180
        if ang<-90: ang+=180
        mx,my=loc[i]; 
        if not(0<mx<W_ft and 0<my<H_ft): continue
        X,Y=pg(mx,my); c.saveState(); c.translate(X,Y); c.rotate(ang); c.drawCentredString(0,2,nm.upper()); c.restoreState(); done.add(nm); break
# Midland Draw (NHD flowline)
draw_lines(load('midland-draw-2277.geojson'),BLU,1.1)
dr=lines_of(load('midland-draw-2277.geojson')[0]['geometry'])[0]; dl=to_local_arr([r[:2] for r in dr]); ins=dl[(dl[:,0]>300)&(dl[:,0]<W_ft-300)]
if len(ins)>4:
    i=int(np.argmax(ins[:,1])); i=min(max(i,3),len(ins)-4); a,b=ins[i-2],ins[i+2]; ang=math.degrees(math.atan2(b[1]-a[1],b[0]-a[0])); X,Y=pg(*ins[i]); c.saveState(); c.translate(X,Y); c.rotate(ang); c.setFont('CondM',9); c.setFillColor(BLU); c.drawCentredString(0,6,'MIDLAND DRAW  ·  NHDPlus flowline 5688042, reach unnamed in NHD'); c.restoreState()
# quarter lines
mid=lambda a,b:(P[a]+P[b])/2
c.setStrokeColor(BLK); c.setLineWidth(0.5); c.setDash([4,3])
for (a,b),(d,e) in [((CORN['SW'],CORN['SE']),(CORN['NW'],CORN['NE'])),((CORN['SW'],CORN['NW']),(CORN['SE'],CORN['NE']))]:
    X0,Y0=pg_grid(*mid(a,b)); X1,Y1=pg_grid(*mid(d,e)); c.line(X0,Y0,X1,Y1)
c.setDash([])
# SE/4 outline
cx_,cy_=pg_grid(*((P[CORN['SW']]+P[CORN['NE']])/2))
c.setLineWidth(1.0); c.setDash([6,3]); pth=c.beginPath()
se=[P[CORN['SE']], mid(CORN['SE'],CORN['NE']), (P[CORN['SW']]+P[CORN['NE']])/2, mid(CORN['SW'],CORN['SE'])]
for i,pt in enumerate(se):
    X,Y=pg_grid(*pt); (pth.moveTo if i==0 else pth.lineTo)(X,Y)
pth.close(); c.drawPath(pth); c.setDash([])
c.setFont('Cond',7.5); c.setFillColor(BLK); X,Y=pg_grid(*(P[CORN['SE']]*0.5+((P[CORN['SW']]+P[CORN['NE']])/2)*0.5)); c.drawCentredString(X,Y+120*PPF,'SE/4 · 160 ACRES · SURFACE ONLY · 31 OCT 1978')
# pipelines
pipes=load('pipelines-2277.geojson')
for f in pipes:
    pr=f['properties']; col=BLK; dash=[5,3]
    draw_lines([f],col,0.9,dash=dash)
    ring=lines_of(f['geometry'])[0]; loc=to_local_arr([r[:2] for r in ring]); inside=loc[(loc[:,0]>0)&(loc[:,0]<W_ft)&(loc[:,1]>0)&(loc[:,1]<H_ft)]
    if len(inside)>3:
        i=len(inside)//2; a,b=inside[max(0,i-2)],inside[min(len(inside)-1,i+2)]; ang=math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]))
        if ang>90: ang-=180
        if ang<-90: ang+=180
        X,Y=pg(*inside[i]); lab=f"{pr['system']} · {pr['commodity'].lower()} · {pr['diameter_in']}\" · T-4 {pr.get('t4_permit','')}".replace('· T-4 ','· T-4 ' if pr.get('t4_permit') else '').rstrip(' ·T-4')
        c.saveState(); c.translate(X,Y); c.rotate(ang); c.setFont('Cond',6); c.setFillColor(BLK); c.drawCentredString(0,2.5,lab); c.restoreState()
# wells
rows=list(csv.DictReader(open(REPO+'wells.csv')))
for r in rows:
    x,y=T.transform(float(r['longitude']),float(r['latitude'])); lx,ly=to_local(x,y)
    if not(-BLEED<lx<W_ft+BLEED and -BLEED<ly<H_ft+BLEED): continue
    X,Y=pg(lx,ly); st=r['status']; s=4.2
    c.setLineWidth(0.8); c.setStrokeColor(BLK); c.setFillColor(BLK)
    if r['lateral_azimuth_deg']:
        c.rect(X-s,Y-s,2*s,2*s,stroke=1,fill=1)
        az=float(r['lateral_azimuth_deg']); 
        # lateral tick: azimuth true -> page angle: page up is true az 344.9
        ang=math.radians(90-(az-344.9)); c.setLineWidth(1.2); c.line(X,Y,X+38*math.cos(ang),Y+38*math.sin(ang))
    elif st=='active': c.circle(X,Y,s,stroke=1,fill=1)
    elif st=='dry hole': c.circle(X,Y,s,stroke=1,fill=0); c.line(X-s,Y-s,X+s,Y+s); c.line(X-s,Y+s,X+s,Y-s)
    elif st=='plugged': c.circle(X,Y,s,stroke=1,fill=0); c.line(X-s,Y,X+s,Y)
    else: c.circle(X,Y,s,stroke=1,fill=0)   # permitted
    c.setFont('Cond',6); api=r['api'] if 'xxxxx' not in r['api'] else '42-329-(unconfirmed)'; c.drawString(X+s+2,Y+3,f"{api}  {r['well_name']} · {st}")
c.restoreState()
# legend
lx,ly=pg(120,3350); lw_,lh_=2.45*inch,1.9*inch
c.setFillColor(Color(1,1,1,alpha=0.82)); c.setStrokeColor(BLK); c.setLineWidth(0.6); c.rect(lx,ly,lw_,lh_,stroke=1,fill=1)
c.setFillColor(BLK); c.setFont('CondB',8.5); c.drawString(lx+8,ly+lh_-14,'WELLS  (Railroad Commission of Texas, Sept 2026)')
items=[('producing','fill'),('horizontal pad; tick shows lateral direction','sq'),('permitted, not drilled','open'),('dry hole','dry'),('plugged','plug')]
yy=ly+lh_-30
for lab,k in items:
    X=lx+16; s_=3.6; c.setLineWidth(0.8)
    if k=='fill': c.circle(X,yy,s_,stroke=1,fill=1)
    elif k=='sq': c.rect(X-s_,yy-s_,2*s_,2*s_,stroke=1,fill=1); c.setLineWidth(1.2); c.line(X,yy,X+12,yy+8)
    elif k=='open': c.circle(X,yy,s_,stroke=1,fill=0)
    elif k=='dry': c.circle(X,yy,s_,stroke=1,fill=0); c.line(X-s_,yy-s_,X+s_,yy+s_); c.line(X-s_,yy+s_,X+s_,yy-s_)
    else: c.circle(X,yy,s_,stroke=1,fill=0); c.line(X-s_,yy,X+s_,yy)
    c.setFont('Cond',8); c.drawString(X+18,yy-3,lab); yy-=14
c.setLineWidth(0.9); c.setDash([5,3]); c.line(lx+10,yy-2,lx+28,yy-2); c.setDash([]); c.drawString(lx+34,yy-5,'pipeline, labeled with operator and system'); yy-=14
c.setLineWidth(0.5); c.setDash([4,3]); c.line(lx+10,yy-2,lx+28,yy-2); c.setDash([]); c.drawString(lx+34,yy-5,'quarter-section line'); yy-=14
c.setStrokeColor(G60); c.setLineWidth(0.4); c.setDash([1,2]); c.line(lx+10,yy-2,lx+28,yy-2); c.setDash([]); c.setStrokeColor(BLK); c.drawString(lx+34,yy-5,'soil unit (USDA-NRCS SSURGO), named in small caps')
# neatline
c.setStrokeColor(BLK); c.setLineWidth(2.2); pth=c.beginPath()
for k,i in enumerate([CORN['SW'],CORN['SE'],CORN['NE'],CORN['NW']]):
    X,Y=pg_grid(*P[i]); (pth.moveTo if k==0 else pth.lineTo)(X,Y)
pth.close(); c.drawPath(pth)
# calls along edges
calls={'S':('Thence N 77° E 1900 vrs. St & Earth mnd.', 'measured 5,306 ft · 1,910 vrs · true bearing N 75° E'),
       'E':('Thence N 13° W 1900 vrs. St & Earth mnd.', 'measured 5,319 ft · 1,915 vrs · true bearing N 15° W'),
       'N':('Thence S 77° W 1900 vrs. to the place of beginning.', 'measured 5,351 ft · 1,926 vrs · true bearing S 75° W'),
       'W':('Thence S 13° E 950 vrs. St & Earth mnd. 2 pls; 1900 vrs. St & Earth mnd. 4 pls.', 'measured 5,311 ft · 1,912 vrs · true bearing S 16° E')}
def edge_text(a,b,txt,sub,offset,flip=False):
    (X0,Y0)=pg_grid(*P[a]); (X1,Y1)=pg_grid(*P[b]); ang=math.degrees(math.atan2(Y1-Y0,X1-X0)); mx,my=(X0+X1)/2,(Y0+Y1)/2
    c.saveState(); c.translate(mx,my); c.rotate(ang); 
    c.setFont('Serif',10.5); c.setFillColor(BLK); c.drawCentredString(0,offset,txt); c.setFont('Cond',7.5); c.setFillColor(G40); c.drawCentredString(0,offset-11 if offset>0 else offset+12,sub); c.restoreState()
edge_text(CORN['NW'],CORN['NE'],*calls['N'],14)
edge_text(CORN['SW'],CORN['SE'],*calls['S'],-16)
edge_text(CORN['SE'],CORN['NE'],*calls['E'],-16)       # rotated 90: text reads bottom-to-top on right edge
edge_text(CORN['SW'],CORN['NW'],*calls['W'],14)      # left edge, reads bottom-to-top, text on outside
# corners
c.setFont('Cond',7); c.setFillColor(BLK); c.setLineWidth(0.8)
for k,(dx,dy,al) in {'SW':(8,8,'l'),'SE':(-8,8,'r'),'NE':(-8,-14,'r'),'NW':(8,-14,'l')}.items():
    X,Y=pg_grid(*P[CORN[k]]); c.circle(X,Y,3.5,stroke=1,fill=0); lat,lon=corner_latlon(CORN[k]); s=f"{k}  {lat:.5f}, {lon:.5f}"
    (c.drawRightString if al=='r' else c.drawString)(X+dx,Y+dy,s)
c.setFont('SerifI',8.5); X,Y=pg_grid(*P[CORN['NW']]); c.drawString(X+2,Y+30,'Beginning at a stake & Earth mnd, 4 pls, the S.W. corner of Survey No. 6')
# north arrow + scale bar (inside panel, lower right of section)
TRUE_N=15.1
X,Y=pg(W_ft-350,3450); c.saveState(); c.translate(X,Y); c.rotate(-TRUE_N); c.setLineWidth(1); c.setStrokeColor(BLK); c.setFillColor(BLK)
c.line(0,-40,0,40); pth=c.beginPath(); pth.moveTo(0,48); pth.lineTo(-5,34); pth.lineTo(5,34); pth.close(); c.drawPath(pth,fill=1); c.setFont('CondB',8); c.drawCentredString(0,52,'TRUE N'); c.restoreState()
c.setFont('Cond',7); c.drawCentredString(X,Y-62,'The sheet is oriented to the 1876 survey, not to north.')
# scale bar
sx,sy=pg(170,3100); c.setLineWidth(0.8)
for i in range(4): c.rect(sx+i*250*PPF,sy,250*PPF,4,stroke=1,fill=(i%2==0))
c.setFont('Cond',7)
for i in range(0,5): c.drawCentredString(sx+i*250*PPF,sy+7,str(i*250))
c.drawString(sx+1000*PPF+14,sy+7,'FEET')
V=2.7778*PPF  # pt per vara
for i in range(4): c.rect(sx+i*90*V,sy-8,90*V,4,stroke=1,fill=(i%2==1))
for i in range(0,5): c.drawCentredString(sx+i*90*V,sy-18,str(i*90))
c.drawString(sx+360*V+14,sy-18,'VARAS (33⅓ in)'); c.drawString(sx,sy+18,'SCALE 1 : 3,000   ·   1 INCH = 250 FEET')
# ---------- TITLE BLOCK ----------
ty=H-M
c.setFillColor(BLK); c.setFont('Serif',118); c.drawString(panel_x0-2,ty-1.35*inch,'SECTION 7')
c.setFont('Serif',15); c.drawString(panel_x0,ty-1.72*inch,'Block 39, Township 1 South, Texas & Pacific Railway Company Survey  ·  Abstract 34  ·  Midland County, Texas')
c.setFont('Serif',12); c.drawString(panel_x0,ty-2.02*inch,'ONE SQUARE MILE'); c.setFont('SerifI',12); c.drawString(panel_x0+c.stringWidth('ONE SQUARE MILE  ','Serif',12),ty-2.02*inch,'Desk Edition. Compiled from records, not walked.')
c.setFont('Serif',10.5); c.drawString(panel_x0,ty-2.28*inch,'First edition, October 2026. One copy. Corrections invited; anyone who corrects it gets the second edition free.')
rs=ParagraphStyle('r',fontName='Serif',fontSize=11,leading=14,textColor=RED)
fr=Frame(W-M-7.0*inch,ty-2.4*inch,3.4*inch,2.4*inch,leftPadding=0,rightPadding=0,topPadding=2,bottomPadding=0,showBoundary=0)
fr.addFromList([Paragraph('Surveyed 1 February 1876 and docketed under <b>Martin County</b>. Corrected to Midland County in red ink, 1887, two years after Midland County was organized. The county this ground sits in was itself a correction.',rs),
 Paragraph('<font size=9>On this sheet, red means the record disagreed with itself, or ran out.</font>',rs)],c)
# field notes reproduction in title block, right
fnim=Image.open(REPO+'glo-page-6.png'); fw_=fnim.size[0]; fnim.crop((0,int(fnim.size[1]*0.10),fw_,int(fnim.size[1]*0.36))).save('/home/claude/build/fieldnotes.jpg',quality=90)
iw=3.3*inch; ih=iw*(0.26*fnim.size[1])/fw_
c.drawImage('/home/claude/build/fieldnotes.jpg',W-M-iw,ty-ih,width=iw,height=ih); c.setStrokeColor(G60); c.setLineWidth(0.4); c.rect(W-M-iw,ty-ih,iw,ih)
c.setFont('Serif',8.4); c.setFillColor(BLK); c.drawString(W-M-iw,ty-ih-11,'Powell’s field notes, 1 Feb 1876, as filed. “Martin,” struck. GLO Bexar Scrip File 020113.')
# ---------- AERIAL STRIP ----------
g=0.2*inch; fw=(panel_w-5*g)/6
years=[('1954','USGS single frame, 1:63,000, 2 May 1954','/home/claude/build/base_1954.png'),('1965','USGS single frame, 1:21,400, 20 Feb 1965','/home/claude/build/base_1965.png'),('1974','USGS single frame, 1:29,000, 19 Feb 1974','/home/claude/build/base_1974.png'),
       ('1984','USGS NHAP, 28 Oct 1984','/home/claude/build/base_1984.png'),('1995','USGS NAPP color-infrared, 19 Dec 1995','/home/claude/build/base_1995.png'),('2022','USDA NAIP, 24 Sep 2022','/home/claude/build/base_naip.png')]
# strip crop = polygon bbox + 10% in local frame, square
side=max(W_ft,H_ft)*1.1; cx0=(loc_minx+loc_maxx)/2; cy0=(loc_miny+loc_maxy)/2
u0,v0=local_to_px(cx0-side/2,cy0+side/2); u1,v1=local_to_px(cx0+side/2,cy0-side/2)
for i,(yr,src,img) in enumerate(years):
    x=panel_x0+i*(fw+g); y=strip_y0
    c.setStrokeColor(BLK); c.setLineWidth(0.6)
    if img:
        im=cv2.imread(img,0)[int(v0):int(v1),int(u0):int(u1)]; im=cv2.resize(im,(1000,1000),interpolation=cv2.INTER_AREA); lo,hi_=np.percentile(im[im>0],(1,99)); im=np.clip((im.astype(float)-lo)/(hi_-lo)*235+10,0,255).astype(np.uint8); 
        Image.fromarray(im).save(f'/home/claude/build/strip_{yr}.jpg',quality=88); c.drawImage(f'/home/claude/build/strip_{yr}.jpg',x,y+0.42*inch,fw,fw)
        # section outline on strip
        c.setLineWidth(0.5); c.setStrokeColor(BLK); pth=c.beginPath()
        for k,ii in enumerate([CORN['SW'],CORN['SE'],CORN['NE'],CORN['NW']]):
            lx,ly=L[ii]; X=x+(lx-(cx0-side/2))/side*fw; Y=y+0.42*inch+(ly-(cy0-side/2))/side*fw; (pth.moveTo if k==0 else pth.lineTo)(X,Y)
        pth.close(); c.drawPath(pth)
    else:
        c.setDash([3,3]); c.rect(x,y+0.42*inch,fw,fw); c.setDash([]); c.setFont('CondM',8); c.setFillColor(G60); c.drawCentredString(x+fw/2,y+0.42*inch+fw/2,'FRAME NOT YET ALIGNED')
    c.setFillColor(BLK); c.setFont('Serif',13); c.drawString(x,y+0.22*inch,yr); c.setFont('Cond',7.5); c.setFillColor(G40); c.drawString(x+c.stringWidth(yr,'Serif',13)+5,y+0.22*inch,src)
    c.setFont('Cond',7); c.drawString(x,y+0.06*inch,{'1954':'Open range; the draw plain across the north. Placement approximate, error over 500 ft.','1965':'Still range; a road on the west line, a pad at the draw. Placement approximate, ±300–500 ft.','1974':'First graded corridors. Placement ±300 ft, two control points on the south-line road.','1984':'Streets and a golf course under construction, south half. ±150 ft.','1995':'Course mature, south half built out. North half still range. ±150 ft.','2022':'Built out to the plat. North half: pads, gathering lines, a caliche yard. Orthoimage.'}[yr])
# ---------- TEXT ZONE ----------
body=ParagraphStyle('b',fontName='Serif',fontSize=10.6,leading=13,alignment=TA_JUSTIFY,spaceAfter=3)
head=ParagraphStyle('h',fontName='CondB',fontSize=12.5,leading=15,spaceAfter=4)
red=ParagraphStyle('rb',parent=body,textColor=RED,alignment=0); redh=ParagraphStyle('rh',parent=head,textColor=RED)
small=ParagraphStyle('s',fontName='Serif',fontSize=8.4,leading=10.2,alignment=TA_JUSTIFY,spaceBefore=6)
cw=(panel_w-2*g)/3
def col(i,items):
    f=Frame(panel_x0+i*(cw+g),text_y0,cw,text_h,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0,showBoundary=0); f.addFromList(items,c)
    return f
A_=[Paragraph('CHAIN OF TITLE, 1876–1982  ·  complete, no gaps',head)]+[Paragraph(t,body) for t in [
'<b>1876.</b> Surveyed 1 Feb by deputy surveyor W.C. Powell, chain carriers L.E. Wright and E.C. Bennett, “on the waters of North Concho.” Bearings in varas. Filed at the General Land Office 27 Dec.',
'<b>1876.</b> Land Scrip No. 3123, 25 May: the Texas & Pacific has built 203 miles, 4,624 feet of railroad. This section is part of what that construction earned. Odd-numbered — railroad land, not school land.',
'<b>1883.</b> Patented 15 Dec to Texas and Pacific Railway Co. Patent 540, Vol. 68, p. 503. 640 acres.',
'<b>1906.</b> Charles J. Canda, trustee of the Texas Pacific Land Trust → Mrs. Mary T. Edwards, 640 acres. Recorded 6 Jan 1906, Deed Records 12/54. Three notes of $795.',
'<b>1911.</b> Mary T. Edwards and heirs → S.H. Holloway, with Sections 6, 8, 17, 18; buyer assumes the 1906 notes. Four months later Holloway → S.W. Estes. <i>The Estes years begin.</i>',
'<b>1921.</b> S.W. and Arminta Estes → Thelma Estes, about 160 acres.',
'<b>1976.</b> Ethel Aldredge Estes → Aldredge Estes Jr.',
'<b>1978.</b> The Estes family → Midland West Corp., 31 Oct. Surface and surface rights only, SE/4, 160 acres. Minerals stay with the family. Consideration: ten dollars and the note.',
'<b>1981–82.</b> Midland West → Hailco Inc. (plat-joinder parcel). BSD Inc. → Midland West, agreement.',
'<b>1982.</b> Green Tree North plat recorded 1 Dec. Cabinet C, p. 134. Developer: Midland West Corporation.',
'<i>The chain stops here. Sixty-seven years of one family; ninety-nine years of ranch. Everything since is somebody’s home and is not this map’s business.</i>']]
B_=[Paragraph('THE GROUND',head)]+[Paragraph(t,body) for t in [
'<b>Water.</b> Ogallala aquifer 100–180 ft below the section. One City of Midland well inside the line, 147 ft, unused. About ten domestic and irrigation wells drilled 2002–2021, 135–180 ft. Golf course well, 175 ft, 2021. Midland Draw crosses the north half and has carried its name on every USGS sheet from 1954 to 2019 — it never disappeared; the ranch did. Powell’s 1876 notes call this “waters of North Concho.” Modern mapping drains it east to the Colorado by Midland Draw and Beals Creek; the North Concho is not on the path.',
'<b>Soil.</b> About 60% Amarillo and Midessa fine sandy loam — well drained, “farmland of statewide importance.” Bippus clay loam in the draws, subject to occasional flooding. No hydric soils. Water table below 80 in. A “sandy old farm with one sickly tree,” as the man who sold it put it in 1977.',
'<b>Oil.</b> Inside the line: three producing wells, one permitted location, one dry hole. On the north line, three horizontal pads; two laterals run south under the streets, one runs north. Those three carry Martin County’s code in their API numbers though they sit in Midland County — the Railroad Commission assigns the code by the county it approved the drilling under, which is its rule and not an explanation. Two crude gathering lines (Oryx “Green Tree” system, 6.63 in) and one 16-in gas line (ONEOK WesTex) cross the north half. Operators, dates, and depths could not be pulled; the Commission’s wellbore service was down for the whole compilation.',
'<b>Before the streets.</b> Open rangeland on every USGS edition 1954–1985: oil wells, drill holes, a gravel pit, a pipeline. Streets first appear 1991. Built out by 2010.',
'<b>The course.</b> Summer 1977: two men buy 320 acres from the Estes family, one of them the head pro at Ranchland Hills. First National Bank finances it — $8.9 million, later litigated. Dirt-trail access until 1980. Course opens 1980–81; nine more holes 1985; rebuilt 2018.',
'<b>The measure.</b> Powell called 1,900 varas on every side. The county’s polygon measures 1,910 to 1,926. The section holds about 650 acres against 640 patented — ten acres of survey excess that nobody has had to account for in 150 years.']]
C_=[Paragraph('COULD NOT BE CONFIRMED',redh),Paragraph('Compiled from records, not walked. The following were looked for and not found, or found and not trusted:',red)]+[Paragraph('· '+t,red) for t in [
'Identity of the pipeline drawn on the 1954 and 1966 USGS sheets.',
'Whether the 1978 gathering line is the T-4 Permit 10611 “Green Tree” system. Likely; not shown by any single record.',
'Operators, completion dates, and depths of the wells (RRC wellbore service unavailable throughout compilation). One dry hole’s API number returned truncated and is printed as unconfirmed.',
'Why three wells inside a Midland County section were permitted under Martin County’s code. The rule is in the Commission’s data dictionary; the reason for these three is in no public record.',
'Which quarter Thelma Estes received in 1921.',
'Whether Thelma Estes and Ethel Aldredge Estes are the same person. No instrument says so.',
'Hailco Inc.: who they were. The nature of the 1982 BSD Inc. agreement.',
'First lot sold, first house built, first price paid.',
'Any 1930s–40s aerial. A 1944 Air Force frame exists at TxGIO and was not ordered.',
'Powell records a magnetic variation of 12° 9½′ E; applied conventionally his lines would run near-cardinal. The ground runs 14° off. Which convention he used is not known.',
'Anything the Reporter-Telegram printed about this ground; the archive is paywalled.']]+[Paragraph('If you know any of these, write. Second edition is free to anyone who corrects the first.',red),
Paragraph('<b>Sources.</b> Texas General Land Office (patent, field notes, scrip); Midland County Clerk (deed records as cited); Midland Central Appraisal District (abstracts, parcels); USGS topoView and EarthExplorer (topographic sheets 1954–2019; aerials 1954, 1965, 1974, 1984, 1995); USDA NAIP 2022; Railroad Commission of Texas GIS; Texas Water Development Board; USDA-NRCS Web Soil Survey; EPA WATERS / NHDPlus; federal court records as cited. Full source log, forty-six rows, at github.com/acwil88/One-square-mile.',small),
Paragraph('Gathered by Skippy (Meta Muse). Designed by Claude (Anthropic). Approved and paid for by a resident of the section, who is not named on it. No phone calls were made. Sheet oriented to the 1876 survey; true north 15° right of page-up. Scale 1:3,000. Aerial strip: each frame’s placement error is stated in its caption.',small)]
from reportlab.platypus import Image as RLImage, Spacer
fnim=Image.open(REPO+'glo-page-6.png'); fw_=fnim.size[0]; fnim.crop((0,int(fnim.size[1]*0.10),fw_,int(fnim.size[1]*0.36))).save('/home/claude/build/fieldnotes.jpg',quality=90)
fn_w=cw*0.92; fn_h=fn_w*(0.26*fnim.size[1])/fw_
col(0,A_); col(1,B_); col(2,C_)
c.showPage(); c.save(); print('ok')
