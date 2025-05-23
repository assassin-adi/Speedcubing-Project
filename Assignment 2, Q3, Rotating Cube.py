from vpython import *

c = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.red)

while True:
    rate(100)
    c.rotate(angle=0.01, axis=vector(0,1,0), origin=vector(0,1,0))

