a0 = 1
r = 2
loop = [a0]
sum = a0
item = a0
n_f = 6
n = 2
while item in loop:
    # sum += item
    item = item * r
    loop += [item]
    sum += item
    n += 1
    if n > n_f:
        break
print(f"loop = {loop}, and sum = {sum}")
