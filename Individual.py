#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    # Определим универсальное множество
    u = set("abcdefghiklmnopqrstuvwxyz")

    a = {"b", "e", "f", "k", "t"}
    b = {"f", "i", "j", "p", "y"}
    c = {"j", "k", "l", "y"}
    d = {"i", "j", "s", "t", "u", "y", "z"}

    x = (a.intersection(c)).union(b.intersection(c))
    print(f"x = {x}")

    # Найдём дополнения множеств
    nb = u.difference(b)

    y = (a.difference(nb)).union(d.difference(c))
    print(f"y = {y}")
