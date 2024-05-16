array = [1, 3, 5, 7, 9, 11]
target = 3
left = 0 #to search root node in binary search
right = len(array) - 1 #to search root node in binary search
while left <= right:
    mid = (left + right) // 2 #root node
    if array[mid] == target:
        #print(mid)
        rev_mid = len(array) - 1 - mid #reverse index for target

        break
    elif array[mid] < target:
        left = mid + 1 #move to right
    else:
        right = mid - 1# move to left
print("Target index is",mid,"Target reverse index is",rev_mid)