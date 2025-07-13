import numpy as np

total = 0.0
avg = 0.0

degrees = np.array([27, 28, 29, 30, 31, 32, 33])

for deg in degrees:
    total += deg

avg = total / len(degrees)

print(f"degrees = {degrees}, avg = {avg}")


scorse = np.array([5, 7, 3, 8, 9, 1])
print(scorse)


# for i in range(len(scorse)-2,-1,-1):
#     for j in range(0,i+1):
#         if scorse[j] > scorse[j+1]:
#             tmp = scorse[j]
#             scorse[j] = scorse[j+1]
#             scorse[j+1] = tmp

# for i in range(0,len(scorse)+1):
#     if scorse[i] > scorse[i+1]:
#         tmp = scorse[i]
#         scorse[i] = scorse[i+1]
#         scorse[i+1] = tmp
# for j in range(scorse[-1],0,-1):
#     if scorse[j] < scorse[j-1]:
#         tmp = scorse[j]
#         scorse[j] = scorse[j-1]
#         scorse[j-1] = tmp

# print(scorse)


scorse.sort()
print(f"after scorse : {scorse}")
print(f"reverse scorst : {scorse[::-1]}")
