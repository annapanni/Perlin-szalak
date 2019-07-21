from numpy_perlin import perlin
from PIL import Image, ImageDraw
import random, math

nyilak=10
kepsize=1600
size=800
pottyszam=4000
r=500
color=(random.randint(0, 255),random.randint(0, 255), random.randint(0, 255), 30 )

img = Image.new("RGB", (kepsize, kepsize), color="black")
d = ImageDraw.Draw(img, "RGBA")

xp=(perlin(kepsize, nyilak)-120)/60
yp=(perlin(kepsize, nyilak)-120)/60
rad=0

for i in range(pottyszam):
    rad+=2*math.pi/pottyszam
    x=math.cos(rad)*r+kepsize/2
    y=math.sin(rad)*r+kepsize/2
    path=[]
    for _ in range(2000):
        x+=xp[int(x), int(y)]
        if x>=kepsize or x<0:
            break
        y+=yp[int(x), int(y)]
        if y>= kepsize or y<0:
            break
        path.append((x,y))
    d.line(path, fill=(color), width=2)


img2=img.resize((size, size), Image.ANTIALIAS)
img2.show()

img2.save("korkep{}.png" .format(str(random.randint(1000,9999))))