# QUESTION 9

def reverse_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)

stack = []
n = int(input("Enter the number of elements in the stack: "))
for i in range(n):
    stack.append(int(input(f"Enter element {i + 1}: ")))

print(f"Original stack: {stack}")
reverse_stack(stack)
print(f"Reversed stack: {stack}")



# QUESTION 10

stack = []
n = int(input("Enter the number of elements in the stack: "))
for i in range(n):
    stack.append(int(input(f"Enter element {i + 1}: ")))

min_num = stack.pop()
while stack:
    num = stack.pop()
    if num < min_num:
        min_num = num

print(f"The smallest number is {min_num}")

def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
            
    return pairs

arr = [1, 2, 3, 4, 5]
target_sum = 7
result = find_pairs(arr, target_sum)
print(result)
