n=299

for i in range(2, int(n/2)+1):
    pow = int(n/i)
    last = 1
    result = 1
    if n%i == 1: 
        last = i + 1
        result = i ** (pow - 1) * last
        print(str(i)+'^'+str(pow-1)+'*'+str(last)+' '+str(result))
    else:
        last = (1 if n%i == 0 else n%i)
        result = i ** pow * last
        print(str(i)+'^'+str(pow)+'*'+str(last)+' '+str(result))