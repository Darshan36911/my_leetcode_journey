from functools import lru_cache

CONTRIB = {1:(0,0,0,0),2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),5:(0,0,1,0),
           6:(1,1,0,0),7:(0,0,0,1),8:(3,0,0,0),9:(0,2,0,0)}

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        x = t
        t2 = t3 = t5 = t7 = 0
        while x % 2 == 0: x //= 2; t2 += 1
        while x % 3 == 0: x //= 3; t3 += 1
        while x % 5 == 0: x //= 5; t5 += 1
        while x % 7 == 0: x //= 7; t7 += 1
        if x != 1:
            return "-1"

        @lru_cache(None)
        def f(a, b):
            if a <= 0 and b <= 0: return 0
            a = max(a, 0); b = max(b, 0)
            best = (a + 2)//3 + (b + 1)//2
            for c in range(1, min(a, b) + 1):
                best = min(best, c + (a - c + 2)//3 + (b - c + 1)//2)
            return best

        def feasible(need, r):
            a, b, c5, c7 = need
            return r >= max(c5,0) + max(c7,0) + f(max(a,0), max(b,0))

        def build(need, r):
            a, b, c5, c7 = need
            res = []
            for pos in range(r):
                for d in range(1, 10):
                    na, nb, nc5, nc7 = CONTRIB[d]
                    new = (a-na, b-nb, c5-nc5, c7-nc7)
                    if feasible(new, r-pos-1):
                        res.append(str(d))
                        a, b, c5, c7 = new
                        break
            return ''.join(res)

        n = len(num)
        if '0' not in num:
            p = 1
            for ch in num: p *= int(ch)
            if p % t == 0:
                return num

        ps2=[0]*(n+1); ps3=[0]*(n+1); ps5=[0]*(n+1); ps7=[0]*(n+1)
        zero_before=[False]*(n+1)
        for i, ch in enumerate(num):
            d = int(ch)
            c2,c3,c5,c7 = CONTRIB.get(d, (0,0,0,0))
            ps2[i+1]=ps2[i]+c2; ps3[i+1]=ps3[i]+c3
            ps5[i+1]=ps5[i]+c5; ps7[i+1]=ps7[i]+c7
            zero_before[i+1] = zero_before[i] or (ch == '0')

        for i in range(n-1, -1, -1):
            if zero_before[i]:
                continue
            for d in range(int(num[i])+1, 10):
                c2,c3,c5,c7 = CONTRIB[d]
                need = (t2-ps2[i]-c2, t3-ps3[i]-c3, t5-ps5[i]-c5, t7-ps7[i]-c7)
                r = n-1-i
                if feasible(need, r):
                    return num[:i] + str(d) + build(need, r)

        m = max(n+1, t5+t7+f(t2,t3))
        return build((t2,t3,t5,t7), m)