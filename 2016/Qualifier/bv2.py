from lcj import *
with openw() as g:
 for s in lines('B'):
  t=dedup(s)
  case(g,len(t)-(t[-1]=='+'))