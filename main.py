rsum = []


def main():
    numbers = [[11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [31, 32, 33, 34, 35]]
    global rsum
    ##################################################
    # Comlete your code here
    ##################################################
    for i in range(len(numbers)):
        total = 0
        for j in range(len(numbers[i])):
            total += numbers[i][j]
        rsum.append(total)
        # main.rsum.append(total)
    print(rsum)
    # print(main.rsum)


if __name__ == '__main__':
    main()
