# coding = utf-8

#print('\n'.join([' '.join(['%s*%s=%-2s'%(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

#print(' '.join('%s*%s=%s'%(x,y,x*y) for x in range(1,10) for y in range(1,10)))

L = []
for x in range(1,10):
    for y in range(1,x+1):
        L.append('%s*%s=%-2s'%(y,x,x*y))

    L.append('\n')

print(' '.join(L))
