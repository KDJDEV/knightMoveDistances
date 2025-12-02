"""
Testing utilities for knight_distances module.
Includes BFS verification, visualization, and comprehensive testing functions.
"""
import matplotlib.pyplot as plt
from collections import deque
from knight_distance import knight_distance


def bfs_dist(R, C, Gr, Gc):
    """
    Calculate true knight distances using BFS.
    
    Args:
        R: Number of rows on the board
        C: Number of columns on the board
        Gr: Starting row (1-indexed)
        Gc: Starting column (1-indexed)
    
    Returns:
        2D list of distances from start position
    """
    dist = [[None]*(C+1) for _ in range(R+1)]
    moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
    q = deque()
    q.append((Gr, Gc))
    dist[Gr][Gc] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 1 <= nr <= R and 1 <= nc <= C and dist[nr][nc] is None:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist


def show_calc_board(R, C, Gr, Gc):
    """
    Display a board showing knight_distance distances from starting position.
    
    Args:
        R: Number of rows on the board
        C: Number of columns on the board
        Gr: Starting row (1-indexed)
        Gc: Starting column (1-indexed)
    """
    fig, ax = plt.subplots(figsize=(C/2, R/2))
    ax.set_xticks(range(C+1))
    ax.set_yticks(range(R+1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    ax.invert_yaxis()

    for r in range(1, R+1):
        for c in range(1, C+1):
            val = knight_distance(R, C, Gr, Gc, r, c)
            ax.text(c-0.5, r-0.5, str(val), ha='center', va='center')

    plt.show()


def show_side_by_side(R, C, Gr, Gc):
    """
    Display side-by-side comparison of knight_distance vs BFS results.
    Mismatches are highlighted in red.
    
    Args:
        R: Number of rows on the board
        C: Number of columns on the board
        Gr: Starting row (1-indexed)
        Gc: Starting column (1-indexed)
    """
    bfs = bfs_dist(R, C, Gr, Gc)

    fig, axs = plt.subplots(1, 2, figsize=(C/1.5, R/2))

    for ax, title, getter in [
        (axs[0], "calc()", lambda r,c: knight_distance(R,C,Gr,Gc,r,c)),
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
                calc_val = knight_distance(R,C,Gr,Gc,r,c)
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
    """
    Print all positions where knight_distance differs from BFS.
    
    Args:
        R: Number of rows on the board
        C: Number of columns on the board
        Gr: Starting row (1-indexed)
        Gc: Starting column (1-indexed)
    """
    bfs = bfs_dist(R, C, Gr, Gc)
    mistakes = []

    for r in range(1, R+1):
        for c in range(1, C+1):
            calc_val = knight_distance(R, C, Gr, Gc, r, c)
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


def run_comprehensive_test(maxR=15, maxC=15):
    """
    Run comprehensive testing across all board sizes and starting positions.
    
    Args:
        maxR: Maximum number of rows to test
        maxC: Maximum number of columns to test
    """
    for R in range(1, maxR+1):
        for C in range(1, maxC+1):
            for Gr in range(1, R+1):
                for Gc in range(1, C+1):
                    print_mistakes(R, C, Gr, Gc)


if __name__ == "__main__":
    # Example usage - uncomment to run specific tests
    
    # Visualization examples
    # show_side_by_side(4, 4, 2, 2)
    # show_side_by_side(10, 10, 10, 10)
    # show_side_by_side(3, 4, 2, 2)
    
    # Individual test cases
    # print_mistakes(12, 12, 1, 1)
    # print_mistakes(3, 4, 1, 1)
    # print_mistakes(4, 4, 2, 2)
    
    # Test specific board dimensions
    # x = 3
    # y = 3
    # for Gr in range(1, x+1):
    #     for Gc in range(1, y+1):
    #         print_mistakes(x, y, Gr, Gc)
    
    # Comprehensive test - no output means successful tests
    run_comprehensive_test(maxR=15, maxC=15)