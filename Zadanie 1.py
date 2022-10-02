#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    strock = input("Введите строку: ").lower()
    a = set(strock)
    u = set("aeiouyаоуыэеёиюя")

    count = 0
    for i in strock:
        if i in u:
            count += 1

    print(count)
