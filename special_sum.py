def calculate_special_sum(n):
    sum = 0
    for i in range(n):
        sum += (i)*(i)*(i+1)
    return sum
if __name__ == '__main__':
    assert calculate_special_sum(3) == 14