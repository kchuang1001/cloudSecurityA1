def hex_to_binary(hex_string):
    """
    Convert a hexadecimal string to a binary string.
    
    Args:
    hex_string: A string representing a hexadecimal number.
    
    Returns:
    A string representing the binary equivalent of the input hexadecimal number.
    """
    decimal_number = int(hex_string, 16)
    binary_string = bin(decimal_number)[2:]  # Removing '0b' prefix
    return binary_string.zfill(len(hex_string) * 4)  # Padding with zeros to ensure 4 bits per hex digit

def hex_to_binary2(hex_string):
    """
    Convert a hexadecimal string to a binary string.
    
    Args:
    hex_string: A string representing a hexadecimal number.
    
    Returns:
    A string representing the binary equivalent of the input hexadecimal number.
    """
    s = ''
    for i in range(0, len(hex_string), 2):
        decimal_number = int(hex_string[i:i+2], 16)
        binary_string = bin(decimal_number)[2:].zfill(8)  # Removing '0b' prefix
        s += binary_string
    return s.zfill(len(hex_string) * 4)  # Padding with zeros to ensure 4 bits per hex digit



def binary_to_hex(binary_string):
    """
    Convert a binary string to a hexadecimal string.
    
    Args:
    binary_string: A string representing a binary number.
    
    Returns:
    A string representing the hexadecimal equivalent of the input binary number.
    """
    decimal_number = int(binary_string, 2)
    hexadecimal_number = hex(decimal_number)
    # TODO
    if len(hexadecimal_number) < 10:
        hexadecimal_number = '0x' + '0' * (10-len(hexadecimal_number)) + hexadecimal_number[2:]
    return hexadecimal_number

def binary_xor(bin_str1, bin_str2):
    """
    Perform a bitwise XOR operation between two binary strings.
    
    Args:
    bin_str1: A string representing a binary number.
    bin_str2: A string representing a binary number (must be the same length as bin_str1).
    
    Returns:
    A string representing the result of the bitwise XOR operation.
    """
    l1, l2 = len(bin_str1), len(bin_str2)
    if l1 < l2:
        bin_str1, bin_str2 = bin_str2, bin_str1
        l1, l2 = l2, l1
    
    bin_str2 = (l1-l2) * '0' + bin_str2
        
        
        # raise ValueError("Binary strings must be of the same length")
    
    # Perform XOR operation for each corresponding bit and create the result string
    result = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(bin_str1, bin_str2))
    
    return result

def split_hex(hex_str):
    return [hex_str[i:i+2] for i in range(2,len(hex_str),2)]

def text_to_hex(str):
    """_summary_

    Args:
        str (str): a string consists of ascii characters

    Returns:
        str: a array consist of hex values of the given string
    """
    hex_s = []
    for c in str:
        hex_c = hex(ord(c))
        hex_s.append(hex_c[2:])

    return hex_s


def hex_to_matrix(arr):
    matrix = []
    for i in range(0, 16, 4):
        row = []
        for j in range(4):
            row.append(arr[i+j])        

        matrix.append(row)
    return matrix
