from PIL import Image
import numpy as np
import math
#np.random.seed(42)

def smoothstep(x):
    return np.clip(3*x**2-2*x**3, 0,1)

def interpol (a, b, t):
##    return a+t*(b-a)
    return a+smoothstep(t)*(b-a)

def dot(a,b):
    return a[:,:,0]*b[:,:,0]+a[:,:,1]*b[:,:,1]

def perlin(kepsize, nyilszájz):
    kep =(np.random.rand(kepsize,kepsize)*10).astype(int)
    nyil=np.random.rand(nyilszájz, nyilszájz, 2)*2-1
    hosszak=np.sqrt(nyil[:,:,0]**2+nyil[:,:,1]**2)
    nyil=nyil/np.repeat(np.expand_dims(hosszak, axis =2),2,axis=2)

    x,y=np.meshgrid(range(0,kepsize), range(0,kepsize))

    ##egészrész
    doboz=math.ceil(kepsize/(nyilszájz-1))
    ux, uy=x//doboz, y//doboz
    ex, ey=ux*doboz ,uy*doboz
    ##törtrész
    ibf=np.stack(((x-ex)/doboz,(y-ey)/doboz), axis=2)
    iba=np.stack(((x-ex)/doboz, (ey-y+doboz)/doboz), axis=2)
    ijf=np.stack(((ex-x+doboz)/doboz, (y-ey)/doboz), axis=2)
    ija=np.stack(((ex-x+doboz)/doboz, (ey-y+doboz)/doboz), axis=2)

##    print(ibf)
    bf=nyil[ux, uy]
    ba=nyil[ux, uy+1]
    jf=nyil[ux+1, uy]
    ja=nyil[ux+1, uy+1]
##    print(bf)
    skbf=dot(bf, ibf)
    skba=dot(ba, iba)
    skjf=dot(jf, ijf)
    skja=dot(ja, ija)
##    print(skbf)
    f=interpol(skbf, skjf, ibf[:,:,0])
    a=interpol(skba, skja, ibf[:,:,0])
    vegso=interpol(f,a, ibf[:,:,1])
    return np.clip((vegso+0.5)*256, 0, 255)
##    print(np.min(vegso), np.max(vegso))

if __name__=="__main__":
    kepsize=800
    nyilszájz=6

    p=perlin(kepsize, nyilszájz)
    Image.fromarray(p).show()
