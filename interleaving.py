from typing import List
from itertools import zip_longest
from ranking_sources import new_ranking, old_ranking

def interleaving(user_id: int, page: int, per_page: int) -> List[int]:
    new_items = new_ranking(user_id, 1, 1000)
    old_items = old_ranking(user_id, 1, 1000)

    seen = set()
    interleaved = []
    for n, o in zip_longest(new_items, old_items):
        for x in [n, o]:
            if x is not None and x not in seen:
                interleaved.append(x)
                seen.add(x)

    start = (page - 1) * per_page
    end = start + per_page
    return interleaved[start:end]
