def count_elements(*lists):
    elements = set(lists[0])
    for lst in lists[1:]:
        elements.intersection_update(lst)
    return len(elements)


list1 = [2, 1, 4, 3, 5]
list2 = [3, 1, 3, 5, 4]
list3 = [3, 2, 3, 4, 7]
elements_count = count_elements(list1, list2, list3)
print("Кол-во общих элементов: ", elements_count)
