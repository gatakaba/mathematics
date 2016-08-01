# coding:utf-8
import sympy as sym
A = sym.MatrixSymbol("A", 3, 3)
B = sym.MatrixSymbol("B", 3, 3)
C = sym.MatrixSymbol("C", 3, 3)
D = sym.MatrixSymbol("D", 3, 3)

V = sym.MatrixSymbol("V", 3, 1)

a = sym.MatrixSymbol("a", 2, 3)
b = sym.MatrixSymbol("b", 2, 1)

# print sym.Matrix(a * a.T)
print sym.Matrix(a[:, 0] * a[:, 0].T + a[:, 1] * a[:, 1].T + a[:, 2] * a[:, 2].T)
print sym.Matrix(a * a.T)
# print sym.Matrix(a * a.T)[1, : ].T
# 行列内容確認
# print sym.Matrix(A)
# 各種計算
# print sym.Matrix(A+B)
# print sym.Matrix(A*B)

# 転置
# print A.T
# 逆行列
# print A.I
# trace
# print sym.Trace(A)
E = sym.BlockMatrix([[A, B], [C, D]])



