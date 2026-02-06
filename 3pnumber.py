import time

ls = []
n = 2
order = 2**28#計算上限数
start = time.time()

def timestr(t):
    s = t%60

    m = t//60
    h = m//60
    m = m%60

    d = h//24
    h = h%24

    M = d//30
    d = d%30

    Y = M//12
    M = M%12

    numls = [Y,M,d,h,m,s]
    strls = ["Y","M","D","h","m","s"]
    outstr = ""

    n = 0
    while numls[n] == 0:
        n += 1
    for i in range(n,len(numls)):
        twostr = str(int(numls[i]))
        while len(twostr) < 2:
            twostr = "0" + twostr
        outstr += twostr + strls[i]
    return outstr

def sieve(n):
    if n < 2:
        return []

    size = (n - 1) // 2
    is_prime = bytearray(b"\x01") * size

    for i in range(int(n**0.5)//2 + 1):
        if is_prime[i]:
            p = 2*i + 3
            start = (p*p - 3)//2
            is_prime[start::p] = b"\x00" * ((size-start-1)//p + 1)

    return [2] + [2*i+3 for i,v in enumerate(is_prime) if v]

pnum = sieve(order)

print(pnum[-1]," ",timestr(time.time()-start))