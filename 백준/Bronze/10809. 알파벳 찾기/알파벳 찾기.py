a_list = [a for a in 'abcdefghijklmnopqrstuvwxyz']

ans, s = "", input()
for a in a_list: ans+=str(s.index(a))+" " if a in s else "-1 "
print(ans)