for t in range(1, int(raw_input())+1):
    k, c, s = map(int, raw_input().split())
    print "Case #%d: " % t + " ".join(map(str, range(1, k+1)))