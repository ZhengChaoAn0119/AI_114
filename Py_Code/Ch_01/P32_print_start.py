# def start(n):
#     def start1():
#         for row in range(n):
#             for col in range(n):
#                 if col <= row:
#                     print("*",end='')
#                 else:
#                     print('')
#                     break

#     def start2():
#         for row in range(n):
#             for col in range(n):
#                 if col <= (n-2)-row:
#                     print(" ",end='')
#                 else:
#                     print('*',end='')
#             print()

#     def start3():
#         for row in range(n):
#             for col in range(n):
#                 if col <= row-1:
#                     print(" ",end='')
#                 else:
#                     print('*',end='')
#             print()

#     def start4():
#         for row in range(n):
#             for col in range(n):
#                 if col <= (n-1)-row:
#                     print("*",end='')
#                 else:
#                     print(' ',end='')
#             print()
#     print(start2(),start1())
#     print(start3(),start4())

# start(5)
# def start(n):
#     col = 0
#     n = n

#     while True:
#         print("*",end='')
#         col += 1
#         if col >= n:
#             print()
#             col = 0
#             n -= 1
#         if n == 0:
#             break


# start(5)


def print_filled_diamond(n):
    for y in range(-n, n + 1):  # y 從上到下
        for x in range(-n, n + 1):  # x 從左到右
            if abs(x) + abs(y) <= n:
                print("*", end="")  # 在菱形內部：填入 *
            else:
                print(" ", end="")  # 菱形外部：填空格
        print()  # 換行


def print_diamond(n):
    y = -n
    while y < n + 1:
        x = -n
        while x < n + 1:
            if abs(x) + abs(y) <= n:
                print("*", end="")
            else:
                print(" ", end="")
            x += 1
        print()
        y += 1


print_diamond(3)
