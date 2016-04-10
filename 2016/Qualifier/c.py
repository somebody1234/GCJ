f=open('IO/C-large.in')
l=f.readlines()[1:][0].split(' ')
f.close()
g=open('IO/out','w+')
def z(n):
 if n%2==0:return 2
 r=1
 while r<n**.5:
  r+=2
  if r>10000:return 0
  if n%r==0:return r#check
 return 0
def t(n):
 s=''
 while n:
  s=str(n%2)+s
  n/=2
 return s
def f(x):
 while 1:
  f=1
  s=t(x)
  d=s+' '
  for i in range(9):
   v=z(int(s,i+2))
   if v==0:
    x+=2
    f=0
    break
   d+=str(v)+' '
  if f==0:continue
  g.write(d+'\n')
  return x+2
r=1+(1<<(int(l[0])-1))
g.write('Case #1:\n')
for y in range(int(l[1])):
 r=f(r)
g.close()