# Parameterized Recursion
# In this approach, we pass an extra parameter (`soma`) that carries the partial result.
# With each recursive call, we accumulate the result in this parameter.
# Once the base case is reached, the accumulated result is printed.
def sum_n_param(n, soma):
    if n < 0:  # base case: stop when n becomes negative
        print(soma)
    else:
        sum_n_param(n - 1, soma + n)


# Functional Recursion
# In this approach, each recursive call *returns* a value.
# The recursion builds the final result during the unwinding phase of the call stack.
# Once the base case is reached, values are returned step by step to the previous calls.
def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

print(sum_n(6))
sum_n_param(6, 0)