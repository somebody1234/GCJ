from lcj import *
with openw() as g:
 f=lambda k,c,s:case(g,*maxLen([revbasea(a,k)+1for a in chunk(range(k),c)],s,['IMPOSSIBLE']))
 for n in lines('D'):
  f(*inta(n.split()))