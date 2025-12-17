base = int(input("Enter the base Value : "))
Exponent =int(input("Enter the Exponent value : "))

power =1

for i in range(Exponent):
    power = power * base

print(power)

# print(base ** Exponent)