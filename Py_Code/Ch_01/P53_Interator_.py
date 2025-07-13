data = [1, 2, 3, 4, 5]

i = iter(data)
print(next(i))  # 1
print(next(i))  # 2
print(next(i))  # 3
print(next(i))  # 4
print(next(i))  # 5

print(next(i))  #

# for i in data:
#     print(i, ", ", end="")
# print()

# i = iter(data)
# while True:
#     try:
#         print(next(i), ", ", end="")
#     except StopIteration:
#         print("NO more elemaent")
#         break
# print()


def read_line():
    return input("Enter a line (input 'quit' to stop): ")


# iter(callable, snetinel)
i = iter(
    read_line, "quit"
)  # iter(function, "quit") 重複呼叫function ,直到回傳的值等於"quit",才會停止
str_buff = ""
for line in i:
    str_buff += line + " "
print("You enterde: ", str_buff)


# 示意流程圖
# loop:
#     call read_line()
#     if result == "quit":
#         break
#     else:
#     yield result
