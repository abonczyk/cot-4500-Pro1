#Method 1

i = 0
p = 0
right = 7
left = -4
def f(x):
    return x**2 - 1


while abs(right - left) > 10**(-4) and i < 50:
    i += 1
    p = (left + right)/2

    if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
        right = p
    else:
        left = p
print("Approximation Algorithm:")
print(f"Found root {p} after {i} iterations\n")

#Method 2

def f(x):
    return x**2 - 9

while abs(right - left) > 10**(-4) and i < 10:
	i += 1
	p = (left + right)/2

	if (f(left) > 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
		right = p
	else:
		left = p
print("Bisection Method:")
print(f"Found root {p} after {i} iterations\n")

#Method 3

def f(x):
    return x**2 + 4*x + 4
p = 0
p0 = 1
i = 0

'''
print("Fixed-Point Iteration Method:")
while (i <= 100):
	p = f(p0)
	if (abs(p - p0) < 10**(-4)):
		print(f"Success:  found root {p} after {i} iterations.\n")
		break
	i += 1
	p0 = p
print("Failure")
'''

#Method 4

p_prev = 1
p_next = 0
i = 1

import sympy as sp

x = sp.Symbol('x')
f = x**3 - 1

f_prime = sp.diff(f, x)

print("Newton-Raphson Method:")

while (i <= 10):
    if float(f_prime.subs(x, p_prev)) != 0:
        p_next = p_prev - float(f.subs(x, p_prev))/float(f_prime.subs(x, p_prev))
        if abs(p_next - p_prev) < 0.001:
            print(f"Success: {p_next} (iterations: {i})")
            break
        p_prev = p_next
        i += 1
    else:
        print("Unsuccessful")
        break
