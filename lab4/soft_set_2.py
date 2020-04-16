import skfuzzy as fuzzy
import numpy as np
import pandas as pd
import random

path_to_softset = 'soft_set_2.csv'
E = ['świeże', 'mrożone', 'ostre', 'słodkie', 'zielone', 'czerwone', 'lokalne', 'tropikalne', 'liściaste', 'bulwowe']
groups = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]


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


# region Random Rows
# df = pd.read_csv(path_to_softset, sep=';', index_col=0).to_numpy()
# for i in range(17):
#     temp = list()
#     for j in range(len(E)):
#         temp.append(random.randint(0, 1))
#     df = np.append(df, temp).reshape([i + 4, 10])

# df = pd.DataFrame(df, index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#                              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'], columns=E)
# df.to_csv(path_to_softset, sep=';', index_label='klient')
# endregion

df = pd.read_csv(path_to_softset, sep=';', index_col=0).T
print(df)
values = list()
for row in df.values:
    values.append(sum(row))

print(make_decision(values, groups))

