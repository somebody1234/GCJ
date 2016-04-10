from lcj import *
l=inta(lines('C')[0].split())
with openw() as g:
 def f(x):
  while 1:
   f=1;s=bins(x);d=s+' '
   for i in range(9):
    v=trialFactor(int(s,i+2),1e4)
    if v==0:x+=2;f=0;break
    d+=str(v)+' '
   if f:
    g.write(d+'\n')
    return x+2
 r=1+(1<<(l[0]-1))
 case(g)
 for y in range(l[1]):
  r=f(r)