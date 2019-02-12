def solution(arr):
    index, length = 0, 1
    while arr[index] != -1:
        index = arr[index]
        length += 1
        
    return length

    
arr = [1,4,-1,3,2]
#Ans -> 4
print(solution(arr))
"""
A non-empty zero indexed array A consisting of N integers is given.

Array A represents a linked list. A list is constructed from this array as follows:

the first node (the head) is located at index 0;
the value of a node located at index K is A[K];
if the value of a node is -1 then it is the last node of the list;
otherwise, the successor of the node located at index K is located at index A[K] (you can assume that A[K] is a valid index, that is 0<=A[K]<N).

For Example, for any Array A such that:

A[0]=1
A[1]=4
A[2]=-1
A[3]=3
A[4]=2

the following list is constructed:

the first node(the head) is located at index 0 and has a value of 1;
the second node is located at index 1 and has a value of 4;
the third node is located at index 4 and has a value of 2;
the fourth node is located at index 2 and has a value of -1.

write a function

Class Solution{ public int solution(int[] A);}
that, given a non empty zero-indexed array A consisting of N integers, returns the length of the list constructed from A in the above manner.

For eg, given array A such that:

A[0]=1
A[1]=4
A[2]=-1
A[3]=3
A[4]=2

this function will return 4, as explained in the example above.

Assume that:

N is an integer within the range [1..2,00,000];
each element of array A is an integer within the range [-1..N-1];
It will always be possible to construct the list and its length will be finite.

in your solution, focus on correctness. the performance of your solution will not be the focus of assessment. 
"""
