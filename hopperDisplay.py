import matplotlib.pyplot as plt
import math
from collections import deque


def knight_calc(R, C, Gr, Gc, Lr, Lc):
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

def show_calc_board(R, C, Gr, Gc):
    fig, ax = plt.subplots(figsize=(C/2, R/2))
    ax.set_xticks(range(C+1))
    ax.set_yticks(range(R+1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    ax.invert_yaxis()

    for r in range(1, R+1):
        for c in range(1, C+1):
            val = knight_calc(R, C, Gr, Gc, r, c)
            ax.text(c-0.5, r-0.5, str(val), ha='center', va='center')

    plt.show()

def bfs_dist(R, C, Gr, Gc):
    dist = [[None]*(C+1) for _ in range(R+1)]
    moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
    q = deque()
    q.append((Gr, Gc))
    dist[Gr][Gc] = 0
    while q:
        r,c = q.popleft()
        for dr,dc in moves:
            nr,nc = r+dr, c+dc
            if 1 <= nr <= R and 1 <= nc <= C and dist[nr][nc] is None:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
    return dist

def show_side_by_side(R, C, Gr, Gc):
    bfs = bfs_dist(R, C, Gr, Gc)

    fig, axs = plt.subplots(1, 2, figsize=(C/1.5, R/2))

    for ax, title, getter in [
        (axs[0], "calc()", lambda r,c: knight_calc(R,C,Gr,Gc,r,c)),
        (axs[1], "BFS true distance", lambda r,c: bfs[r][c] if bfs[r][c] is not None else "impossible")
    ]:
        ax.set_xticks(range(C+1))
        ax.set_yticks(range(R+1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(True)
        ax.invert_yaxis()
        ax.set_title(title)

        for r in range(1, R+1):
            for c in range(1, C+1):
                val = getter(r,c)
                calc_val = knight_calc(R,C,Gr,Gc,r,c)
                bfs_val = bfs[r][c]

                mismatch = False
                if calc_val == "impossible" and bfs_val is None:
                    mismatch = False
                elif calc_val == "impossible" and bfs_val is not None:
                    mismatch = True
                elif calc_val != "impossible" and bfs_val is None:
                    mismatch = True
                elif isinstance(calc_val, int) and isinstance(bfs_val, int) and calc_val != bfs_val:
                    mismatch = True

                color = "red" if mismatch else "black"
                ax.text(c-0.5, r-0.5, str(val), ha='center', va='center', fontsize=6, color=color)

    plt.tight_layout()
    plt.show()

def print_mistakes(R, C, Gr, Gc):
    bfs = bfs_dist(R, C, Gr, Gc)

    mistakes = []

    for r in range(1, R+1):
        for c in range(1, C+1):
            calc_val = knight_calc(R, C, Gr, Gc, r, c)
            bfs_val = bfs[r][c]

            mismatch = False
            if calc_val == "impossible" and bfs_val is None:
                mismatch = False
            elif calc_val == "impossible" and bfs_val is not None:
                mismatch = True
            elif calc_val != "impossible" and bfs_val is None:
                mismatch = True
            elif isinstance(calc_val, int) and isinstance(bfs_val, int) and calc_val != bfs_val:
                mismatch = True

            if mismatch:
                mistakes.append((r, c, calc_val, bfs_val))

   
    if mistakes:
        print(f"\n=== Mistakes for board {R}×{C} from start ({Gr}, {Gc}) ===")
        for (r, c, calc_val, bfs_val) in mistakes:
            print(f"Cell ({r},{c}): calc={calc_val}, bfs={bfs_val}")


#failure cases




#old:
#show_side_by_side(4, 4, 2, 2)
#any n by n board but only one square off
#show_side_by_side(10, 10, 10, 10)
#show_side_by_side(4, 4, 1, 1)
#show_side_by_side(3, 4, 1, 1)
#show_side_by_side(3, 10, 2, 4)
#show_side_by_side(3, 15, 2, 8)
#show_side_by_side(3, 4, 2, 1)
#show_side_by_side(3, 4, 2, 2)

# print_mistakes(12, 12, 1, 1)
# print_mistakes(3, 4, 1, 1)
# print_mistakes(4, 4, 1, 1)
# print_mistakes(7, 7, 1, 1)
# print_mistakes(4, 4, 2, 2)
# print_mistakes(3, 4, 2, 1)
#print_mistakes(3, 4, 2, 2)

# x = 3
# y = 3
# for Gr in range(1, x+1):
#     for Gc in range(1, y+1):
#         print_mistakes(x, y, Gr, Gc)

maxR = 15
maxC = 15
for R in range(1, maxR+1):
    for C in range(1, maxC+1):
        for Gr in range(1, R+1):
            for Gc in range(1, C+1):
                print_mistakes(R, C, Gr, Gc)

