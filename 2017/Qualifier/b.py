from lcj import*
with openw() as g:
 def f(n):
  while 1:
   s=[*str(n)]
   for i in range(len(s)-1):
    if s[-i-1]<s[-i-2]:s=s[:-i-2]+[str(int(s[-i-2])-1)]+['9']*(i+1)
   while s[0]=='0':s=s[1:]
   return''.join(s)
 for l in lines('B'):case(g,f(int(l)))