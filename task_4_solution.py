import math
def solution(a, b):
    ws_count = 0
    for i in range(a, b+1):
        root = math.sqrt(i)
        if i == int(root+0.5)**2:
            ws_count += 1
            
    return ws_count
        

print(solution(4, 17))
"""
An integer P is a whole square if it is a square of some integer Q; if P = Q.
Write a function:
int solution(int A, int B);
that, given two integers A and B, returns the number of whole squares within the interval [A..B] (both ends included).
For example, given A = 4 and B = 17, the function should return 3, because there are three squares of integers in the interval [4..17], namely 4 = 2 square 2, 9 = 3square2 and 16 = 4square2.
Assume that:
A and B are integers within the range [−2,147,483,648.. 2,147,483,647];
A ≤ B.

Complexity:
expected worst-case time complexity is O(sqrt(abs(B)));
expected worst-case space complexity is O(1).
"""
