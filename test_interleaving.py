# test_interleaving.py

def test_interleaving():
    user_id = 123
    per_page = 5

    # 全ページ取得して一意性確認
    full_set = set()
    for page in range(1, 7):  # 5件×6ページ = 30件
        result = interleaving(user_id, page, per_page)
        print(f"Page {page}: {result}")
        assert len(result) <= per_page
        assert len(set(result)) == len(result)
        full_set.update(result)

    # 全ての new_ranking, old_ranking のIDが1度は出現するか
    new_ids = set(new_ranking(user_id, 1, 1000))
    old_ids = set(old_ranking(user_id, 1, 1000))
    assert new_ids.issubset(full_set)
    assert old_ids.issubset(full_set)
    print("すべての募集IDが表示されました ✔️")

test_interleaving()
