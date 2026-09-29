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
F=REPO+'fonts/'
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
c=canvas.Canvas(BUILD+'proof-v10.pdf',pagesize=(W,H)); c.setTitle('Section 7, Block 39, T-1-S — One Square Mile, Desk Edition'); c.setAuthor('Claude (Anthropic) and Skippy (Meta Muse) for a resident of the section'); c.setSubject('First edition, October 2026')
BLEED=250.0  # ft shown beyond the section
def clip_rect():
    x0,y0=pg(loc_minx-BLEED,loc_miny-BLEED); x1,y1=pg(loc_maxx+BLEED,loc_maxy+BLEED); return x0,y0,x1-x0,y1-y0
# ---------- MAIN PANEL ----------
c.saveState(); p=c.beginPath(); p.rect(*clip_rect()); c.clipPath(p,stroke=0)
# base raster
base=cv2.imread(BUILD+'base_main.png',0)
from PIL import Image
Image.fromarray(base).save(BUILD+'base_main.jpg',quality=85)
bx,by=pg(loc_minx-PAD,loc_miny-PAD); c.drawImage(BUILD+'base_main.jpg',bx,by,width=(W_ft+2*PAD)*PPF,height=(H_ft+2*PAD)*PPF)
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
# 1966 USGS features (windmill, building, gravel pit)
for lat,lon,kind,lab in [(32.0647,-102.1588,'wm','WINDMILL, USGS 1966'),(32.0616,-102.1732,'bldg','BUILDING, USGS 1966'),(32.0631,-102.1743,'pit','GRAVEL PIT, USGS 1966')]:
    gx,gy=T.transform(lon,lat); X,Y=pg_grid(gx,gy); c.setStrokeColor(BLK); c.setLineWidth(0.8); c.setFillColor(white)
    if kind=='wm': c.circle(X,Y,4,stroke=1,fill=1); c.line(X-4,Y,X+4,Y); c.line(X,Y-4,X,Y+4); c.line(X-3,Y-3,X+3,Y+3); c.line(X-3,Y+3,X+3,Y-3)
    elif kind=='bldg': c.rect(X-3.5,Y-3.5,7,7,stroke=1,fill=1)
    else: c.setDash([1,2]); c.circle(X,Y,5,stroke=1,fill=0); c.setDash([])
    c.setFont('Cond',6); c.setFillColor(BLK); c.drawString(X+7,Y-2,lab)
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
c.setFont('Cond',7.5); c.setFillColor(BLK); X,Y=pg_grid(*(P[CORN['SE']]*0.5+((P[CORN['SW']]+P[CORN['NE']])/2)*0.5)); c.drawCentredString(X,Y+120*PPF,'SE/4 · 160 ACRES · SURFACE ONLY · NOV 1978')
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
    if r['api'].startswith('42-317'):
        # bottomhole (toe) of a horizontal whose pad is ~2.5 mi north in Martin County: open square, tick toward the pad
        c.setFillColor(white); c.rect(X-s,Y-s,2*s,2*s,stroke=1,fill=1); c.setFillColor(BLK)
        ang=math.radians(90-(345-344.9)); c.setLineWidth(1.2); c.line(X,Y+s,X+38*math.cos(ang),Y+s+38*math.sin(ang))
    elif st=='active': c.circle(X,Y,s,stroke=1,fill=1)
    elif st=='dry hole': c.circle(X,Y,s,stroke=1,fill=0); c.line(X-s,Y-s,X+s,Y+s); c.line(X-s,Y+s,X+s,Y-s)
    elif st=='plugged': c.circle(X,Y,s,stroke=1,fill=0); c.line(X-s,Y,X+s,Y)
    else: c.circle(X,Y,s,stroke=1,fill=0)   # permitted
    c.setFont('Cond',6); api=r['api'] if 'xxxxx' not in r['api'] else '42-329-(unconfirmed)'
    lease={'42-329-37587':'Estes Button 7-8 Unit','42-329-35205':'Estes Button 7','42-329-39287':'Stephens Fee 6','42-329-36421':'Aldridge','42-317-45816':'Easy Target','42-317-45818':'Easy Target','42-317-45820':'Easy Target'}.get(r['api'],'')
    yr=(r.get('completion_date') or r.get('spud_date') or '')[:4]
    stl={'permitted':'permitted, never drilled','dry hole':'dry hole','plugged':'plugged','active':'producing'}.get(st,st)
    op=r.get('operator','').title().replace('Llc','LLC').replace('L.P.','LP').replace('Ltd.','Ltd').replace('Parish, John R.','John R. Parish')
    if r['api'].startswith('42-317'):
        if r['well_name']=='4H':
            c.setFont('Cond',6); c.drawString(X+s+4,Y-s-8,'toes of the three Easy Target laterals · Occidental · 2024 · pads 2½ mi north, Martin Co. · 42-317-45816 / -45818 / -45820')
        continue
    lab=f"{api}  {lease+' ' if lease else ''}#{r['well_name']} · {stl}"+(f" · {op}" if op else '')+(f" · {yr}" if yr else '')+(f" · {int(r['td_ft']):,} ft" if r.get('td_ft') else '')
    c.drawString(X+s+2,Y+3,lab)
c.restoreState()
# legend
lx,ly=pg(120,3350); lw_,lh_=2.9*inch,2.1*inch
c.setFillColor(Color(1,1,1,alpha=0.82)); c.setStrokeColor(BLK); c.setLineWidth(0.6); c.rect(lx,ly,lw_,lh_,stroke=1,fill=1)
c.setFillColor(BLK); c.setFont('CondB',8.5); c.drawString(lx+8,ly+lh_-14,'WELLS  (Railroad Commission of Texas, Sept 2026)')
items=[('producing','fill'),('toe of a horizontal well; tick points to its pad, 2½ mi north','sq'),('permitted, not drilled','open'),('dry hole','dry'),('plugged','plug')]
yy=ly+lh_-30
for lab,k in items:
    X=lx+16; s_=3.6; c.setLineWidth(0.8)
    if k=='fill': c.circle(X,yy,s_,stroke=1,fill=1)
    elif k=='sq': c.setFillColor(white); c.rect(X-s_,yy-s_,2*s_,2*s_,stroke=1,fill=1); c.setFillColor(BLK); c.setLineWidth(1.2); c.line(X,yy+s_,X+2,yy+12)
    elif k=='open': c.circle(X,yy,s_,stroke=1,fill=0)
    elif k=='dry': c.circle(X,yy,s_,stroke=1,fill=0); c.line(X-s_,yy-s_,X+s_,yy+s_); c.line(X-s_,yy+s_,X+s_,yy-s_)
    else: c.circle(X,yy,s_,stroke=1,fill=0); c.line(X-s_,yy,X+s_,yy)
    c.setFont('Cond',8); c.drawString(X+18,yy-3,lab); yy-=14
c.setLineWidth(0.9); c.setDash([5,3]); c.line(lx+10,yy-2,lx+28,yy-2); c.setDash([]); c.drawString(lx+34,yy-5,'pipeline, labeled with operator and system'); yy-=14
c.setLineWidth(0.5); c.setDash([4,3]); c.line(lx+10,yy-2,lx+28,yy-2); c.setDash([]); c.drawString(lx+34,yy-5,'quarter-section line'); yy-=14
c.setStrokeColor(G60); c.setLineWidth(0.4); c.setDash([1,2]); c.line(lx+10,yy-2,lx+28,yy-2); c.setDash([]); c.setStrokeColor(BLK); c.drawString(lx+34,yy-5,'soil unit (USDA-NRCS SSURGO), named in small caps'); yy-=14
c.setFillColor(white); c.circle(lx+19,yy-2,3.5,stroke=1,fill=1); c.setFillColor(BLK); c.drawString(lx+34,yy-5,'windmill · building · gravel pit as drawn on the 1966 USGS sheet')
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
fnim=Image.open(REPO+'glo-page-6.png'); fw_=fnim.size[0]; fnim.crop((0,int(fnim.size[1]*0.10),fw_,int(fnim.size[1]*0.36))).save(BUILD+'fieldnotes.jpg',quality=90)
iw=3.3*inch; ih=iw*(0.26*fnim.size[1])/fw_
c.drawImage(BUILD+'fieldnotes.jpg',W-M-iw,ty-ih,width=iw,height=ih); c.setStrokeColor(G60); c.setLineWidth(0.4); c.rect(W-M-iw,ty-ih,iw,ih)
c.setFont('Serif',8.4); c.setFillColor(BLK); c.drawString(W-M-iw,ty-ih-11,'Powell’s field notes, 1 Feb 1876, as filed. “Martin,” struck. GLO Bexar Scrip File 020113.')
# ---------- AERIAL STRIP ----------
g=0.18*inch; fw=(panel_w-6*g)/7
years=[('1946','USDA, 20 Feb 1946, two frames mosaicked',BUILD+'base_1946.png'),('1954','USGS single frame, 1:63,000, 2 May 1954',BUILD+'base_1954.png'),('1965','USGS single frame, 1:21,400, 20 Feb 1965',BUILD+'base_1965.png'),('1974','USGS single frame, 1:29,000, 19 Feb 1974',BUILD+'base_1974.png'),
       ('1984','USGS NHAP, 28 Oct 1984',BUILD+'base_1984.png'),('1995','USGS NAPP color-infrared, 19 Dec 1995',BUILD+'base_1995.png'),('2022','USDA NAIP, 24 Sep 2022',BUILD+'base_naip.png')]
# strip crop = polygon bbox + 10% in local frame, square
side=max(W_ft,H_ft)*1.1; cx0=(loc_minx+loc_maxx)/2; cy0=(loc_miny+loc_maxy)/2
u0,v0=local_to_px(cx0-side/2,cy0+side/2); u1,v1=local_to_px(cx0+side/2,cy0-side/2)
for i,(yr,src,img) in enumerate(years):
    x=panel_x0+i*(fw+g); y=strip_y0
    c.setStrokeColor(BLK); c.setLineWidth(0.6)
    if img:
        im=cv2.imread(img,0)[int(v0):int(v1),int(u0):int(u1)]; im=cv2.resize(im,(1000,1000),interpolation=cv2.INTER_AREA); lo,hi_=np.percentile(im[im>0],(1,99)); im=np.clip((im.astype(float)-lo)/(hi_-lo)*235+10,0,255).astype(np.uint8); 
        Image.fromarray(im).save(BUILD+f'strip_{yr}.jpg',quality=88); c.drawImage(BUILD+f'strip_{yr}.jpg',x,y+0.42*inch,fw,fw)
        # section outline on strip
        c.setLineWidth(0.5); c.setStrokeColor(BLK); pth=c.beginPath()
        for k,ii in enumerate([CORN['SW'],CORN['SE'],CORN['NE'],CORN['NW']]):
            lx,ly=L[ii]; X=x+(lx-(cx0-side/2))/side*fw; Y=y+0.42*inch+(ly-(cy0-side/2))/side*fw; (pth.moveTo if k==0 else pth.lineTo)(X,Y)
        pth.close(); c.drawPath(pth)
    else:
        c.setDash([3,3]); c.rect(x,y+0.42*inch,fw,fw); c.setDash([]); c.setFont('CondM',8); c.setFillColor(G60); c.drawCentredString(x+fw/2,y+0.42*inch+fw/2,'FRAME NOT YET ALIGNED')
    c.setFillColor(BLK); c.setFont('Serif',12); c.drawString(x,y+0.22*inch,yr); c.setFont('Cond',7); c.setFillColor(G40); c.drawString(x+c.stringWidth(yr,'Serif',13)+5,y+0.22*inch,src)
    c.setFont('Cond',6.6); c.drawString(x,y+0.06*inch,{'1946':'Range, one field, a full playa, outbuildings on the west line, no house. Approximate, ±600–900 ft.','1954':'Open range; the draw plain across the north. Approximate, over 500 ft.','1965':'Still range; a road on the west line, a pad at the draw. Approximate, ±300–500 ft.','1974':'First graded corridors. Placement ±300 ft, two control points on the south-line road.','1984':'Streets and a golf course under construction, south half. ±150 ft.','1995':'Course mature, south half built out. North half still range. ±150 ft.','2022':'Built out to the plat. North half: pads, gathering lines, a caliche yard. Orthoimage.'}[yr])
# ---------- TEXT ZONE ----------
body=ParagraphStyle('b',fontName='Serif',fontSize=9.1,leading=11.0,alignment=TA_JUSTIFY,spaceAfter=3)
head=ParagraphStyle('h',fontName='CondB',fontSize=12.5,leading=15,spaceAfter=4)
red=ParagraphStyle('rb',parent=body,textColor=RED,alignment=0); redh=ParagraphStyle('rh',parent=head,textColor=RED)
small=ParagraphStyle('s',fontName='Serif',fontSize=8.4,leading=10.2,alignment=TA_JUSTIFY,spaceBefore=6)
fr_=[0.42,0.32,0.26]; cws=[(panel_w-2*g)*f for f in fr_]; cw=cws[0]
def col(i,items):
    x=panel_x0+sum(cws[:i])+i*g
    f=Frame(x,text_y0,cws[i],text_h,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0,showBoundary=0); f.addFromList(items,c)
    if items: print('col',i,'overflow items:',len(items))
    return f
A_=[Paragraph('CHAIN OF TITLE, 1876–1983  ·  complete, no gaps',head)]+[Paragraph(t,body) for t in [
'<b>1876.</b> Surveyed 1 Feb by deputy surveyor W.C. Powell, chain carriers L.E. Wright and E.C. Bennett, “on the waters of North Concho.” Bearings in varas. Filed at the General Land Office 27 Dec.',
'<b>1876.</b> Land Scrip No. 3123, 25 May: the Texas & Pacific has built 203 miles, 4,624 feet of railroad. This section is part of what that construction earned. Odd-numbered — railroad land, not school land.',
'<b>1883.</b> Patented 15 Dec to Texas and Pacific Railway Co. Patent 540, Vol. 68, p. 503. 640 acres.',
'<b>1906.</b> Charles J. Canda, trustee of the Texas Pacific Land Trust → Mrs. Mary T. Edwards, 640 acres. Recorded 6 Jan, Deed Records 12/54. Three notes of $795.',
'<b>1911.</b> Mary T. Edwards and heirs → S.H. Holloway, with Sections 6, 8, 17, 18; buyer assumes the 1906 notes. Four months later Holloway → S.W. Estes. <i>The Estes years begin.</i>',
'<b>1921.</b> Arminta Estes → Thelma Estes, 7 June. DR 30/144. The whole section; her 1923 deeds of trust cover all 640 acres.',
'<b>1940.</b> Thelma Estes Brown and W.T. Brown → Magnolia Pipe Line Company, right-of-way across the 640 acres, 2 Dec. DR 67/531. That is the pipeline on the 1954 and 1966 USGS sheets.',
'<b>1941.</b> Family partition, 31 Oct, four instruments in a row. Thelma Estes Brown → Aldredge Estes, Section 7 (DR 70/294); Aldredge → Thelma, Section 6, the same day. Both had taken land from S.W. and Arminta. Kin, plainly; the records never say how. Thelma died in 1983 at 80, in Laguna Hills, California.',
'<b>1953, 1970.</b> Ethel Estes, Aldredge’s wife, then widow: a royalty deed on the 640 acres to Stanolind Oil & Gas; an oil and gas lease to Pan American Petroleum.',
'<b>1976.</b> Ethel Aldredge Estes → her three children, 14 Dec. DR 615/436–438.',
'<b>1978.</b> The Estes family → Midland West Corporation, 21–22 Nov, three deeds. Surface only; the minerals stay with the family. A deed of trust runs back to Mrs. Estes on the SE/4.',
'<b>1979.</b> The Estes heirs and Midland West → Pioneer Natural Gas Company, right-of-way, October. DR 673/712–714. Today’s 16-in gas line; ONEOK WesTex is Pioneer’s successor.',
'<b>1979.</b> Midland West, about a dozen partners, opens the Green Tree course in July.',
'<b>1980–81.</b> Midland West → Hailco Inc. (incorporated May 1979; Neal Hail, president), a Midland homebuilder buying finished lots.',
'<b>1982.</b> 8 Jan: Midland West sells 20.343 acres — Lots 20–23, Block 6, the seed of Green Tree North — to The Greens, a joint venture of Hailco, Dovecote Inc., and BSD Inc., for $1,348,425 cash, with a four-year build-or-reconvey clock and a promise to annex, plat, zone, pave, and pipe the land. DR 731/258.',
'<b>1982.</b> Green Tree North plat recorded 1 Dec. Cabinet C, p. 134. Frank Mullins becomes majority owner of Midland West the same month.',
'<b>1983.</b> 26 Jan: the first Green Tree North lot is deeded to a homebuyer — Lot 18, Block 2, from Midland West. DR 770/614. 1 March: the members buy the clubhouse and both courses from Midland West for more than $6 million. Green Tree North — 297 acres, 220 lots, nine more holes — under construction, 85 lots pre-sold, First National Bank of Midland carrying the paper. Three years later a First National banker is convicted in federal court of hiding his own stake in Midland West while the bank lent it $1.925 million.',
'<b>1989.</b> Ten acres at the northeast corner of the SE/4, deeded 15 Sept to the family’s ranch partnership. Still theirs.',
'<i>The chain stops here. Sixty-seven years of one family; ninety-nine years of ranch. Everything since is somebody’s home and is not this map’s business.</i>']]
B_=[Paragraph('THE GROUND',head)]+[Paragraph(t,body) for t in [
'<b>Water.</b> Ogallala aquifer 100–180 ft below the section. One City of Midland well inside the line, 147 ft, unused. About ten domestic and irrigation wells drilled 2002–2021, 135–180 ft. Golf course well, 175 ft, 2021. Midland Draw crosses the north half and has carried its name on every USGS sheet from 1954 to 2019 — it never disappeared; the ranch did. Powell’s 1876 notes call this “waters of North Concho.” Modern mapping drains it east to the Colorado by Midland Draw and Beals Creek; the North Concho is not on the path.',
'<b>Soil.</b> About 60% Amarillo and Midessa fine sandy loam — well drained, “farmland of statewide importance.” Bippus clay loam in the draws, subject to occasional flooding. No hydric soils. Water table below 80 in. A “sandy old farm with one sickly tree,” as the man who sold it put it in 1977.',
'<b>Oil.</b> Fourteen locations on the Commission’s map. Inside the line: a dry hole drilled by John R. Parish in December 1980; Exxon’s No. 1 of 1998, still producing; Petroplex’s Estes Button 7 No. 3 (2005) and the 7-8 Unit No. 4 (2011); Fasken’s Aldridge 1208R (2009), after Henry Resources’ 1208 came up dry; Endeavor’s Stephens Fee No. 3 (2014), since plugged; and three permits that expired without a bit turning. Under the north line, the toes of three Occidental horizontals — the Easy Target wells — spudded within four days of each other in early 2024 from one pad two and a half miles north in Martin County, laterals of 24,000 to 26,000 feet that come south and stop a hundred feet inside this section. Their numbers carry Martin County’s code, and rightly: tested against 18,000 permits along this county line, the Commission’s code follows the surface hole every time. Two crude gathering lines — Oryx Midland Oil Gathering’s “Green Tree” system, 6.63 in, T-4 Permit 10611, issued in 2024 to serve those pads — and one 16-in gas line (ONEOK WesTex, on Pioneer Natural Gas’s 1979 right-of-way) cross the north half. The leases are still named for the family.',
'<b>Before the streets.</b> Open rangeland on every USGS edition 1954–1985: oil wells, drill holes, a gravel pit, a pipeline. Streets first appear 1991. Built out by 2010.',
'<b>The course.</b> Summer 1977: two men buy 320 acres from the Estes family, one of them the head pro at Ranchland Hills. First National Bank finances it — $8.9 million, later litigated. Dirt-trail access until 1980. The course opens July 1979; the members own it from March 1983; the north nine follows; rebuilt 2018.',
'<b>The measure.</b> Powell called 1,900 varas on every side. The county’s polygon measures 1,910 to 1,926. The section holds about 650 acres against 640 patented — ten acres of survey excess that nobody has had to account for in 150 years. And the tilt is not his mistake: every section in Block 39 runs 14° off north. He ran his lines by needle and wrote the variation down without correcting for it; the whole block is the fossil of his compass.']]
C_=[Paragraph('COULD NOT BE CONFIRMED',redh),Paragraph('Compiled from records, not walked. The following were looked for and not found, or found and not trusted:',red)]+[Paragraph('· '+t,red) for t in [
'One dry hole, Well No. 1, plotted from the Commission’s hardcopy map with no API number on file. Its operator and date are in no digital record.',
'What the first lot sold for. A course-front lot was asking $55,000 that winter; the first deed of trust is indexed at a figure too small to believe.',
'Any 1930s–40s aerial. A 1944 Air Force frame exists at TxGIO and is on order; it did not arrive in time for this edition.',
'Where on the ranch the calves of 1916 and the reunion of 1921 were. Not on this section, which had no house in 1946; which of the family’s other sections is not known.']]+[Paragraph('If you know any of these, write. Second edition is free to anyone who corrects the first.',red),
Paragraph('<b>Sources.</b> Texas General Land Office (patent, field notes, scrip); Midland County Clerk (deed records as cited); Midland Central Appraisal District (abstracts, parcels); USGS topoView and EarthExplorer (topographic sheets 1954–2019, features from the 1966 Northwest Midland 7.5′ sheet; aerials 1954, 1965, 1974, 1984, 1995); WellWiki, ezrrc, and texas-drilling mirrors of RRC permit and completion data; Midland Reporter-Telegram 1950–1999 via the Southwest Collection, Texas Tech University; Texas Comptroller entity records; USDA 1946 aerials, frames 67–68 (TxGIO); USDA NAIP 2022 (NAIP 2024 exists as a county mosaic in a proprietary format and was not used); Railroad Commission of Texas GIS and 2024 T-4 permit register; Texas Water Development Board; USDA-NRCS Web Soil Survey; EPA WATERS / NHDPlus; federal court records as cited. Full source log, fifty-plus rows, at github.com/acwil88/One-square-mile.',small),
Paragraph('Gathered by Skippy (Meta Muse). Designed by Claude (Anthropic). Approved and paid for by a resident of the section, who is not named on it. No phone calls were made. Sheet oriented to the 1876 survey; true north 15° right of page-up. Scale 1:3,000. Aerial strip: each frame’s placement error is stated in its caption.',small)]
from reportlab.platypus import Image as RLImage, Spacer
fnim=Image.open(REPO+'glo-page-6.png'); fw_=fnim.size[0]; fnim.crop((0,int(fnim.size[1]*0.10),fw_,int(fnim.size[1]*0.36))).save(BUILD+'fieldnotes.jpg',quality=90)
fn_w=cw*0.92; fn_h=fn_w*(0.26*fnim.size[1])/fw_
col(0,A_); col(1,B_); col(2,C_)
c.showPage(); c.save(); print('ok')
