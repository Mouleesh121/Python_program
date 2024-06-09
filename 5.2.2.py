n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

arr.sort()

print("The elements of the array in ascending order are:")
print(' '.join(map(str, arr)))

