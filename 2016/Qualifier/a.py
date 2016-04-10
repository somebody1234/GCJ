f=open('IO/A-large.in')
l=f.readlines()[1:]
f.close()
a=1
g=open('IO/out','w+')
def f(n):
 s=set();i=0
 if n>0:
  while len(s)<10:
   i+=1
   for d in str(n*i):s.add(int(d))
 g.write('Case #'+str(a)+': '+('INSOMNIA'if n==0else str(n*i))+'\n')
for n in l:
 f(int(n[:-1]));a+=1
g.close()