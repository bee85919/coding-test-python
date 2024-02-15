# def solution(cite):
#     return max(map(min,enumerate(sorted(cite,reverse=True),start=1)))


def solution(cite):
    cite = list(enumerate(sorted(cite, reverse=True), start=1))
    print(cite)
    mins = list(map(min, cite))
    print(mins)
    ans = max(mins)
    print(ans)
    return ans