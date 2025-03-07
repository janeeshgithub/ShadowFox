# Assigning values and checking types
a = 10
b = 3.14
c = 'Hello, Python!'
print(type(a))
print(type(b))
print(type(c))

# Swapping values
a, b = b, a
t=10
p=20
t=t^p
p=t^p
t=p^t
print(t,p)
print(a, b)

# Simple Interest Calculation
p = 1000  # Principal
r = 5      # Rate of interest
t = 2      # Time in years
si = (p * r * t) / 100
print('Simple Interest:', si)
