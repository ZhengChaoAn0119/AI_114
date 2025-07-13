x = 10.0
y = 20.0

z = x + y

print("x=%d,y=%d,z=%d" % (x, y, z))
z = x - y
print(f"x={x},y={y},z={z}")
z = x * y
print("x={:.2f},y={:.2f},z={:.3f}".format(x, y, z))
z = x / y
print(f"x={x},y={y},z={z}")

print("x=%a,y=%a,z=%a" % (x, y, z))
