# 접미사 배열

s = input()
string_list = []
for i in range(len(s)):
    string_list.append(s[i:])

string_list.sort()

for i in string_list:
    print(i)
