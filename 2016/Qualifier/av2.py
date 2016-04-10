from lcj import *
with openw() as g:
 def f(n,s=set(),i=0):
  if n>0:
   while len(s)<10:
    s|=set(*deca(n*i))
  case(g,'INSOMNIA'if n==0else str(n*i))
 for n in inta(lines('A')):
  f(n)