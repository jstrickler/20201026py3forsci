
actor = "Chris Hemsworth"

city = "Hollywood"


print(actor, "lives in", city)
s = f"{actor} lives in {city}"
print(s)

v1 = 12.456
v2 = 3.930
v3 = 89.390239023239023

print(v1, v2, v3)
print(v1, v2, v3, sep=':')
print(v1, v2, v3, sep='==>')

print(v1, end="!")
print(v2, end="!")
print(v3)


# while printing out search results
# print(file_name, end=' ')
# print(result1, end=' ')
# print(result2, end=' ')
# print

#  print(a, b, c, sep=' ', end='\n')

print(v1, v2, v3)

print(actor, "lives in", city)
print("{} lives in {}".format(actor, city))
print(f"{actor} lives in {city}")
print("2 + 2 is {}".format(2 + 2))
print(f"2 + 2 is {2 + 2}")

print(f"{v1:.2f} {v2:.2f} {v3:.2f}")
print("{:.2f} {:.2f} {:.2f}".format(v1, v2, v3))

i1 = 12
i2 = 8032
i3 = 699

print(f"{i1:4d}|{i2:4d}|{i3:4d}")
print(f"{i1:04d}|{i2:04d}|{i3:04d}")

big_num = 38509283502983502983520938520983502983502983502850
print(f"{big_num:,d}")
