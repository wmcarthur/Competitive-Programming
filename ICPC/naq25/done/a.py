r, g, b = map(int, input().split())
cr, cg, cb = map(int, input().split())
crg, cgb = map(int, input().split())

rn = max(0, r-cr)
gn = max(0, g-cg)
bn = max(0, b-cb)

total = 0
ga = 0
if crg < rn or cgb < bn or gn > crg -rn + cgb -bn:
    print(-1)
else:
    if rn <= crg:
        total += rn
        ga += crg-rn
    if bn <= cgb:
        total += bn
        ga += cgb-bn
    if gn > 0 and ga >= gn:
        total += gn
    print(total)
        
    
