# coding:utf-8
"""
コイン投げのようなベルヌーイ試行における生起確率μは
ベータ分布を共役事前分布としてベイズ更新して推測することができる。
しかし現在の推定結果と新たな観測が生起確率のエントロピーの変化にどのような
関係があるのかは不明だった。
自分の予想ではいかなる場合も新たな観測データを得ることによってエントロピーは減少する
との事だったが、実際に計算してみた結果、ある条件下では新たなデータを得られたのに関わらずエントロピーが
増加する場合があることがわかった。
ある状況とは、例えばaがbと比較して極めて大きい場合bが観測された時である。
また詳細に調べた所、エントロピーのピークはa:b=1:1を満たす場合ではなく、
a,bに依存するボーダが存在するということもわかった。
ボーダに囲まれた範囲内においては観測データが得られるにつれてエントロピーは減少する。
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.ndimage.filters import convolve

def plot():
    # os.remove("test23.txt.npy")
    try:
        z = np.load("entropy.npy")
    except:
        a, b = [np.linspace(1, 50, 150)] * 2
        aa, bb = np.meshgrid(a, b)
        z = beta(aa, bb).entropy()
        np.save("entropy", z)
    
    plt.pcolor(z)
    plt.contourf(z)
    plt.colorbar()
    plt.show()
    from mayavi import mlab
    mlab.surf(z * 100)
    mlab.surf(z * 0 - 150)
    mlab.show()
    # 
    
def calc():
    a, b = 100, 1
    e1 = beta(a, b).entropy()
    a, b = 100, 2
    e2 = beta(a, b).entropy()
    # if e2>e1 , entropy is increased regardness additional observation.
    print e2 - e1, e2 > e1
    
if __name__ == "__main__":
    
    plot()
    a = np.linspace(1, 50, 150)
    b = 10
    e2 = beta(a, b).entropy()
    # plt.plot(a, e2)
    # plt.scatter(a, e2)
    
    plt.show()
    
    
        
