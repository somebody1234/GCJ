# Harness the power of repunits

N = 32
J = 500

count = 0

with open("C.out", "w") as outfile:
    print("Case #1:", file=outfile)

    for i in range(2, N//2 - 2 + 1):
        s = "1"*i
        l = N - 2*i - 2

        L = [""]
        S = set()

        while L:
            x = L.pop()

            if len(x) > l:
                continue

            if len(x) == l:
                t = s+"0"+x+"0"+s

                if t in S:
                    continue

                S.add(t)
                
                print(t, *[int(s,i) for i in range(2, 11)], file=outfile)
                count += 1

                if count == J:
                    1/0
                continue

            L.append(x+"0")
            L.append(x+"0"[x[-1:]!="1":]+s)
