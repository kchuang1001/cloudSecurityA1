def mix_columns(state):
    """
    Perform the MixColumns operation on the state matrix.

    Args:
    state: The state matrix as a list of lists.

    Returns:
    The state matrix after the MixColumns operation.
    """
    # The fixed MixColumns matrix
    mix_columns_matrix = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]

    # Initialize the resultant matrix with zeros
    result = [[0] * 4 for _ in range(4)]

    # Perform matrix multiplication
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] ^= gf_multiply(mix_columns_matrix[i][k], state[k][j])

    return result

def gf_multiply(a, b):
    """
    Multiply two numbers in the Galois Field (GF(2^8)).

    Args:
    a, b: The two numbers to multiply.

    Returns:
    The result of the multiplication.
    """
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        # If the most significant bit of a is set, left shift and XOR with the irreducible polynomial
        if a & 0x80:
            a = (a << 1) ^ 0x1b  # 0x1b is the irreducible polynomial x^8 + x^4 + x^3 + x + 1
        else:
            a <<= 1
        b >>= 1
    return result