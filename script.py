n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten (lists):
    result = []
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            result.append(lists[i][j])
    return result
print flatten(n)
