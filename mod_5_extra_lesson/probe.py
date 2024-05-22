import time
duration = 90
i = 0
while i != duration:
    print(i)
    time.sleep(4)
    i += 4
duration = i
print(duration)
