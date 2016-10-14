#coding:utf-8

#Sympyはあらゆる記号が入った数式を演算することができます
import sympy as sym
#Real,Rational,Integerの数値型を持つ
#有理数
a=sym.Rational(1,2)
#無理数
b=sym.Pow(3,0.5)

x,y,z=sym.symbols("x,y,z")
#円周率
pi=sym.pi
#自然対数の底
e=sym.exp(1)
#浮動小数点として評価
#標準は16桁
#print pi.evalf()
#100桁まで表示
#print pi.evalf(100)

#記号演算
#x=sym.Symbol("x")
#y=sym.Symbol("y")

#sym.var("x,y")
#x,y=sym.symbols("x,y")


#展開
#print sym.expand((x+y)**3)
#三角関数も展開できる
#print sym.expand(sym.cos(x+y),trig=True)
#因数分解
#print sym.factor(x**2+2*x*y+y**2)

#単純化
#print sym.simplify((x+x*y)/x)
#三角関数も単純化できる
#print sym.trigsimp(sym.cos(x)/sym.sin(x))

#代入
#sin(x)にx=3を代入して、数値化
#print sym.sin(x).subs(x,3).evalf()
#極限
#print sym.limit(sym.sin(x)/x.x,0)

#微分
#print sym.diff(sym.sin(x),x)
#print sym.diff(sym.cos(x),x)
#print sym.diff(sym.tan(x),x)
#二階微分もできる
#print sym.diff(sym.tan(x),x,3)

#級数展開
#print sym.series(sym.cos(x),x,3)

#積分
#print sym.integrate(6*x**5,x)
#print sym.integrate(sym.sin(x),x)
#print sym.integrate(sym.log(x),x)

#範囲を指定して積分する
#print sym.integrate(x**3,(x,-1,1))
#print sym.integrate(sym.sin(x),(x,-sym.pi,sym.pi))

#広義積分もできる
#print sym.integrate(sym.exp(-x**2),(x,0,sym.oo))

#部分分数分解
#print sym.apart(1/((x+3)*(x+2)),x)

#一つにまとめる
#y=sym.apart(1/((x+3)*(x+2)),x)
#print sym.together(y,"x")

#総和
#n=sym.Symbol("n")
#sum=sym.summation(x**3,(x,1,n))
#print  sym.factor(sum)

#連立方程式
#ansはdict(辞書)型
#ans=sym.solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
#print ans

#代数方程式
#d=sym.Symbol("d")
#print sym.solve((x-3)*(x+2)*(x-2)*(x+d),x)
#微分方程式
#y=sym.Function("y")
#x=sym.Symbol("x")
#dy/dx-2y=0を解く
#print sym.dsolve(y(x).diff(x )-2*y(x), y(x))
#線形代数
#Numpyと異なり、記号を含むことができます
#A=sym.Matrix([[x,y],[y,x]])
#print A**4

#M=sym.Matrix(2, 2, lambda i,j: i*j+2)
#print M.eigenvals()
"""
M=sym.Matrix([[1,2],[-1,4]])

#固有値{固有値:ランク,} dict型
myEig=M.eigenvals()
print myEig.keys()[0]
rint myEig.keys()[1]


myVec=M.eigenvects()
#固有値①
print myVec[0][0]
#固有値①のランク
print myVec[0][1]
#固有ベクトル
print myVec[0][2]

#固有値②
print myVec[1][0]
#固有値②のランク
print myVec[1][1]
#固有ベクトル
print myVec[1][2]
"""
#print M.eigenvects()