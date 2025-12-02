Knight's move distance calculator module.
Calculates the minimum number of moves for a knight to reach any position on a chessboard of arbitrary size in constant time. Also returns an impossible code if a position is unreachable.

The solution is mathematical rather than relying on a BFS, so it runs in constant time. In other words, it should be faster than pretty much any algorithm out there. It has been tested on all possible boards up to 15x15 (including non-square boards), but it is theoretically justified and should work on all possible board sizes.

This problem was inspired by the following Gregory the Grasshopper problem on Kattis:
https://open.kattis.com/problems/grasshopper

Example with 9x9 board with knight starting in the center:

<img width="449" height="449" alt="Figure_1" src="https://github.com/user-attachments/assets/bdc57c52-f0d5-4784-af74-bd36266380fc" />

Example with 25x25 board with knight starting in the top left:

<img width="798" height="686" alt="Figure_2" src="https://github.com/user-attachments/assets/33041179-ec1d-4281-b2b9-6d753ea822eb" />
