#если не важно сохранить порядок
def func_uniq(lst: list):
    return list(set(lst))


#если важно сохранить порядок
def func_uniq_ordered(lst: list):
    seen = set()
    uniq = []
    for i in lst:
        if i not in seen:
            seen.add(i)
            uniq.append(i)
    return uniq


