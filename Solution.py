# Enter your code here. Read input from STDIN. Print output to STDOUT
int(input())
n = input().split()
al = all(list(map(lambda x : int(x) > 0,n)))
an = any(list(map(lambda x : x[::-1] == x,n)))
print(al and an)
