from numpy_perlin import perlin
from PIL import Image, ImageDraw
import random

nyilak=5
kepsize=3200
size=1600
pottyszam=4000
color=random.randint(0, 255),random.randint(0, 255), random.randint(0, 255), 30 

img = Image.new("RGB", (kepsize, kepsize), color="black")
d = ImageDraw.Draw(img, "RGBA")

xp=(perlin(kepsize, nyilak)-120)/60
yp=(perlin(kepsize, nyilak)-120)/60
print(xp.dtype)

for i in range(pottyszam):
    x, y=random.randint(0, kepsize-1), random.randint(0, kepsize-1)
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
img2.save("szalkep{}.png" .format(str(random.randint(1000,9999))))