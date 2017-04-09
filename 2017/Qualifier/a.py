from lcj import*
with openw() as g:
 def f(s,n):
  s,n,o=[*s],int(n),0
  while'-'in s:
   o,i=o+1,s.index('-')
   if i>len(s)-n:break
   s[i:i+n]=map(lambda x:'-+'[x=='-'],s[i:i+n])
  return'IMPOSSIBLE'if'-'in s else o
 for l in lines('A'):case(g,f(*l.split(' ')))