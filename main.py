from aes import aes_round, print_matrix, aes, transpose
from bin_hex_converter import text_to_hex, hex_to_matrix

def write_latex_matrix(matrix):
    print('\\begin{pmatrix}')
    for i in range(4):
        for j in range(4):
            print(matrix[i][j] + ('&' if j < 3 else '\\\\'), end= ' ') 
        print()
    print('\\end{pmatrix}')


if __name__ == "__main__":
    k = 'keechewhuang3808292'
    plain_text = 's3808292@student.rmit.edu.au'

    k_hex = text_to_hex(k)
    p_hex = text_to_hex(plain_text)

    k_matrix = hex_to_matrix(k_hex[:16])
    p_matrix = hex_to_matrix(p_hex[:16])
   
    write_latex_matrix(transpose(k_matrix))
    write_latex_matrix(transpose(p_matrix))

    aes(k, plain_text)


