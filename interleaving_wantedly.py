from typing import List

# スタブ：実際のランキングロジックではなく、疑似データを返す
def new_ranking(user_id: int, page: int, per_page: int) -> List[int]:
    ids = list(range(1, 51))  # 1〜50までのダミーID
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    return ids[start_idx:end_idx]

def old_ranking(user_id: int, page: int, per_page: int) -> List[int]:
    ids = list(range(100, 150))  # 100〜149までのダミーID
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    return ids[start_idx:end_idx]

def interleaving(user_id: int, page: int, per_page: int) -> List[int]:
    """
    Interleaving によって、new_ranking と old_ranking の結果を混合し、
    指定ページに対応する募集IDを返す。
    """
    # 両ランキングから必要なアイテムを多めに取得
    max_items = page * per_page
    new_items = new_ranking(user_id, 1, max_items)
    old_items = old_ranking(user_id, 1, max_items)

    # インターリーブ処理
    interleaved = []
    seen = set()
    i = j = 0

    while len(interleaved) < max_items and (i < len(new_items) or j < len(old_items)):
        if i < len(new_items):
            if new_items[i] not in seen:
                interleaved.append(new_items[i])
                seen.add(new_items[i])
            i += 1
        if len(interleaved) >= max_items:
            break
        if j < len(old_items):
            if old_items[j] not in seen:
                interleaved.append(old_items[j])
                seen.add(old_items[j])
            j += 1

    # ページング処理
    start = (page - 1) * per_page
    end = start + per_page
    return interleaved[start:end]
