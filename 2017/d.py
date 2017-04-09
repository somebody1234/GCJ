from lcj import*
with openw() as g:
 m=0
 def f(m):
  r=[]
  #while 1:
  s='\n'.join(list(map(''.join,m)))
  print(s)
  return ['%i %i'%(2+s.count('+')+s.count('x'),len(r))]+r
 l=lines('D')
 while l:
  a=l[0].split(' ')
  n,m=int(a[0]),int(a[1])
  m=[[' ']*n]*n
  for o in l[1:m+1]:
   p=o.split(' ')
   m[int(p[1])-1][int(p[2])-1]=p[0]
  case(g,f(m))