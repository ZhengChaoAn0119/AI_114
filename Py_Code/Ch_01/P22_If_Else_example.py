while True:
    age = input("aldult? y/n")
    if age == "y":
        break
    if age == "n":
        break
    print("請重新輸入")

aldult = True if age == "y" else False

if aldult == True:
    print("開始瑟瑟!")
else:
    print("闢孩滾!!!!")
