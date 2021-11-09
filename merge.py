def merge(a, b):
    if isinstance(a, tuple):
        ans = list(a[:])
    else:
        ans = a.copy()

    index = 0
    for i in range(0, len(b)):
        while index < len(a):
            if b[i] <= a[index]:
                ans.insert(index + i, b[i])
                break
            else:
                index += 1
    if isinstance(a, tuple):
        return tuple(ans)

    else:
        return ans

if __name__ == '__main__':
        assert merge ([1 , 2 , 7], [3]) == [1 , 2 , 3 , 7]
        assert merge (( 3 , 15 ) , (7 , 8 ) ) == (3 , 7 , 8 , 15 )

        print(merge ([1 , 2 , 7], [3]))
        print(merge (( 3 , 15 ) , (7 , 8 ) ))