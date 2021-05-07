# cook your dish here
def triangle(n):
    if n == 0 or n == 1 or n == 2 or n == 3:
        return 0
    else:
        return (n // 2 - 1) + triangle(n - 2)


t = int(input())
for _ in range(t):
    n = int(input())
    print(triangle(n))
