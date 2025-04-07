import json
import os
from distutils.dir_util import remove_tree

from Tools.scripts.verify_ensurepip_wheels import GITHUB_ACTIONS
from fontTools.misc.cython import returns


# get current working directory path
# cwd_path = os.getcwd()


# def read_data(file_name, field):
#     """
#     Reads json file and returns sequential data.
#     :param file_name: (str), name of json file
#     :param field: (str), field of a dict to return
#     :return: (list, string),
#     """
#     file_path = os.path.join(cwd_path, file_name)


# def read_data(file_name, key):
#     file_name = "sequential.json"
#     key = "unordered_numbers"
#
#     with open(file_name) as f:
#         data = json.load(f)
#         if key in data:
#             x = data[key]
#         else:
#             x = "None"
#
#     return x




# seznam = [54, 2, 18, 5, 3, 31, 20, 65, 31]          #
# cislo = 31
# pozice = [] #+1
# for index, num in enumerate(seznam):    #+n
#     if num == cislo:    #+n
#         pozice.append(index)    #+n
#         # print(f"{index + 1}. pozice cislo {num}.")
#     else:
#         continue
# # 1 + 3n = O(n)
#
# print(pozice)
# print(len(pozice))
# # n = len(seznam)
# # for index in range(n):



# dna = "TGGACTGAGACC"
# n = len(dna)    #1
# sekvence = "GA"
# m = len(sekvence)   #1
# post = set()    #1
# for i in range(n - (m - 1)):    #n - (m - 1) → n    !!
#     # print(dna[i:i + m])
#     # if (dna[i:i + m]) == sekvence:
#     #     print(i)
#     is_same = True  #n - (m - 1)
#
#     for ii in range(m): #m (n - (m - 1))
#         if (dna[i + ii]) != (sekvence[ii]):
#             is_same = False #m (n - (m - 1))
#             # break → ukonci drive, pri nejlepsim pripade bude obtiznost O(n) / zrychli kod
#
#     if is_same: #n - (m - 1)
#         post.add(i) #n - (m - 1)

# 3 + 4(n - m + 1) + 3m(n - m + 1) = ... = O(m * n) O(n)






# pro serazena cisla:

hodnoty = [6, 12, 17, 23, 38, 45, 77, 84, 90]
delka = len(hodnoty)
cislo = 45
L = 0
R = delka - 1
found = None
# middle = (L + R) / 2
# while R >= L:
#     if middle != cislo:
#         if middle < cislo:
#             L = hodnoty[middle + 1]
#         elif middle > cislo:
#             R = hodnoty[middle]
#     else:
#         middle = cislo
# print(middle)



while True:
    midle = (L + R) // 2

    if hodnoty[midle] > cislo:
        R = midle - 1
    elif hodnoty[midle] < cislo:
        L = midle





from generators import ordered_sequence

for












# def main():
#     pass
#
#
# if __name__ == '__main__':
#     main()