from sympy import factor, symbols

x,y = symbols('x, y')

equation = 3*x*y - 6*y**2-x+2*y

print(factor(equation))