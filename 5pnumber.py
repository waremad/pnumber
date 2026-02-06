import os
import time

order = 10**5#計算数
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

def add_next_prime(filename="p.txt"):
    """
    p.txtから素数を読み込み、最後の素数より大きい次の素数を1つ計算して追記する関数
    """
    primes = []
    
    # 1. ファイルから既存の素数を読み込む
    if os.path.exists(filename):
        with open(filename, "r") as f:
            # 改行やスペース区切りに対応して読み込む
            raw_data = f.read().split()
            for item in raw_data:
                if item.strip().isdigit():
                    primes.append(int(item))
    
    # 2. 次の素数を探索する
    if not primes:
        next_prime = 2
    else:
        last_prime = primes[-1]
        candidate = last_prime + 1
        # 偶数なら奇数へ
        if candidate % 2 == 0:
            candidate += 1
            
        while True:
            is_prime = True
            limit = int(candidate**0.5)
            
            # 既存の素数リストを使って割り算判定
            for p in primes:
                if p > limit:
                    break
                if candidate % p == 0:
                    is_prime = False
                    break
            
            # 素数リストが足りない場合（limitまで到達していない場合）の予備判定
            # (p.txtが連続した素数リストなら通常ここは実行されませんが、念のため)
            if is_prime and (not primes or primes[-1] < limit):
                start_div = 3
                if primes:
                    start_div = primes[-1] + 2
                    if start_div % 2 == 0:
                        start_div += 1
                
                for d in range(start_div, limit + 1, 2):
                    if candidate % d == 0:
                        is_prime = False
                        break
            
            if is_prime:
                next_prime = candidate
                break
            
            candidate += 2

    # 3. ファイルに追記する
    try:
        with open(filename, "a") as f:
            f.write(f"{next_prime}\n")
    except PermissionError:
        print(f"\n[Error] '{filename}' への書き込み権限がありません。")
        print(f"ヒント: ターミナルで 'sudo chown $USER:$USER {filename}' を実行して権限を修正してください。")
        raise
        
    return next_prime, len(primes) + 1

for i in range(order):
    start = time.time()
    new_p, count = add_next_prime("p.txt")
    if lastprint+1 < time.time():
        print(f"No.{count}   Added: {new_p}","  Time:",timestr(time.time()-start)," ",tasktime(i+1,order))
        lastprint = time.time()

print(time.time()-allstart)