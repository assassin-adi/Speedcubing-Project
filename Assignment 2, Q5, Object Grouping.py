from vpython import *

s = 1
f = 0.95
d = 0.02
m=[]
for a in [1, 0, -1]:
    for b in [1, 0, -1]:
        for c in [1, 0, -1]:
            pos = vector(a, b, c)
            box(pos=pos, size=vector(s, s, s), color=vector(0.1, 0.1, 0.1))
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
for l in scene.objects:
    if abs(l.pos.x) == 0:
        m.append(l)

while True:
    rate(60)
    for l in m:
        l.rotate(angle=0.05, axis=vector(-1,0,0), origin=vector(0,0,0))
