H = int(input())

plant = 0
day = 0
while True:
    plant += 2 ** day
    day += 1
    if plant > H:
        break

print(day)
