# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    frequency_map = {}
    for num in numbers:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    most_frequent_element = None
    max_frequency = 0

    for num, frequency in frequency_map.items():
        if frequency > max_frequency:
            max_frequency = frequency
            most_frequent_element = num
    return most_frequent_element

    pass

"""
Time and Space Analysis for problem 1:
- Best-case: o(1)
- Worst-case: o(n)
- Average-case: o(n)
- Space complexity: o(n)
- Why this approach? only way i could think of
- Could it be optimized? im sure it can be optimized
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for item in nums:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: o(n)    
- Worst-case: o(n)
- Average-case: o(n)
- Space complexity: o(n)
- Why this approach? straightforward and efficient
- Could it be optimized?    not that i can think of
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num 
        if complement in seen:
            pairs.append(tuple(sorted((num, complement))))
        seen.add(num)
    return pairs

    

"""
Time and Space Analysis for problem 3:
- Best-case: o(n)
- Worst-case:   o(n)
- Average-case: o(n)
- Space complexity: o(n)
- Why this approach? efficient and straightforward
- Could it be optimized? yes it can im sure
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n, initial_capacity=1):
    my_list = [None] * initial_capacity
    size = 0
    capacity = initial_capacity

    for i in range(n):
        if size == capacity:
            print(f"List is full. Resizing from capacity {capacity} to {2 * capacity}")
            new_list = [None] * (2 * capacity)
            for j in range(size):
                new_list[j] = my_list[j]
            my_list = new_list
            capacity *= 2
            my_list[size] = f"Item_{i}"
            size += 1
            print(f"Added Item_{i}, size: {size}, capacity: {capacity}")
    
   

"""
Time and Space Analysis for problem 4: 
- When do resizes happen? when size == capacity
- What is the worst-case for a single append? o(n) when n is the number of elements in the list
- What is the amortized time per append overall? o(1)
- Space complexity: o(n)
- Why does doubling reduce the cost overall?because it makes resizing less frequent
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    running_sum = 0
    running_totals_list = []
    for num in nums:
        running_sum += num
        running_totals_list.append(running_sum)
    return running_totals_list
    pas

"""
Time and Space Analysis for problem 5:
- Best-case: o(n)
- Worst-case:   o(n)
- Average-case: o(n)
- Space complexity: o(n)
- Why this approach? straightforward and efficient
- Could it be optimized? not that i can think of for a single pass solution
"""
