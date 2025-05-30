from vpython import *
#first i make the cube 
s = 19         
f = 18        
d = 0.02       
#I followed the size requirments

for a in [1, 0, -1]:
    for b in [1, 0, -1]:
        for c in [1, 0, -1]:
            pos = vector(a * 20, b * 20, c * 20)
            box(pos=pos, size=vector(s, s, s), color=color.white)
            if c == 1:
                box(pos=pos + vector(0, 0, s/2 + d/2), size=vector(f, f, d), color=color.white)
            if c == -1:
                box(pos=pos + vector(0, 0, -s/2 - d/2), size=vector(f, f, d), color=color.yellow)
            if a == -1:
                box(pos=pos + vector(-s/2 - d/2, 0, 0), size=vector(d, f, f), color=color.blue)
            if a == 1:
                box(pos=pos + vector(s/2 + d/2, 0, 0), size=vector(d, f, f), color=color.green)
            if b == 1:
                box(pos=pos + vector(0, s/2 + d/2, 0), size=vector(f, d, f), color=color.red)
            if b == -1:
                box(pos=pos + vector(0, -s/2 - d/2, 0), size=vector(f, d, f), color=color.orange)
#the cube with stickers as flat boxes is ready 
#now i will map keys to it, but before i will define functions of what to rotate and define if the cube is in rotation or not

rotation = False

def R():
    global rotation
    rotation = True
    for _ in range(90):
        for i in [j for j in scene.objects if round(j.pos.x) >= 20]:
            i.rotate(angle=radians(1), axis=vector(-1,0,0), origin=vector(20,0,0))
        rate(60)
    rotation = False

def L():
    global rotation
    rotation = True
    for _ in range(90):
        for i in [j for j in scene.objects if round(j.pos.x) <= -20]:
            i.rotate(angle=radians(1), axis=vector(1,0,0), origin=vector(-20,0,0))
        rate(60)
    rotation = False

def U():
    global rotation
    rotation = True
    for _ in range(90):
        for i in [j for j in scene.objects if round(j.pos.y) >= 20]:
            i.rotate(angle=radians(1), axis=vector(0,-1,0), origin=vector(0,20,0))
        rate(60)
    rotation = False

def D():
    global rotation
    rotation = True
    for _ in range(90):
        for i in [j for j in scene.objects if round(j.pos.y) <= -20]:
            i.rotate(angle=radians(1), axis=vector(0,1,0), origin=vector(0,-20,0))
        rate(60)
    rotation = False

def F():
    global rotation
    rotation = True
    for _ in range(90):
        for i in [j for j in scene.objects if round(j.pos.z) >= 20]:
            i.rotate(angle=radians(1), axis=vector(0,0,-1), origin=vector(0,0,20))
        rate(60)
    rotation = False

def B():
    global rotation
    rotation = True
    for _ in range(90):
        for i in [j for j in scene.objects if round(j.pos.z) <= -20]:
            i.rotate(angle=radians(1), axis=vector(0,0,1), origin=vector(0,0,-20))
        rate(60)
    rotation = False
#mapping the keys
def key(evt):
    global rotation
    if rotation:
        return
    a = evt.key
    if a.lower() == 'k':
        R()
    elif a.lower() == 'd':
        L()
    elif a.lower() == 'j':
        U()
    elif a.lower() == 's':
        D()
    elif a.lower() == 'h':
        F()
    elif a.lower() == 'w':
        B()

scene.bind('keydown', key)
#my logic behind the roations was, that if i am asked to rotate the right side clockwise,
#I will just see that my right face has all the boxes at rounded x=20 and the stickers at rounded x=20+delta where delta is a small number,
#and then i will rotate all those items at x>=20 which would include the main cubes and all the stickers, and i expaned this logic to all the faces
#I then selected the axis and vertex to each rotation to match the actual cube notations so that all faces are roatted aclockwise when looked directly at from the front
