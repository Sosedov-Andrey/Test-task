def sort_strings(lst):
    lst.sort(key=len)
    print("Отсортированный список по возрастанию длины:", lst)

    lst.sort(key=len, reverse=True)
    print("Отсортированный список по убыванию длины:", lst)
