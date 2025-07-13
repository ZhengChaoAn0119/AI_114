for i in range(9):
    if 3 < i < 5:
        continue
    if i == 8:
        print("")
        break
    print(i, end=" ")

print("End!")
