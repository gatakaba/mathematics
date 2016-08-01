import sympy as sym

# x=sym.Symbol("x")
# y=sym.Symbol("y")

x, y , z = sym.symbols("x,y,z")
def factorizatoin():
    f = 1 - x ** 2 - y ** 2 - z ** 2 + 2 * x * y * z - (x - y * z) * (y - z * x) - (y - z * x) * (z - x * y) - (z - x * y) * (x - y * z)
    print sym.factor(f)

