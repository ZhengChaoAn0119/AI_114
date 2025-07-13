sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + i
print(f"使用for迴圈, sum = {sum}")

sum = 0  # 設定變數初始值
i = 1  # 設定變數條件初始值
while i in range(1, 11):  # 設定判斷條件迴圈
    sum += i  # sum = sum + i #變數更動
    i += 1  # i = i + 1 #條件變數更動
print(f"使用while迴圈, sum = {sum}")

sum = 0
i = 1
while True:
    sum += i
    i += 1
    if i > 10:
        break
print(f"使用while True迴圈, sum = {sum}")

sum = 0
i = 1
while i in range(1, 11):
    sum += i
    i += 1
print(sum)
