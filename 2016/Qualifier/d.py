f=open('IO/D-large.in')
l=f.readlines()[1:]
f.close()
a=1
g=open('IO/out','w+')
def f(h):
 [k,c,s]=[int(t)for t in h];d='';l=0
 for i in range(k):
  l=l*k+i
  if i>0and i%c==0:
   d+=str(l+1)+' '
   l=0
 d+=str(l+1)
 g.write('Case #'+str(a)+': '+(d if len(d.split(' '))<=s else 'IMPOSSIBLE')+'\n')
for n in l:
 f(n[:-1].split(' '));a+=1
g.close()