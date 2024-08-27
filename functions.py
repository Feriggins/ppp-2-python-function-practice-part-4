# Function to find the maximum of three numbers
def max_num(a, b, c):
    return max(a, b, c)

# Function to multiply all numbers in a list
def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Function to reverse a string
def rev_string(s):
    return s[::-1]

# Function to check if a number falls within a given range
def num_within(num, start, end):
    return start <= num <= end

# Function to print the first n rows of Pascal's triangle
def pascal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
        print(' '.join(map(str, row)))

# Demonstrating the functions with examples
print("Max of 3, 7, 5:", max_num(3, 7, 5))
print("Multiplication of list [2, 3, 4]:", mult_list([2, 3, 4]))
print("Reversed string 'hello':", rev_string("hello"))
print("Is 3 within range 2 to 4:", num_within(3, 2, 4))
print("Pascal's Triangle with 5 rows:")
pascal(5)
