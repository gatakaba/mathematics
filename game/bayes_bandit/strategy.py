# coding:utf-8
'''
Thompson samplingとも
1. 各バンディットにベータ分布を割り当てる
2. 各バンディットのベータ分布からサンプリングを行う
3. 最も高い値のサンプルを出力したバンディットBを選択する
4. 観測結果をバンディットBのベータ分布に反映させる
5. 2.を繰り返す
'''
# todo : スコア
# todo : 進捗状況表示

from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
import abc


class Strategy(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    '''
    @abc.abstractmethod
    def slot(self):
        pass
    '''


class BayesianStrategy(Strategy):
    def __init__(self, bandit):
        super().__init__()

        self.bandit = bandit
        self.n_bandit = len(self.bandit)
        self.beta_parameter = [{'a': 1, 'b': 1} for i in range(self.n_bandit)]
        self.log = []

    def slot(self, n_iter, verbose=False):
        # n_iter回スロットを打ち,パラメータを更新する
        for i in range(n_iter):
            print(i)
            choice, result = self._slot()

            # 結果を記録
            self.log.append({'choice': choice, 'result': result})
            if verbose:
                print('{0},choice:{1},result:{2}'.format(n_iter, choice, result))

        return self.log

    def _slot(self):
        # 1回スロットを打ち,パラメータを更新する
        choice = self._sample()
        result = self.bandit.pull(choice)

        # パラメータの更新
        if result == True:
            self.beta_parameter[choice]['b'] += 1
        else:
            self.beta_parameter[choice]['a'] += 1
        return choice, result

    def _sample(self):
        # N個のベータ分布からサンプリングして、最も大きな値のバンディットのインデックスを出力する
        l = []
        for i in range(self.n_bandit):
            a = self.beta_parameter[i]['a']
            b = self.beta_parameter[i]['b']
            l.append(beta(a, b).rvs())
        return np.argmax(l)

    def score(self):
        pass

    def draw_distribution(self):

        x = np.linspace(0, 1, 1000)
        for i in range(self.n_bandit):
            a = self.beta_parameter[i]['a']
            b = self.beta_parameter[i]['b']
            p = beta(a, b).pdf(x)
            plt.plot(x, p, label='No.{0} bandit'.format(i))
        plt.legend()
        plt.show()
