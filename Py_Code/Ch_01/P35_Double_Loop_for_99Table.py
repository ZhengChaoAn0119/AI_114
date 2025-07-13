"""
for a in range(2,10):
    for b in range(2,6):
        print(f"{b} * {a} = {a*b}",end= '\t') #end= 不換行繼續print
    print() #b range(2,6) b到5結束時 print後換行
print("----------------------------------------------------------------------")
for a in range(2,10):
    for b in range(6,10):
        print(f"{b} * {a} = {a*b}",end= '\t')
    print()
"""

a = 2
while a < 10:
    b = 2
    while b < 6:
        print(f"{b} * {a} = {a*b}", end="\t")  # end= 不換行繼續print
        b += 1
    print()  # b range(2,6) b到5結束時 print後換行
    a += 1
print("----------------------------------------------------------------------")
a = 2
while a < 10:
    b = 6
    while b < 10:
        print(f"{b} * {a} = {a*b}", end="\t")
        b += 1
    print()
    a += 1
