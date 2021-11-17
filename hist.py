def distribute(list, k):
    # find the max and min
    result = [0]
    list = sorted(list)
    max = list[-1]
    min = list[0]
    intervalRange = (max - min) / k
    # calculate the range of each interval
    tempInterval = min + intervalRange
    for i in range(len(list)):
        if list[i] <= tempInterval:
            result[-1] += 1
        else:
            tempInterval += intervalRange
            result.append(1)
    print(result)
    return result


if __name__ == '__main__':
    assert distribute([1.25, 1, 2, 1.75], 2) == [2, 2]
    assert distribute([1.25, 1, 4, 1.75], 2) == [3, 1]