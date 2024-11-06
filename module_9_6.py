# Домашнее задание по теме "Генераторы"

def all_variants(text):
    s = len(text)
    for j in range(1, s + 1):
        for k in range(s - j + 1):
            print(k)
            yield text[k:k + j]

a = all_variants("abc")
for i in a:
    print(i)
