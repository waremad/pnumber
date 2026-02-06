import time

ls = []
n = 2
order = 2**10#計算上限数
last = order*(order+1)//2 - 1
sumn = 0
start = time.time()
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

def tasktime():
    par = sumn*1000//last
    par = par/10
    strpar = str(par)
    while len(strpar) < 5:
        strpar = "0" + strpar
    timex = (time.time() - start)/(sumn/last)//1-(time.time() - start)//1

    if timex <= 0:
        return "100.0% 00s"

    return strpar+"%" + " " + timestr(timex)

def pture(n):
    n = int(n//1)
    if n < 3:
        return [2]
    
    pls = pture(n**0.5//1)

    ls = [0]
    tls = ["x"]
    for i in range(n):
        ls.append(i+1)
        tls.append("o")
    
    for i in pls:
        for j in range(n//i):
            tls[(j+1)*i] = "x"
    
    outls = []
    for i in range(n+1):
        if tls[i] == "o":
            outls.append(i)
    return outls
    

pnum = pture(order)

print(pnum[-1]," ",timestr(time.time()-start))