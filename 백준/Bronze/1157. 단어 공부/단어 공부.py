w = input().upper()

cnt = {}
for char in w:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1

max_val = max(cnt.values())

lst = [k for k, v in cnt.items() if v == max_val]

print('?' if len(lst) > 1 else lst[0])