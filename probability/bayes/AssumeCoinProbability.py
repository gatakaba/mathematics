# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
import os, sys
import shutil
import subprocess

plt.ion()
def makegif(dir="coin_img"):
    if os.path.exists(dir):
        p = subprocess.Popen(["mogrify" , "-resize", " 640x480", dir + "/*.jpg"])
        p.wait()
        p = subprocess.Popen(["convert" , "-delay" , "40", "-loop" , "0", dir + "/*.jpg", "myimage.gif"])
        p.wait()
        shutil.rmtree(dir)
    else:
        print "no file coin_img \n "

def plot(results, save=False):
    x = np.linspace(0 + 10 ** -4, 1 - 10 ** -4, 1000)
    a , b = sum(results) , len(results) - sum(results)
    f = beta(a + 1 , b + 1)
    y = f.pdf(x)
    mean, std, entropy = f.mean(), f.std(), f.entropy()
    plt.clf()
    plt.ylim(0, 10)
    plt.plot(x, y)
    if not len(results) == 0:
        plt.hist(results, normed=True, alpha=0.1)
    plt.fill_between(x, 0, y, where=(-std * 2 + mean < x) & (x < std * 2 + mean), alpha=0.5)
    plt.xticks(np.arange(0, 1, 0.1))
    plt.text(0.75, 9.5, "total:{0}" .format(a + b))
    plt.text(0.75, 9, "face:{0},tail:{1}" .format(a, b))
    plt.text(0.75, 8.5, "mean:%1.3f" % mean)
    plt.text(0.75, 8, "std:%1.3f" % std)
    plt.text(0.75, 7.5, "entropy:%1.3f" % entropy)
    if save:
        if not os.path.exists("coin_img"):
            os.mkdir("coin_img")
        plt.savefig("coin_img/coin_{0:0>3}.jpg" .format(str(len(results))))
    else:
        plt.pause(0.01)
    
def main():
    results = []
    plot(results, save=True)
    for n in range(500):
        result = np.random.binomial(1, p=0.25)
        results.append(result)
        a , b = sum(results) , len(results) - sum(results)
        mean, std, entropy = beta(a + 1 , b + 1).mean(), beta(a + 1 , b + 1).std(), beta(a + 1 , b + 1).entropy()
        # print "face:" + str(a) + "," + "tail:" + str(b)
        # print "mean:%1.3f,std:%1.3f,entropy:%1.3f" % (beta(a + 1, b + 1).mean(), beta(a + 1, b + 1).std(), beta(a + 1, b + 1).entropy())
        if len(results) % 10 == 0:
            plot(results, save=True)
    
if __name__ == "__main__":
    main()
    makegif()
