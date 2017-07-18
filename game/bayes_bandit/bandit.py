# coding :utf-8
import numpy as np
from strategy import Strategy


class Bandit(object):
    def __init__(self, p):
        self.p = p

    def pull(self, i):
        # i番目のアームを引く.勝ったらTrue,負けたらFalse

        if i > len(self.p):
            raise IndexError("index error")

        if np.random.random() < self.p[i]:
            result = False
        else:
            result = True
        return result

    def evaluate_strategy(self, strategy, n_iter=100):
        print(strategy)

    def __len__(self):
        return len(self.p)
