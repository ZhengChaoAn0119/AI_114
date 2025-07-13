import random

roll = range(6)
for r in roll:
    print(random.randint(1, 10), end=", ")  # 1-10擲骰 包含1-10
print()
for r in roll:
    print(random.randrange(1, 10), end=", ")  # (start, stop, step) 不包含stop
print()
for r in roll:
    print(random.random(), end=", ")  # 0.0-1.0 包含0 不包含1
print()
for r in roll:
    print(random.uniform(1, 10), end=", ")  # 回傳float 包含兩邊
print()
