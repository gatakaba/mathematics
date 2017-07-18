# coding :utf-8
'''
- 多腕バンディットシミュレータ
-
'''

import numpy as np
from bandit import Bandit
from strategy import BayesianStrategy

if __name__ == '__main__':
    n_bandit = 5
    p = [0.9, 0.2, 0.1, 0.1, 0.4]

    bandit = Bandit(p)

    bs = BayesianStrategy()
    score = bandit.evaluate(bs, n_iter=1000)
