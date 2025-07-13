def Sequnuce_Sum(n):
    sum = 0
    res = []

    def num_gen():
        for i in range(1, n + 1):
            yield i**2

    for num in num_gen():
        res += [num]

    for i in res:
        sum += i

    print(f"res : {res}, and sum = {sum}")


Sequnuce_Sum(5)
