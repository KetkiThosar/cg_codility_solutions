from itertools import permutations


class Solution(object):
    div = 1000000

    def __init__(self, A, B):
        self.A = A
        self.B = list(map(lambda x: x/Solution.div, B))

    @staticmethod
    def mul(item):
        return item[0] * item[1]

    def get_real_number_array(self):
        return [float(sum(items)) for items in zip(self.A, self.B)]

    def get_multiplicative_pairs(self):
        all_indices = list(permutations(range(len(self.A)), 2))
        real_num_array = self.get_real_number_array()
        pairs = filter(lambda t: t[0] < t[1], all_indices)
        selected_pairs = filter(lambda t: Solution.mul((real_num_array[t[0]], real_num_array[t[1]]))
                                          >= sum((real_num_array[t[0]], real_num_array[t[1]])), pairs)

        return len(selected_pairs)


a = Solution([0, 1, 2, 2, 3, 5], [5e5, 5e5, 0, 0, 0, 2e4])

#print(a.get_real_number_array())
print(a.get_multiplicative_pairs())
#8

"""
Zero-indexed arrays A and B consisting of N non-negative integers are given. Together, they represent N real numbers, denoted as C[0], ..., C[N−1]. Elements of A represent the integer parts and the corresponding elements of B (divided by 1,000,000) represent the fractional parts of the elements of C. More formally, A[I] and B[I] represent C[I] = A[I] + B[I] / 1,000,000.

For example, consider the following arrays A and B:
  A[0] = 0	B[0] = 500,000
  A[1] = 1	B[1] = 500,000
  A[2] = 2	B[2] = 0
  A[3] = 2  B[3] = 0
  A[4] = 3	B[4] = 0
  A[5] = 5	B[5] = 20,000
  
  They represent the following real numbers:
  C[0] = 0.5
  C[1] = 1.5
  C[2] = 2.0
  C[3] = 2.0
  C[4] = 3.0
  C[5] = 5.02
  
  A pair of indices (P, Q) is multiplicative  if 0 ≤ P < Q < N and C[P] * C[Q] ≥ C[P] + C[Q].
  
  The above arrays yield the following multiplicative pairs:
	1. (1, 4), because 1.5 * 3.0 = 4.5 ≥ 4.5 = 1.5 + 3.0,
	2. (1, 5), because 1.5 * 5.02 = 7.53 ≥ 6.52 = 1.5 + 5.02,
	3. (1, 5), because 1.5 * 5.02 = 7.53 ≥ 6.52 = 1.5 + 5.02,
	4. (2, 3), because 2.0 * 2.0 = 4.0 ≥ 4.0 = 2.0 + 2.0,
	5. (2, 4) and (3, 4), because 2.0 * 3.0 = 6.0 ≥ 5.0 = 2.0 + 3.0.
	6. (2, 5) and (3, 5), because 2.0 * 5.02 = 10.04 ≥ 7.02 = 2.0 + 5.02.
	7. (4, 5), because 3.0 * 5.02 = 15.06 ≥ 8.02 = 3.0 + 5.02.
	
	Write a function: 
	class Solution { public int solution(int[] A, int[] B); }
	
	that, given zero-indexed arrays A and B, each containing N non-negative integers, returns the number of multiplicative pairs of indices.
	
	If the number of multiplicative pairs is greater than 1,000,000,000, the function should return 1,000,000,000.
	
	For example, given:
	
  A[0] = 0	B[0] = 500,000
  A[1] = 1	B[1] = 500,000
  A[2] = 2	B[2] = 0
  A[3] = 2	B[3] = 0
  A[4] = 3	B[4] = 0
  A[5] = 5	B[5] = 20,000
  
  the function should return 8, as explained above.
  
  Assume that : 
  1. N is an integer within the range [0..100,000];
  2. each element of array A is an integer within the range [0..1,000]
  3. each element of array B is an integer within the range [0..999,999]
  4. real numbers created from arrays are sorted in non-decreasing order.
  
  Complexity
  1. expected worst-case time complexity is O(N);
  2. expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
  
  Elements of input arrays can be modified.
"""
