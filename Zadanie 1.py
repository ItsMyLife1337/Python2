#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    a = set("a, o, u, e, i, y, а, и, е, ё, у, о, ы, э, ю, я")
    n = int(input('Количество элементов множества?'))
    m = set()
    for i in range(n):
        m.add(input("введите элемент - "))
    b = a.intersection(m)
    print(m)
    print("Количество гласных ", len(b))
