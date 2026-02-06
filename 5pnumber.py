import os
import time
import math

order = 2**20#計算数
allstart = time.time()
lastprint = time.time()

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

def tasktime(sumn,last):
    par = sumn*1000//last
    par = par/10
    strpar = str(par)
    while len(strpar) < 5:
        strpar = "0" + strpar
    timex = (time.time() - allstart)/(sumn/last)//1-(time.time() - allstart)//1

    if timex <= 0:
        return "100.0% 00s"

    return "Done: "+strpar+"%" + "   Tasktime: " + timestr(timex)

def add_next_prime_fast(filename="p.txt"):
    primes = []

    if os.path.exists(filename):
        with open(filename, "r") as f:
            for x in f.read().split():
                primes.append(int(x))

    if not primes:
        next_prime = 2
    else:
        last = primes[-1]
        candidate = last + 2 if last % 2 == 1 else last + 1

        while True:
            limit = math.isqrt(candidate)
            is_prime = True

            for p in primes:
                if p > limit:
                    break
                if candidate % p == 0:
                    is_prime = False
                    break

            if is_prime:
                next_prime = candidate
                break

            candidate += 2

    with open(filename, "a") as f:
        f.write(f"{next_prime}\n")

    return next_prime, len(primes) + 1

for i in range(order):
    start = time.time()
    new_p, count = add_next_prime_fast("p.txt")
    if lastprint+1 < time.time():
        print(f"No.{count}   Added: {new_p}","  Time:",timestr(time.time()-start)," ",tasktime(i+1,order))
        lastprint = time.time()

print(time.time()-allstart)