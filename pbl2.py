x = int(input())
digits = list(map(int, input().split()))
count = {}
ans = 0
for digit in digits:
    if digit in count:
         count[digit] += 1
    else:
        count[digit] = 1
for key, value in count.items():
    if key <= value:
        ans += (value - key)
    else:
        ans += value
print(ans)