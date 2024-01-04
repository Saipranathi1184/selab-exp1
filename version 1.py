T=25
H=65
w=20
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