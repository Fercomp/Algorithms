# https://atcoder.jp/contests/abc124/tasks/abc124_a?lang=en

a, b = map(int, input().split())
x1 = a + a-1
x2 = a + b
x3 = b + b-1
print(max(x1, x2, x3))