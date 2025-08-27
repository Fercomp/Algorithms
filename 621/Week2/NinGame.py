'''
Problem J. Nim Game I

There are heaps of sticks and two players who move alternately. On each move, a player
chooses a non-empty heap and removes any number of sticks. The player who removes
the last stick wins the game.
Your task is to find out who wins if both players play optimally.

Input
The first input line contains an integer : the number of tests. After this, test cases are
described:
The first line contains an integer : the number of heaps.
The next line has integers : the number of sticks in each heap.

Output
For each test case, print "first" if the first player wins the game and "second" if the
second player wins the game.
Constraints
the sum of all is at most

Example
Input Output
3
4
5 7 2 5
2
4 1
3
3 5 6
first
first
second
'''

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    
    xor_sum = 0
    for h in l:
        xor_sum ^= h
        
    if xor_sum != 0:
        print("first")
    else:
        print("second")