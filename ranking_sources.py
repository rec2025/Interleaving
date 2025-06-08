from typing import List

def new_ranking(user_id: int, page: int, per_page: int) -> List[int]:
    # ダミーのランキング生成（例：昇順 1〜100）
    return list(range(1, 101))

def old_ranking(user_id: int, page: int, per_page: int) -> List[int]:
    # ダミーのランキング生成（例：51〜150）
    return list(range(51, 151))
