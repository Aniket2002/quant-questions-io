from sympy import symbols, Eq, solve

# Question:  You flip a fair coin until you see the pattern HTH. What is the expected number of tosses to see this pattern?

# Solve for x

x_symbol = symbols('x')
equation = Eq((1/2) * (x_symbol + 1) + (1/4) * x_symbol + (1/8) * (x_symbol + 3) + (1/8) * 3, x_symbol)
expected_value = solve(equation, x_symbol)[0]

print(f"Expected value of the number of tosses to see HTH: {expected_value}")