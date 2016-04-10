f=open('IO/B-large.in')
l=f.readlines()[1:]
f.close()
a=1
g=open('IO/out','w+')
def f(s):
 i=0;p=s[0]
 for c in s[1:]:
  if p!=c:i+=1
  p=c
 if s[-1]=='-':i+=1
 g.write('Case #'+str(a)+': '+str(i)+'\n')
for n in l:
 f(n[:-1]);a+=1
g.close()