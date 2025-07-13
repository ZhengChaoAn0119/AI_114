strEx = "python"
print(strEx.ljust(12))
print(strEx.ljust(12, "$"))

print(strEx.rjust(12, "$"))

print(strEx.center(12, "$"))

strEx = "        python is fun       "
print(strEx.lstrip())
print(strEx.rstrip())
print(strEx.strip())
print("------------------------------")
print(strEx.find("n"))
print(strEx.rfind("n"))

print(strEx.count("n"))
print("-----------------------------")
print(strEx.replace("n", "&"))  # "pytho& is fu&"
print(strEx.replace("n", "&", 1))  # "pytho& is fun"
print(strEx.replace("n", ""))  # "pytho is fu "
