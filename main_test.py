import main
import io
import sys
import re

# global rsum


def test_main_1():
    numbers = [[11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [31, 32, 33, 34, 35]]
    result = main.getSumRow(numbers)
    print(result)

    assert len(result) == 3
    assert result[0] == 65
    assert result[1] == 115
    assert result[2] == 165


def test_main_2():
    import random
    rownum = random.randint(5, 10)
    colnum = random.randint(3, 7)

    numbers = [[0] * colnum for i in range(rownum)]
    for i in range(rownum):
        for j in range(colnum):
            numbers[i][j] = random.randint(0, 10)
    result = main.getSumRow(numbers)
    print(result)

    assert len(result) == rownum
    for i in range(rownum):
        assert result[i] == sum(numbers[i])
