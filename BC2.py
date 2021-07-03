def solution(param0):
    types = {'BOOL': 1, 'SHORT': 2, 'FLOAT': 4, 'INT': 8, 'LONG': 16}
    size = [types[t] for t in param0]
    print(size)
    # answer = ''
    # for data_type in param0:
    #     if data_type == 'LONG':
    #         result += types[data_type]
            


solution(['INT','INT','BOOL','SHORT','LONG']) # => '########, ########, #.##....,########,########'
solution(['INT','SHORT','FLOAT','INT','BOOL']) # => '########,##..####,########,#.......'
solution(['FLOAT','SHORT','BOOL','BOOL','BOOL', 'INT']) # => '########,#.......,########'
solution(['BOOL', 'LONG', 'SHORT', 'LONG', 'BOOL', 'LONG','BOOL','LONG','SHORT','LONG','LONG']) # => HALT
