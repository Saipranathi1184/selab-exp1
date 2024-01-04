variable = {}
with open('weather.txt', 'r') as file:
    for line in file:
        name, value = line.replace(' ', '').split('=')
        variable[name.strip()] = int(value)  # Removing spaces and storing values in the dictionary

W = (0.5) * (variable['T'] ** 2) - (0.2) * variable['H'] + (0.1) * variable['w'] - 15
print(W)

if W > 300:
    print("Sunny")
elif 200 < W <= 300:
    print("Cloudy")
elif 100 < W <= 200:
    print("Rainy")
else:
    print("Stormy")
