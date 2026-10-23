#(ABCD*2=DCBA)
import itertools

digits = range(10)

for p in itertools.permutations(digits, 4):
    a, b, c, d = p

    if a == 0 or d == 0:
        continue

    abcd = a*1000 + b*100 + c*10 + d
    dcba = d*1000 + c*100 + b*10 + a

    if abcd * 4 == dcba:
        print("solution found")
        print(f"A={a},B={b},C={c},D={d}")
        print(abcd, "*" ,"4","=", dcba)
        break
else:
    print("no solution found")




#ab+cd=ef
import itertools

for p in itertools.permutations(range(10), 6):
    a, b, c, d, e, f = p

    if a == 0 or c == 0 or e == 0:
        continue

    ab = a * 10 + b
    cd = c * 10 + d
    ef = e * 10 + f

    if ab + cd == ef:
        print("solution found")
        print(f"A={a},B={b},C={c},D={d},E={e},F={f}")
        print(ab, "+", cd, "=", ef)
        break
else:
    print("no solution found")
