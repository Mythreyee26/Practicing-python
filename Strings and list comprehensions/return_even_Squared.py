# nums = [234,325567,356687,345]

nums = list(map(int,input("enter numbers separated by space: ").split()))

result = [x**2 for x in nums if x%2 == 0]
print(result)