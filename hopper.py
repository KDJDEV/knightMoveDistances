import math
import sys

for line in sys.stdin:
    R, C, Gr, Gc, Lr, Lc = map(int, line.split())
    def calc():
        i = abs(Lr - Gr)
        j = abs(Lc - Gc)

        if (Lr > R or Lc > C or Lr < 1 or Lc < 1):
            return "impossible"
        if (R == 1 or C == 1) and (Gr, Gc) != (Lr, Lc):
            return "impossible"
        if (C == 2):
            if (not (i % 4 == 0 and j == 0) and not (i % 4 == 2 and j == 1)):
                return "impossible"
        if (R == 2):
            if (not (j % 4 == 0 and i == 0) and not (j % 4 == 2 and i == 1)):
                return "impossible"
        if (R == 3 and C == 3 and Gr == 2 and Gc == 2 and (Lr, Lc) != (2, 2)):
            return "impossible"
        if (R == 3 and C == 3 and (Gr, Gc) != (2, 2) and (Lr, Lc) == (2, 2)):
            return "impossible"
        
        if (i + j == 1):
            return 3
        if (i == j == 2):
            return 4
        m = math.ceil(max(i/2, j/2, (i+j)/3))
        return m + (m + i + j) % 2
    
    print(calc())