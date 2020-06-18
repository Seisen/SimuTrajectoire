import Player
from math import *


class var:
    gravite=0
    just_touched=True

   

def set_gravite(nmb):
    try:
        nmb=float(nmb)
        var.gravite=nmb
        
    except ValueError:
        pass


def impulseX(joueur,x):
    try:
        float(x)
        joueur.vecX+=x
    except ValueError:
        pass

def impulseXY(joueur,x,y):
    try:
        float(x)
        float(y)
        joueur.vecX+=x
        joueur.vecY+=y
    except ValueError:
        pass

def impulseY(joueur,y):
    try:
        float(y)
        joueur.vecY+=y
    except ValueError:
        pass
 

def getDistance(obj1,obj2):
    return sqrt(((obj1.x-obj2.x)*(obj1.x-obj2.x))+((obj1.y-obj2.y)*(obj1.y-obj2.y)))

def getDistance2Points(x1,y1,x2,y2):
    return sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))

def getVecXY(x1,y1,x2,y2):
    Fx=0
    Fy=0

    dx=abs(x1-x2)
    dy=abs(y1-y2)

    total_d=dx+dy

    dx=(100*dx)/total_d
    dy=(100*dy)/total_d

    if x1-x2>0:
        dx=dx-(2*dx)
    if y1-y2>0:
        dy=dy-(2*dy)

    force = getDistance2Points(x1,y1,x2,y2)/40

    Fx=(force*dx)/100
    Fy=(force*dy)/100

    return Fx,Fy

def setForceXY(obj1,obj2):
    
    Fx=0
    Fy=0

    dx=abs(obj1.x-obj2.x)
    dy=abs(obj1.y-obj2.y)

    total_d=dx+dy

    dx=(100*dx)/total_d
    dy=(100*dy)/total_d

    if obj1.x-obj2.x<0:
        dx=dx-(2*dx)
    if obj1.y-obj2.y<0:
        dy=dy-(2*dy)

    force = setForce(obj1,obj2)

    Fx=(force*dx)/100
    Fy=(force*dy)/100

    return Fx,Fy

def setForce(obj1,obj2):
    distance=getDistance(obj1,obj2)
    return ((var.gravite*obj2.masse*1000)/(distance*distance))

def appliqueForceXY(j,attracteur):

    Fx,Fy=setForceXY(j,attracteur)

    j.vecX-=Fx
    j.vecY-=Fy
  
def appliqueVec(j):
    j.x+=j.vecX
    j.y+=j.vecY

def appliqueFriction(obj):
    obj.vecX*=1-obj.friction
    obj.vecY*=1-obj.friction

def test_collision(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if j!=i:
                pass# a finir


def add_traine(obj):

    if len(obj.traine)<obj.traine[0]:

        obj.traine+=[(int(obj.x),int(obj.y))]
       

    else:
        
        for i in range(len(obj.traine)-1,1,-1):
            
            obj.traine[i]=obj.traine[i-1]

        obj.traine[1]=(int(obj.x),int(obj.y))

def test_traine(obj):
    return obj.traine[0]>0

def test_liste_traine(liste):
    for i in range(len(liste)):
        if test_traine(liste[i]):
            add_traine(liste[i])

