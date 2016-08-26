# coding:utf-8
import random


def monty_hall():
    """モンティ・ホール問題シミュレータ

    出題者がハズレを見せた後、選択したドアを変更する

    Returns:
        is_hit : 正解の場合、True,不正解の場合、False
    """
    # 正解のドア
    answer_door_id = random.choice(range(3))
    # 回答者が最初に選んだドア
    first_choice_id = random.choice(range(3))
    # 出題者が開くドア
    open_door_id = random.choice(list(filter(lambda x: x != answer_door_id and x != first_choice_id, range(3))))
    # 回答者が二回目に選んだドア
    second_choice_id = random.choice(list(filter(lambda x: x != first_choice_id and x != open_door_id, range(3))))

    return second_choice_id == answer_door_id


if __name__ == "__main__":

    hit_num = 0
    N = 10 ** 6  # 繰り返し数
    for i in range(N):
        if monty_hall():
            hit_num += 1
    print(hit_num / N)
