from vpython import *

v = vector(0, 0, 0) 
s = 2 
d = 0.02

box(pos=v,size=vector(s,s,s, color=color.grey))

box(pos=v + vector(0, 0, s/2 + 0.01), size=vector(s, s, d), color=color.white)
box(pos=v + vector(0, 0, -s/2 - 0.01), size=vector(s, s, d), color=color.yellow)
box(pos=v + vector(s/2 + 0.01, 0, 0), size=vector(d, s, s), color=color.green)
box(pos=v + vector(-s/2 - 0.01, 0, 0), size=vector(d, s, s), color=color.blue)
box(pos=v + vector(0, s/2 + 0.01, 0), size=vector(s, d, s), color=color.red)
box(pos=v + vector(0, -s/2 - 0.01, 0), size=vector(s, d, s), color=color.orange)
