import time

ls = []
n = 2
order = 2**29#計算上限数
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

def pture(n):
    n = int(n)
    if n < 2:
        return []
    
    pls = pture(int(n**0.5))

    # 0と1は素数ではないので "x"、2以降を "o" で初期化
    tls = ["x", "x"] + ["o"] * (n - 1)
    
    for i in pls:
        # i自身(1*i)を消さないように j=1 (つまり2*i) から開始
        for j in range(1, n//i):
            tls[(j+1)*i] = "x"
    
    outls = []
    for i in range(n+1):
        if tls[i] == "o":
            outls.append(i)

    return outls
    

pnum = pture(order)

print(pnum[-1]," ",timestr(time.time()-start))