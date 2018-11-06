import re

mileage = input("What mileage ? ")

try:
    file = open("theta", "r")
except:
    print("No theta file.")
    exit(0)

pattern = re.compile("([0-9.\-]+),([0-9.\-]+)")
line = file.readline()
match = re.match(pattern, line)

try:
    theta0 = match.group(1)
    theta1 = match.group(2)
except:
    print("Bad theta.")
    exit(0)

estimatePrice = float(theta0) + (float(theta1) * int(mileage))

print("The estimated price is : " + str(estimatePrice))
