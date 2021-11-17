def compress(lis):
    counts = {}
    homework = []
    for i in lis:
        if counts.get(i) is None:
            counts[i] = 1

        else:
            counts[i] += 1
    for j in counts.items():
        homework.append(j)
    return homework

if __name__ == '__main__':
    expected_sorted = [(1, 2), (2, 1), (3, 1)]
    actual_sorted = sorted(compress([1, 2, 1, 3]))
    assert expected_sorted == actual_sorted