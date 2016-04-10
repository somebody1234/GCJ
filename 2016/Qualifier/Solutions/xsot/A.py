for t in range(1, int(raw_input())+1):
    n = int(raw_input())
    seen = 0
    
    if n == 0:
        print "Case #%d: INSOMNIA" % t
        continue
        
    m = 0
    while seen != (1<<10)-1:
        m += n
        temp = m
        while temp:
            seen |= 1<<temp%10
            temp /= 10
        
    print "Case #%d: %d" % (t, m)