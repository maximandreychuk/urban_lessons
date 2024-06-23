import datetime

s = datetime.date.today().strftime("%B %d, %Y")
r = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
t = datetime.datetime.now()
print(s)
print(r)
print(t)
