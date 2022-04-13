def minmax(n, k, a):
    count = 0
    start = 0
    end = 1
    arr = []
    # Calculating count array
    while (start <= end and end < n):
        if a[start] == a[end]:
            end+=1
            if end == n:
                arr.append(end - start)
        else:
            if end-start > 1:
                arr.append(end-start)
                start = end
                end += 1
            else:
                start +=1
                end+=1
    count = n - sum(arr)
    
    # print(count)
    # print(arr)
    # print(k)
    # if k!=0:
    while (k != 0 and len(arr) != 0):
        max_value = max(arr)
        max_index = arr.index(max_value)
        if max_value == 2:
            count += 2
            arr.pop(max_index)
        elif max_value == 3:
            count += 3
            arr.pop(max_index)
        elif max_value % 2 == 0:
            count+=1
            arr.pop(max_index)
            arr.append(max_value // 2)
            arr.append((max_value // 2) - 1)
        elif max_value % 2 != 0:
            count+=1
            arr.pop(max_index)
            arr.append(max_value // 2)
            arr.append(max_value // 2)
        k-=1
    for i in arr:
        count += (i * (i+1))//2
    return count

# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     n,k = [int(s) for s in input().split(" ")]
#     a = [int(s) for s in input().split(" ")]
#     ans = str(minmax(n,k,a))
#     print(ans)


# print(minmax(7,1,[1,2,2,3,4,4,4]))
# print(minmax(3,1,[1,2,3]))
# print(minmax(4,2,[3,3,3,1]))
# print(minmax(5,1,[1,1,1,1,1]))
print(minmax(4,1,[2,2,1,1]))