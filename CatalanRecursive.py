count = 20
resultArr = [0.0] * count # It is used to prevent calculating values more than once

def totalTree(n):
    if n < 2:
        return 1
    else:
        leftLeaf = 0
        rightLeaf = 0
        sum = 0;
        for i in range(1, n+1):
            if resultArr[i - 1] == 0:
                resultArr[i - 1] = totalTree(i - 1)
            leftLeaf = resultArr[i - 1]
            if resultArr[n - i] == 0:
                resultArr[n - i] = totalTree(n - i)
            rightLeaf = resultArr[n - i]
            sum = sum + (leftLeaf * rightLeaf)
    return sum

print(totalTree(20))
