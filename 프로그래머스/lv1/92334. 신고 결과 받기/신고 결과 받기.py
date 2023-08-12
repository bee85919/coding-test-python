from collections import defaultdict


def solution(ids, report, k): 
    id_reported = defaultdict(set)
    id_rptd_cnt = defaultdict(int)
    
    for r in report:
        reporter, reported = r.split()
        if reported not in id_reported[reporter]:
            id_reported[reporter].add(reported)
            id_rptd_cnt[reported] += 1
    
    banned_users = {id for id, cnt in id_rptd_cnt.items() if cnt >= k}
    
    result = []
    for id in ids:
        mail_cnt = sum(1 for reported in id_reported[id] if reported in banned_users)
        result.append(mail_cnt)
    
    return result