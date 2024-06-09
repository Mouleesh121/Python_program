def length(s):
    return len(s)
def copy(s):
    return s
def concatenate(s1, s2):
    return s1 + s2
def uppercase(s):
    return s.upper()


first = input("Enter the first string: ")
second = input("Enter the second string: ")
print("\nLength of first string:", length(first))
print("\nLength of second string:", length(second))
print("\nCopy of first string:",copy(first_string))
print("\nConcatenation of both strings:", concatenate(first, second))
print("\nUppercase of first string:", uppercase(first))
