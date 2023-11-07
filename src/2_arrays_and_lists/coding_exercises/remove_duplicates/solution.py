# Question 7 - Remove duplicates   
# Time complexity: O(n)
# Space complexity: O(n)

def remove_duplicates(arr):
    seen = set()
    new_array = list()
    for element in arr:
        if element in seen:
            continue
        seen.add(element)
        new_array.append(element)
    return new_array

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
