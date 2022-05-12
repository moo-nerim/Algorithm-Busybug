# BOJ 1049
# 기타줄

n, m = map(int, input().split())
brandL = []

for _ in range(m):
    pack, single = map(int, input().split())
    if n < 6:
        brandL.append((pack, single * n))
    else:
        brandL.append((pack, single))  # 패키지만 구입, 패키지 + 낱개, 낱개 여러개
if n < 6:
    print(min(map(min, brandL)))
else:
    pack_sort = sorted(brandL, key=lambda x: x[0])
    single_sort = sorted(brandL, key=lambda x: x[1])
    onlyPack = pack_sort[0][0] * (n // 6 + 1)
    onlySingle = single_sort[0][1] * n
    packPlusSingle = pack_sort[0][0] * (n // 6) + single_sort[0][1] * (n % 6)
    print(min(onlyPack, onlySingle, packPlusSingle))
