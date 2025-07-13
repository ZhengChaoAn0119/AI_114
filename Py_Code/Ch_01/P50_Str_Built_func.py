strlist = ["Today", "is", "a", "nice", "day"]
print("*".join(strlist))

str_example = " ".join(strlist)
print(str_example)

print("----------------------------")
lst_1 = str_example.split()

str_example = "~!~".join(strlist)
lst_2 = str_example.split("!")

print(f"lst_1 : {lst_1}")
print(f"lst_2 : {lst_2}")

print("---------------------------")
str_example = "http://www.python.org"
print(str_example.startswith("http"))  # True
print(str_example.endswith("org"))  # True
