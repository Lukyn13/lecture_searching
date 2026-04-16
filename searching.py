# import os
# from dataclasses import field
# from distutils.dir_util import remove_tree
#
# from Tools.scripts.verify_ensurepip_wheels import GITHUB_ACTIONS
# from fontTools.misc.cython import returns


# get current working directory path
# cwd_path = os.getcwd()


# -----------------------------------------------------------------------
# Dnešní cvičení ...

import json


def read_data(file_name, field):
    with open(file_name, mode="r") as object:
        data = json.load(object)
        if field in data.keys():
            return data[field]
        else:
            return None


def linear_search(sekvence_cisel, hledane_cislo):
    slovnik = {}
    pozice = []
    pocet = 0
    for index, cislo in enumerate(sekvence_cisel):
        if cislo == hledane_cislo:
            pozice.append(index)
            pocet += 1
    slovnik["positions"] = pozice
    slovnik["count"] = pocet
    return slovnik


# def binary_search(seznam_cisel, hledane_cislo):
#     for index, cislo in enumerate(seznam_cisel):
#         if cislo == hledane_cislo:
#             return index
#     return None


def binary_search(seznam_cisel, hledane_cislo):
    levy_kraj = 0
    pravy_kraj = len(seznam_cisel) - 1          # indexuju od 0
    while levy_kraj <= pravy_kraj:
        stredovy_index = (levy_kraj + pravy_kraj) // 2
        if seznam_cisel[stredovy_index] == hledane_cislo:
            return stredovy_index
        elif seznam_cisel[stredovy_index] < hledane_cislo:
            levy_kraj = stredovy_index + 1      # musím přičíst 1, abych se posunul blíže
        elif seznam_cisel[stredovy_index] > hledane_cislo:
            pravy_kraj = stredovy_index - 1
    return None
    # delka = len(seznam_cisel)
    # stred = seznam_cisel[(delka // 2) + 1]



import time

numbers = [4, 8, 15, 16, 23, 42, 55, 78, 91, 120]
target = 78
start = time.perf_counter()
for number in numbers:
    if number == target:
        break
end = time.perf_counter()
duration = end - start
print(f"Měření trvalo {duration:.8f} s")



import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]
times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]
plt.plot(sizes, times)
plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()



from generators import unordered_sequence
from generators import ordered_sequence
from generators import dna_sequence







def main():
    # print(read_data("sequential.json", "dna_sequence"))
    sekvence = read_data("sequential.json", "ordered_numbers")
    vyhledat_cislo = -10
    print(linear_search(sekvence, vyhledat_cislo))
    # serazena_sekvence = sorted(sekvence)
    serazena_sekvence = read_data("sequential.json", "ordered_numbers")
    print(binary_search(serazena_sekvence, vyhledat_cislo))


if __name__ == '__main__':
    main()


# ----------------------------------------------------------------------------













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

# hodnoty = [6, 12, 17, 23, 38, 45, 77, 84, 90]
# delka = len(hodnoty)
# cislo = 45
# L = 0
# R = delka - 1
# found = None
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



# while True:
#     midle = (L + R) // 2
#
#     if hodnoty[midle] > cislo:
#         R = midle - 1
#     elif hodnoty[midle] < cislo:
#         L = midle





# from generators import ordered_sequence

# for












