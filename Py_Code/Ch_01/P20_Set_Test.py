s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8, 9}

print(f"s1 & s2 : {s1 & s2}")  # {4,5}
print(f"s1 | s2 : {s1 | s2}")  # {1,2,3,4,5,6,7,8,9}
print(f"s1 - s2 : {s1 - s2}")  # {1,2,3}
print(f"s1 ^ s2 : {s1 ^ s2}")  # {1,2,3,6,7,8,9}

print(f"1 in s1? : {1 in s1}")  # Ture
print(f"10 in s1? : {10 in s1}")  # False

s3 = set("Wison have nice day.")
print(s3)
print(f"n in s3 :{'n' in s3}")  # Ture
