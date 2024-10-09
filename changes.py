def getMinimumChanges(fileSize, minSize):
    needed = []
    extra = []
    
    for i in range(len(fileSize)):
        if fileSize[i] < minSize[i]:
            needed.append(minSize[i] - fileSize[i])
        else:
            extra.append(fileSize[i] - minSize[i])
    
    # Sort needed in ascending and extra in descending order
    needed.sort()
    extra.sort(reverse=True)
    
    change_count = 0
    extra_index = 0
    
    for need in needed:
        while extra_index < len(extra) and extra[extra_index] == 0:
            extra_index += 1
        
        if extra_index == len(extra):
            return -1
        
        if extra[extra_index] >= need:
            extra[extra_index] -= need
            change_count += 1
        else:
            return -1
    
    # Add the number of changes made when reducing file sizes to match the minimum size
    change_count += sum(extra)
    
    return change_count

# Example test case
fileSize = [5, 2, 3, 1, 5, 9]
minSize = [5, 1, 5, 6, 1, 5]
result = getMinimumChanges(fileSize, minSize)
print(result)  # Expected output: 4
