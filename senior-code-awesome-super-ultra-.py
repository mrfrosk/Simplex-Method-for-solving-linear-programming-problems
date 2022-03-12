import numpy as np

table = []
first_line = input('Введите таблицу \n>> ').split(' ')
cols_count = len(first_line)
first_line = list(map(float, first_line))
table.append(first_line)
while 1:
    line = input('>> ').split(' ')
    if line != ['']:
        if len(line) == cols_count:
            line = list(map(float, line))
            table.append(line)
        else:
            print('Неверное количество элементов в строке')
            continue
    else:
        while 1:
            line = input('Введите строку относительных оценок\n>> ').split(' ')
            if len(line) != cols_count - 1:
                print(
                    "Неверное количество эллементов в строке относительных оценок "
                )
            else:
                line = list(map(float, line))
                table.append(line)
                break
        break
table = np.array(table)

res_column_idx = len(table) - 1 
res_column_idx = np.amin(table[res_column_idx])

res_column_idx = np.where(table[len(table) - 1] == res_column_idx)
res_column_idx = int(res_column_idx[0])

res_row_idx = 0
res_row_value = table[0][len(table[0]) - 1] / table[0][res_row_idx]
for i in range(1,len(table) - 1):
    value = table[i][len(table[0]) - 1] / table[i][res_column_idx] 
    if value < res_row_value:
        res_row_value = value 
        res_row_idx = i
res_row_idx = int(res_row_idx)
for i in table:
    print(i)
del res_row_value 
res_elem = int(table[res_row_idx][res_column_idx])
print(res_elem)
for i in range(0,len(table)):
    if i != res_row_idx:
        for j in range(0,len(table[i])):
            if j != res_column_idx:
                table[i][j] = table[i][j]  - ((table[i][res_column_idx] * table[res_row_idx][j]) / res_elem)
                table[i][j] = round(table[i][j],2)
print("")
for i in range(0,len(table) ):
    if table[i][res_column_idx] != res_elem:    
        table[i][res_column_idx] = round((table[i][res_column_idx] / res_elem * -1),2)

value = len(table[0])

for i in range(0,value):
    if table[res_row_idx][i] != res_elem:
         table[res_row_idx][i] =     round(table[res_row_idx][i] / res_elem,2)
         
                         
         
for i in table:
    print(i)
