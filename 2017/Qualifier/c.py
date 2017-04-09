from lcj import*
with openw() as g:
 def f(n,o):
  n,o=int(n),int(o)
  for i in basea(o,2)[:0:-1]:n=n//2-(i&(n+1)%2)
  return'%i %i'%(n//2,(n-1)//2)
 for l in lines('C'):case(g,f(*l.split(' ')))