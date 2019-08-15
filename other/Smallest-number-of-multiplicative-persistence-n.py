"""全桁の相乗を1桁になるまで計算し続けるプログラム"""
import functools
import operator
import time


def calc(n):
    n_str = str(n)
    if "0" in n_str:
        return 0
    n_str_list = map(int, n_str)
    next_num = functools.reduce(operator.mul, n_str_list)
    return next_num


def run():
    N = 10 ** 6
    max_cnt, max_num = 0, 0
    d = dict()
    for i in range(N):
        n,cnt = i,0
        while True:
            if n in d:
                cnt += d[n]
                break
            n = calc(n)
            if n < 10:
                break
            else:
                cnt += 1
        if cnt != 0:
            d[i] = cnt

        if cnt > max_cnt:
            max_cnt = cnt
            max_num = i

    return max_cnt, max_num


if __name__ == "__main__":

    start = time.time()
    max_cnt, max_num = run()
    elapsed = time.time() - start
    print(max_cnt, max_num, elapsed)

