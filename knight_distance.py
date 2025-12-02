"""
Knight's move distance calculator module.
Calculates the minimum number of moves for a knight to reach any position on a chessboard of arbitrary size in constant time.
"""

# Copyright (c) 2025 Kyle Dagman
# Licensed under the MIT License. See LICENSE file for details.

import math

def knight_distance(R, C, Gr, Gc, Lr, Lc):
    """
    Calculate the minimum number of knight moves from (Gr, Gc) to (Lr, Lc) on an RxC board.
    
    Args:
        R: Number of rows on the board
        C: Number of columns on the board
        Gr: Starting row (1-indexed)
        Gc: Starting column (1-indexed)
        Lr: Target row (1-indexed)
        Lc: Target column (1-indexed)
    
    Returns:
        int: Minimum number of moves, or "impossible" if unreachable
    """
    i = abs(Lr - Gr)
    j = abs(Lc - Gc)

    # Out of bounds
    if not (1 <= Lr <= R and 1 <= Lc <= C):
        return "impossible"

    # Single row/column is impossible
    if (R == 1 or C == 1) and (Gr, Gc) != (Lr, Lc):
        return "impossible"

    # 2-wide impossible cases
    if C == 2 and not ((i % 4 == 0 and j == 0) or (i % 4 == 2 and j == 1)):
        return "impossible"
    if R == 2 and not ((j % 4 == 0 and i == 0) or (j % 4 == 2 and i == 1)):
        return "impossible"

    # 3x3 center is impossible
    if R == 3 and C == 3 and (Gr == 2 and Gc == 2) != (Lr == 2 and Lc == 2):
        return "impossible"

    # Corner diagonal edge cases
    if i == 1 and j == 1:
        if (Gr in (1, R) and Gc in (1, C)) and (Lr in (2, R-1) and Lc in (2, C-1)):
            return 4
        if (Gr in (2, R-1) and Gc in (2, C-1)) and (Lr in (1, R) and Lc in (1, C)):
            return 4

    # 4xN and Nx4 corner to corner edge cases
    if (Gr in (1, R) and Gc in (1, C)) and (Lr in (1, R) and Lc in (1, C)):
        if i == 3 and j == 0 and R == 4:
            return 5
        if i == 0 and j == 3 and C == 4:
            return 5

    # 3xN and Nx3 2 from the start edge cases
    if i == 0 and j == 2 and R == 3 and Gr == 2:
        return 4
    if i == 2 and j == 0 and C == 3 and Gc == 2:
        return 4

    # 3x4 and 4x3 center start case
    if ((R, C) == (3, 4) and {(Gr, Gc), (Lr, Lc)} == {(2, 2), (2, 3)}) or \
       ((R, C) == (4, 3) and {(Gr, Gc), (Lr, Lc)} == {(2, 2), (3, 2)}):
        return 5

    if (i + j == 1):
        return 3
    if (i == j == 2):
        return 4
    m = math.ceil(max(i/2, j/2, (i+j)/3))
    return m + (m + i + j) % 2