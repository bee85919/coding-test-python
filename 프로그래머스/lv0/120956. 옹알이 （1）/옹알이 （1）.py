def solution(babbling):
    
    ans = 0    
    for babble in babbling: 
        word, cnt = '', 0
        for b in babble: 
            word += b
            if word in ['aya', 'ye', 'woo', 'ma']:
                word = ''; cnt += 1
                
        if len(word) == 0 and cnt > 0: 
            ans += 1
                
    return ans