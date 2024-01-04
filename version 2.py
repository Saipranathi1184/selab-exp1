T=float(input("Enter value of temperature:"))
H=float(input("Enter value of humidity:"))
w=float(input("Enter value of wind speed:"))
W=(0.5)*(T**2)-(0.2)*H+(0.1)*w-15
print(W)
if W>300:
    print("Sunny")
elif 200<W<=300:
    print("Cloudy")
elif 100<W<=200:
    print("Rainy")
else:
    print("Stormy")
