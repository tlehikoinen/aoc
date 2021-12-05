# Read lines from the file and store them into variable
with open('input.txt', 'r') as f:
    lines = f.readlines()

def considerBit(array, bit, msb):
    if len(array) == 1:
        return array[0]
    else:
        array_hold_ones = []
        array_hold_zeros = []
        for item in array:
            if item[bit] == '1':
                array_hold_ones.append(item)
            else:
                array_hold_zeros.append(item)

        if msb == 1:
            if len(array_hold_ones) < len(array_hold_zeros):
                return considerBit(array_hold_zeros, bit+1, msb)
            else:
                return considerBit(array_hold_ones, bit+1, msb)
        else:
            if len(array_hold_ones) < len(array_hold_zeros):
                return considerBit(array_hold_ones, bit+1, msb)
            else:
                return considerBit(array_hold_zeros, bit+1, msb)


def convertToDecimal(string):
    decimal = 0
    powerOf = len(string)-2
    for i in range(len(string)-1):
        decimal += (2**powerOf)*int(string[i])
        powerOf-=1
    return decimal

oxygen = considerBit(lines, 0, 1)
scrubber = considerBit(lines, 0, 0)

answer = convertToDecimal(oxygen) * convertToDecimal(scrubber)
print(answer)
