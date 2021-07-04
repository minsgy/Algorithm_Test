# 2번 문제
def solution(param0):
    types = {'BOOL': 1, 'SHORT': 2, 'FLOAT': 4, 'INT': 8, 'LONG': 16}
    size = [types[t] for t in param0]
    ret = []
    cur_str = ''

    for s in size:
        if len(cur_str) <= 8-s:
            cur_str += '.' * ((s-len(cur_str)) % s) + '#' * s
            if len(cur_str) == 8:
                ret.append(cur_str)
                cur_str = ''
        
        else:
            if len(cur_str):
                ret.append(cur_str + '.' * (8-len(cur_str)))
                cur_str = ''
            if s >= 8:
                for _ in range(s // 8):
                    ret.append('########')
            else:
                cur_str = '#' * s
    
    if cur_str:
        ret.append(cur_str + '.' * (8-len(cur_str)))
    
    return ','.join(ret) if len(ret) <= 16 else 'HALT'

            


print(solution(['INT','INT','BOOL','SHORT','LONG'])) # => '########, ########, #.##....,########,########'
print(solution(['INT','SHORT','FLOAT','INT','BOOL'])) # => '########,##..####,########,#.......'
print(solution(['FLOAT','SHORT','BOOL','BOOL','BOOL', 'INT'])) # => '########,#.......,########'
print(solution(['BOOL', 'LONG', 'SHORT', 'LONG', 'BOOL', 'LONG','BOOL','LONG','SHORT','LONG','LONG'])) # => HALT
