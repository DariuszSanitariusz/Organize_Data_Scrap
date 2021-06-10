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
        return a

    def quicksort(self):
        a = self.to_sort
        a = [a]
        a_length = len(a[0])
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
            if len(a) == a_length:
                in_progress = False
        return [num[0] for num in a]

    def merge_sort(self):
        a = self.to_sort
        a = [a]
        a_length = len(a[0])
        while len(a) != a_length:
            result = []
            for n in a:
                b = []
                split_point = (len(n) // 2)
                for i in range(split_point):
                    b.append(n[i])
                    n.pop(i)
                result.append(b)
                result.append(n)
            a = [x for x in result if len(x) != 0]

        while len(a) != 1:
            even_index = list(range(0, len(a), 2))
            odd_index = list(range(1, len(a), 2))
            index_pairs = list(zip(even_index, odd_index))
            if len(even_index) != len(odd_index):
                index_pairs.append((even_index[-1], None))

            for i, u in index_pairs:
                result = []
                if not u:
                    break
                while len(a[i]) or len(a[u]):
                    try:
                        if a[i][0] < a[u][0]:
                            result.append(a[i].pop(0))
                        else:
                            result.append(a[u].pop(0))
                    except IndexError:
                        if len(a[i]) == 0:
                            result.extend(a[u])
                            a[u].clear()
                        elif len(a[u]) == 0:
                            result.extend(a[i])
                            a[i].clear()
                a[i] = result
            a = [x for x in a[::2]]
        return [num for num in a[0]]
