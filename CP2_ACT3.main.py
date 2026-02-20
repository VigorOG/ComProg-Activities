x = 300

print("Find the closest number to", x)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

diff_a = abs(a - x)
diff_b = abs(b - x)
diff_c = abs(c - x)

smallest = min(diff_a, diff_b, diff_c)

if diff_a == smallest:
    print("The closest number to", x, "is:", a)
elif diff_b == smallest:
    print("The closest number to", x, "is:", b)
else:
    print("The closest number to", x, "is:", c)