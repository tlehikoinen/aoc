with open('input.txt', 'r') as f:
    data = f.read().strip()

hexa = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
        }  

def convert_hex_bin(data):
    string = ''
    for d in data: 
        string += hexa[d]
    string.split()
    return string

def convert_bin_dec(bin_str, msb_first=True):
    decimal = 0
    if msb_first == True:
        for i in range(len(bin_str)):
            decimal += ((2**(len(bin_str)-i-1))*int(bin_str[i]))
    elif msb_first == False:
        for i in range(len(bin_str)):
            decimal += ((2**i)*int(bin_str[i]))
    return decimal


def read_packet(index):

    packet_version = convert_bin_dec(binary[index:index+3])
    type_id = convert_bin_dec(binary[index+3:index+6])
    index += 6

    if type_id == 4: # Literal version
        new_bin = ''
        keep_reading = True
        while(keep_reading):
            seq = binary[index:(index+5)]
            index +=5
            if int(seq[0]) == 0: # Stop reading
                keep_reading = False
            new_bin += seq[1:]
        new_dec = convert_bin_dec(new_bin)
        #print(f' Literal value {new_dec}')

    else: # Operator versions
        if int(binary[index]) == 0:
            length = convert_bin_dec(binary[index+1:index+16]) + index + 16
            index += 16
            while (index < length):
                index, pv = read_packet(index)
                packet_version += pv
        else:
            sub = convert_bin_dec(binary[index+1:index+12])
            index += 12
            for _ in range(sub):
                index, pv = read_packet(index)
                packet_version += pv

    return index, packet_version

# Part 1
# Convert hex to bin
binary = convert_hex_bin(data)
index, packet_version = read_packet(0)
print(f'Part 1 result {packet_version}')




    
    





















