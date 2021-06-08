import random


class SomeSort:

    def __init__(self, to_sort):
        self.to_sort = to_sort

    def bubble_sort(self):
        a = self.to_sort
        in_progress = True
        while in_progress:
            in_progress = False
            for i, n in enumerate(a):
                if i != len(a) - 1:
                    if a[i] > a[i + 1]:
                        in_progress = True
                        b = a.pop(i + 1)
                        a.insert(i, b)

    def quicksort(self):
        a = self.to_sort
        a = [a]
        in_progress = True
        while in_progress:
            result = []
            for num in a:
                pivot = random.choice(num)
                result.append([x for x in num if x < pivot])
                result.append([pivot])
                result.append([x for x in num if x > pivot])
                num.clear()
            a.extend(result)
            a = list(filter(lambda x: x != [], a))

    def merge_sort(self):
        a = self.to_sort


class MergeSort:
    """
    merge sort class
    separate methods for splitting and merging process
    """

    def __init__(self, list_to_sort):
        self.list_to_sort = list_to_sort
        self.list_split = []
        self.list_merge = []

    def __str__(self):
        write = " ".join(str(self.list_merge))
        return write

    def split(self):
        """
        splitting list following merge sort diagram strictly
        """
        self.list_split.append(self.list_to_sort)
        while len(self.list_split[0]) > 1:
            result = []
            for n in range(len(self.list_split), 0, -1):
                b = self.list_split.pop()
                stop = (len(b) // 2) + 1
                c = []
                for i in range(0, stop):
                    c.append(b.pop())
                result.append(c)
                if b:
                    result.append(b)
            self.list_split = result

    def merge(self):
        """
        merging list following merge sort diagram strictly
        """
        merge = self.list_split
        while len(merge) != 1:
            result = []
            for i in range(len(merge)):
                compare_result = []
                if i % 2 == 0:
                    while len(merge[i]) != 0:
                        try:
                            # comparing first element of lists
                            first_list_element = merge[i][0]
                            second_list_element = merge[i+1][0]
                            if first_list_element <= second_list_element:
                                compare_result.append(first_list_element)
                                del merge[i][0]
                            else:
                                compare_result.append(second_list_element)
                                del merge[i+1][0]
                        except IndexError:
                            if len(merge[i]) != 0:
                                compare_result.extend(merge[i])
                                merge[i].clear()
                            elif len(merge[i+1]) != 0:
                                compare_result.extend((merge[i+1]))
                                merge[i+1].clear()
                    # last element case
                    if i != len(merge)-1:
                        compare_result.extend(merge[i+1])
                        merge[i+1].clear()
                    result.append(compare_result)
            merge = result
        # saving outcome
        self.list_merge = merge[0]


example_list = [5, 8, 2, 9, 3, 4, 1, 6, 0]
print(quicksort(example_list))
