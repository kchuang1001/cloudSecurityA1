import math
from bin_hex_converter import \
    hex_to_binary2, \
    binary_to_hex, \
    binary_xor, \
    split_hex, \
    text_to_hex, \
    hex_to_matrix 

from matrix_multiplication import mix_columns

from constants import Sbox, round_constants

def circular_byte_left_shift(row):
    return row[1:4] + [row[0]]


def hex_to_num(n):
    return int(n, 16)


def substitute_bytes(byte):
    x, y = byte
    x, y = hex_to_num(x), hex_to_num(y)

    return Sbox[x*16+y]


def g_func(row, round_constant):
    row = circular_byte_left_shift(row)
    row_s_box = [substitute_bytes(byte) for byte in row]
    row_s_box[0] = hex(int(row_s_box[0], 16) ^ round_constant)[2:]

    return row_s_box


def hex_xor(arr1, arr2):
    h1, h2 = ''.join(arr1), ''.join(arr2)
    b1, b2 = hex_to_binary2(h1), hex_to_binary2(h2)
    return split_hex(binary_to_hex(binary_xor(b1, b2)))


k = 'Thats my Kung Fu'
hex_s = text_to_hex(k)
matrix = hex_to_matrix(hex_s)


def roundKey(matrix, round):
    g = g_func(matrix[3], round_constants[round-1])

    w4 = hex_xor(g, matrix[0])
    w5 = hex_xor(w4, matrix[1])
    w6 = hex_xor(w5, matrix[2])
    w7 = hex_xor(w6, matrix[3])

    return [w4, w5, w6, w7]

def transpose(matrix):
    return [list(t) for t in zip(*matrix)]

def matrix_substitute(matrix):
    sub = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sub[i][j] = substitute_bytes(matrix[i][j])
    return sub

def shift_row(row, shift):
    return row[shift:] + row[:shift] 


curr = matrix

plain_text = "Two One Nine Two"
matrix_text = hex_to_matrix(text_to_hex(plain_text))

def print_matrix(matrix):
    for i in range(4):
        print(matrix[i])
    print()

def aes_round(matrix, round_key):
  
    # substitution bytes
    matrix_sbox = matrix_substitute(matrix)
    print("Substitution bytes")
    write_latex_matrix(matrix_sbox)
    # print_matrix(matrix_sbox)
    # shift row
    for i in range(4):
        matrix_sbox[i] = shift_row(matrix_sbox[i], i)

    print("Shift row")
    write_latex_matrix(matrix_sbox)

    # mix column
    matrix_sbox_int = [[hex_to_num(matrix_sbox[i][j]) for j in range(4)] for i in range(4)]
    mixed = mix_columns(matrix_sbox_int)
    result = [[hex(mixed[i][j])[-2:].replace('x', '0') for j in range(4)] for i in range(4)]

    print("Mix Columns")
    write_latex_matrix([
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ])
    write_latex_matrix(result)
    round_key = transpose(round_key)
    # add round key
    result = [hex_xor(result[i], round_key[i]) for i in range(len(result))]
    return result

def write_latex_matrix(matrix):
    print('\\begin{pmatrix}', end= ' ')
    for i in range(4):
        for j in range(4):
            print(str(matrix[i][j]) + ('&' if j < 3 else '\\\\'), end= ' ') 
    print('\\end{pmatrix}')


def aes(key, plain_text):
    key_matrix = hex_to_matrix(text_to_hex(key))
    plain_text_matrix = hex_to_matrix(text_to_hex(plain_text))

    key_matrix_trans, plain_text_matrix = transpose(key_matrix), transpose(plain_text_matrix)
    curr_key = key_matrix

    # add round 0 key
    curr = [hex_xor(plain_text_matrix[i], key_matrix_trans[i]) for i in range(len(plain_text_matrix))]
    print("First Transformation:")
    write_latex_matrix(curr)

    for i in range(1, 3):
        print(f"Round {i}:")
        curr_key = roundKey(curr_key, i)
        print("Curr Key", curr_key)
        curr = aes_round(curr, curr_key)
        
        print_matrix(curr)

if __name__ == "__main__":
    aes(k, plain_text)
