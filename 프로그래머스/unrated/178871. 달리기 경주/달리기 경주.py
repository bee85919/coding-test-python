def solution(runner, passings):
    rank = {name: rank for rank, name in enumerate(runner)}

    for passing in passings:
        idx = rank[passing]
        if idx == 0: continue
        runner[idx], runner[idx-1] = runner[idx-1], runner[idx]
        rank[runner[idx]], rank[runner[idx-1]] = idx, idx-1

    return runner