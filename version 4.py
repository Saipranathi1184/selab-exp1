inputs = []
n = int(input("Enter the number of iterations: "))
for i in range(n):
    t, h, w = map(int, input(f"Enter values for iteration {i+1} (space-separated): ").split())
    inputs.append([t, h, w])

result = []
for each in inputs:
    T, H, w = each
    W = (0.5) * (T ** 2) - (0.2) * H + (0.1) * w - 15
    if W > 300:
        ans = "Sunny"
    elif 200 < W <= 300:
        ans = "Cloudy"
    elif 100 < W <= 200:
        ans = "Rainy"
    else:
        ans = "Stormy"
    result.append(ans)

print(result)
