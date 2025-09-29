import json
import os
import random
import time
from statistics import mean

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "api", "transactions.json")

def load_transactions():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def linear_search(lst, target_id):
    for item in lst:
        if item.get("id") == target_id:
            return item
    return None

def dict_lookup(dct, target_id):
    return dct.get(target_id)

def benchmark(trs, trials=20):
    # preparing dict mapping
    d = {t["id"]: t for t in trs}
    ids = [t["id"] for t in trs]
    if len(ids) < trials:
        trials = len(ids)

    sample_ids = random.sample(ids, trials)

    linear_times = []
    dict_times = []

    for sid in sample_ids:
        start = time.perf_counter()
        linear_search(trs, sid)
        linear_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        dict_lookup(d, sid)
        dict_times.append(time.perf_counter() - start)

    results = {
        "trials": trials,
        "linear_avg_sec": mean(linear_times),
        "dict_avg_sec": mean(dict_times),
        "linear_times": linear_times,
        "dict_times": dict_times
    }
    return results

if __name__ == "__main__":
    trs = load_transactions()
    print(f"Loaded {len(trs)} transactions")
    res = benchmark(trs, trials=min(20, len(trs)))
    print("Benchmark results (averages in seconds):")
    print(json.dumps(res, indent=2))
    print("\nReflection:")
    print("Dictionary lookup is O(1) average time; linear search is O(n). For larger datasets, dict lookup will be much faster.")
    print("Alternative improvements: use an indexed database (SQLite, Postgres) with an index on id, or use B-tree or hash-based indexes. For range/time queries, use sorted structures or an in-memory search tree (e.g., bisect on sorted lists) or specialized search engines (Elasticsearch).")
