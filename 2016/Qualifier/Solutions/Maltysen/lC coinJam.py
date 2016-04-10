from itertools import product

N = 32
J = 500

print("Case #1:")

for i in product("01", repeat=N-2):
    s = "1"+"".join(i)+"1"
    Y = []
    for j in range(2, 11):
        n = int(s, j)
        for k in range(2, int(min(n ** .5, 1e4))):
            if n % k == 0:
                Y.append(k)
                break
        else:
            break
    else:
        print(s + " " + " ".join(map(str, Y)))
        J -= 1

        if not J:
            break
