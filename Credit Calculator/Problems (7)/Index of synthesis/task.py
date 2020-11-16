n = float(input())
if n < 2:
    print("Analytic")
elif 2 <= n <= 3:
    print("Synthetic")
elif n > 3:
    print("Polysynthetic")
