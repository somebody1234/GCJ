def flip(s, k):
    return s[:k+1][::-1].replace('+','@').replace('-','+').replace('@','-')+s[k+1:]

for t in range(1, int(raw_input())+1):
    s = raw_input()
    moves = 0
    n = len(s)-1
    
    while s[n] == '+' and n >= 0:
        n -= 1
        
    while n >= 0:
        if s[0] == '+':
            m = n
            while s[m] != '+' and m > 0:
                m -= 1
            s = flip(s, m)
            moves += 1
        s = flip(s, n)
        moves += 1
        
        while s[n] == '+' and n >= 0:
            n -= 1
            
    print "Case #%d: %d" % (t, moves)
