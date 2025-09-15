'''
Dynamic Programming is a commonly used algorithmic technique used to optimize recursive solutions when same subproblems are called again.
Dynamic programming is used for solving problems that consists of the following characteristics:

1. Optimal Substructure:
The property Optimal substructure means that we use the optimal results of subproblems to achieve the optimal result of the bigger problem.

2. Overlapping Subproblems:
The same subproblems are solved repeatedly in different parts of the problem

1. Top-Down Approach (Memoization):
In the top-down approach, also known as memoization, we keep the solution recursive and add a memoization table to avoid repeated calls of same subproblems.

Before making any recursive call, we first check if the memoization table already has solution for it.
After the recursive call is over, we store the solution in the memoization table.

2. Bottom-Up Approach (Tabulation):
In the bottom-up approach, also known as tabulation, we start with the smallest subproblems and gradually build up to the final solution.

We write an iterative solution (avoid recursion overhead) and build the solution in bottom-up manner.
We use a dp table where we first fill the solution for base cases and then fill the remaining entries of the table using recursive formula.
We only use recursive formula on table entries and do not make recursive calls.
'''