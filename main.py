import random


def getSumRow(numbers):
    """
    ################################################## 
     # Comlete your code here
    ################################################## 
    """
    return result


def main():
    # Test 1
    numbers = [[11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [31, 32, 33, 34, 35]]
    result = getSumRow(numbers)
    print(result)

    # Test 2
    rownum = 5
    colnum = 10

    numbers = [[0] * colnum for i in range(rownum)]
    for i in range(rownum):
        for j in range(colnum):
            numbers[i][j] = random.randint(0, 10)

    print(numbers)
    result = getSumRow(numbers)
    print(result)


if __name__ == '__main__':
    main()
