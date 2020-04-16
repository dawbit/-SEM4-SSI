import skfuzzy as fuzzy
import numpy as np
import pandas as pd
import random

path_to_softset = 'soft_set_1.csv'
E = ['drogie', 'tanie', 'jeans', 'dresowe', 'klasyczne', 'modern', 'fit', 'granatowe', 'czarne', 'na zamek',
     'na guziki']
groups = [[0, 1], [2, 3], [4, 5, 6], [7, 8], [9, 10]]
# A = {'jeans', 'modern', 'na zamek'}
# B = {'jeans', 'klasyczne', 'granatowe', 'na guziki'}


def make_decision(arg_values, arg_groups):
    decision = "Decyzja: "
    for group in arg_groups:
        bool_same = False
        temp_values = list()
        for index in group:
            temp_values.append(arg_values[index])

        temp_max = temp_values[0]
        for x in temp_values[1:]:
            if x > temp_max:
                temp_max = x
            elif x == temp_max:
                bool_same = True
                break
        if not bool_same:
            decision += E[group[temp_values.index(max(temp_values))]] + " "

    return decision


df = pd.read_csv(path_to_softset, sep=';', index_col=0).T
print(df)
# region Random Rows
# df = pd.read_csv(path_to_softset, sep=';', index_col=0).to_numpy()
# for i in range(18):
#     temp = list()
#     for j in range(len(E)):
#         temp.append(random.randint(0, 1))
#     df = np.append(df, temp).reshape([i + 3, 11])
#
# df = pd.DataFrame(df, index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#                              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'], columns=E)
# df.to_csv(path_to_softset, sep=';', index_label='klient')
# endregion

values = list()
for row in df.values:
    values.append(sum(row))

print(make_decision(values, groups))
