import re


data = [1, 2, 3, 4, 5]
for i in data:
    print(i, ", ", end="")
print()

i = iter(data)
while True:
    try:
        print(next(i), ", ", end="")
    except StopIteration:
        print("NO more elemaent")
        break
print()


def read_line():
    return input("Enter a line: ")


i = iter(read_line, "quit")
str_buff = ""
for line in i:
    str_buff += line + " "
print("You enterde: ", str_buff)

# --------------------------------------------------
# re exam
# --------------------------------------------------
print(r"\n")
text = "hello, heo, heabo, heaaaao, hello125, hello3"
print(re.findall(r"he..o", text))  # "hello","heabo" . any key
print(re.findall(r"he[a-d][abc]o", text))  # "heabo"
print(re.findall(r"hea+o", text))  # "heaaaao" + 1個/1個以上
print(re.findall(r"hea*o", text))  # "heo" "heaaaao" * 任何數量
print("------------------------------------")
print(re.findall(r"hello\d\d\d", text))  # 任何數字 "hello125"
print(re.findall(r"hello\d{3}", text))
print(re.findall(r"hello\d{1,3}", text))  # 任何{1-3}個數字 "hello125" "hello3"
print(re.findall(r"hello\d{1,}", text))  # 任何{1,}個以上的數字
print("------------------------------------")
print(re.findall(r"he[a-z]{,2}o", text))  # "hello" "heo" "heabo" "hello" "hello"
