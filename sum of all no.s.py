def cumulativesum(n):
        # base case
        if n==0:
            return n
        else:
            return n+cumulativesum(n-1)


n = int(input())
print(cumulativesum(n))
