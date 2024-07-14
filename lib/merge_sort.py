def merge(l, r):
    m = []
    i, j = 0, 0
    while ((i < len(l)) and (j < len(r))):
        if l[i] <= r[j]:
            m.append(l[i])
            i += 1
        else:
            m.append(r[j])
            j += 1
    if i >= len(l):
        m.extend(r[j:])
    else:
        m.extend(l[i:])
    return m

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    l = merge_sort(array[:mid])
    r = merge_sort(array[mid:])
    return merge(l, r)

if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sorted_data = merge_sort(data)
    print(f"{data} → {sorted_data}")
