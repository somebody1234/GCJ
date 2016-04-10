t = int(input())
for i in range(1, t + 1):
  n = int(input())
  if n == 0:
    out = "INSOMNIA";
  else:
    letters = ""
    p = 0
    while not all(c in letters for c in "0123456789"):
      p += n #pending attempt
      for q in str(p):
        if not q in letters:
          letters += q
        else:
          pass
    out = p
      
  print("Case #{}: {}".format(i, out))