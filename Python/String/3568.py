# iSharp
import sys
n = sys.stdin.readline()
var_list = list(n.split(', '))
first_list = list(var_list[0].split(' '))
base = first_list[0]
var_list[0] = first_list[1]
var_list[-1] = var_list[-1][:-1]
last = ';'

for var in var_list:
    var = list(var)
    new_var = []
    for i in range(len(var)):
        new_var.append(var.pop())
    for i in range(len(new_var)-1):
        if new_var[i] == ']' and new_var[i+1] == '[':
            new_var[i], new_var[i+1] = new_var[i+1], new_var[i]

    new_var = ''.join(new_var)
    print(base + new_var[:-1] + ' ' + new_var[-1] + last)
