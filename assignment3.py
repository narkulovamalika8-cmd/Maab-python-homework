# 1. Count Occurrences: Given a list and an element, find how many times the element appears in the list.
a=[1, 2, 3, 4, 2, 3, 2]
print(a.count(3)) 

# 2. Sum of Elements: Given a list of numbers, calculate the total of all the elements.
a=[1, 2, 3, 4, 5]
print(sum(a))

# 3. Max Element: From a given list, determine the largest element.
a=[1, 2, 3, 4, 5]
print(max(a))

# 4. Min Element: From a given list, determine the smallest element.
a=[1, 2, 3, 4, 5]
print(min(a))

# 5. Check Element: Given a list and an element, check if the element is present in the list.
a=[1, 2, 3, 4, 5]
b=int(input("Enter an element to check: "))
print(b in a)

# 6. First Element: Access the first element of a list, considering what to return if the list is empty.
a=[1, 2, 3, 4, 5]
if a:
    print(a[0])
else:
    print("The list is empty.")

# 7. Last Element: Access the last element of a list, considering what to return if the list is empty.
a=[1, 2, 3, 4, 5]
if a:
    print(a[-1])
else:
    print("The list is empty.")

# 8. Slice List: Create a new list that contains only the first three elements of the original list.
a=[1, 2, 3, 4, 5]
b=a[0:3]
print(b)

# 9. Reverse List: Create a new list that contains the elements of the original list in reverse order.
a=[1, 2, 3, 4, 5]
b=a[::-1]
print(b)
a=[1, 2, 3, 4, 5]
b=a.copy()
b.reverse()
print(b)

# 10. Sort List: Create a new list that contains the elements of the original list in sorted order.
a=[3, 1, 4, 2, 5]
b=sorted(a, reverse=True)
print(b)

# 11. Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.
a=[1, 7, -1, 0, 2, 3, 2, 4, 3, 5]
b=list(set(a))
b=sorted(b)
print(b)

# 12. Insert Element: Given a list and an element, insert the element at a specified index.
a=[1, 2, 3, 4, 5]
a.insert(2, 10)
print(a)

# 13. Index of Element: Given a list and an element, find the index of the first occurrence of the element.
a=[1, 2, 3, 4, 5]
b=int(input("Enter an element to find its index: "))
if b in a:
    print(a.index(b))

# 14. Check for Empty List: Determine if a list is empty and return a boolean.
a=[1, 2, 3, 4, 5]
print(len(a) == 0)  # or print(not a)

# 15. Count Even Numbers: Given a list of integers, count how many of them are even.
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def count_even_numbers(a):
    return sum(1 for x in a if x % 2 == 0)
print(count_even_numbers(a))

# 16. Count Odd Numbers: Given a list of integers, count how many of them are odd.
def count_odd(nums: List[int]) -> int:
    return sum(1 for num in nums if num % 2 != 0)   
# 17. Concatenate Lists: Given two lists, create a new list that combines both lists
a=[1, 2, 3]
b=[4, 5, 6]
c=a+b
print(c)

# 18. Find Sublist: Given a list and a sublist, check if the sublist exists within the main list.
a=list(range(1, 11))
b=list(range(5, 8))
if all(elem in a for elem in b):
    print("Sublist exists.")
else:
    print("Sublist does not exist.")

# 19. Replace Element: given a list, replace the first occurence of a specified element with another element.
a=[1, 2, 3, 4, 5]
if 3 in a:
    a[a.index(3)] = 10
print(a)

#20. Find Second Largest: From a given list, find the second largest element.
a=input(list)
a=sorted(set(a), reverse=True)
print(a[1])

#21. Find Second Smallest: From a given list, find the second smallest element.
def second_smallest(nums: list):
    unique = set(nums)
    if len(unique)<2:
        return None
    unique.remove(min(unique))
    return min(unique)

#22. Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.
a=list[int]
b=[x for x in a if x%2==0]
print(b)
     
#23. Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.
a=list[int]
b=[x for x in a if x%2!=0]
print(b)

#24. List Length: Determine the number of elements in the list.
a=list[int]
print(len(a))

#25. Create a Copy: Create a new list that is a copy of the original list.
a=list[int]
b=a.copy()
print(b)

#26. Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
a=list[int]
mid=len(a)//2
if len(a)%2==0:
    print(a[mid-1:mid+1])
else:
    print(a[mid])

#27. Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.
a=list[int]
b=list[int]
if b in a:
    print(max(b))
else:
    print("Sublist not found in the main list.")
    
#28. Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.
a=list[int]
b=list[int]
if b in a:
    print(min(b))
else:
    print("Sublist not found in the main list.")

#29. Remove Element by Index: Given a list and an index, remove the element at that index if it exists.
a=list[int]
index=int(input("Enter the index of the element to remove: "))
if 0 <= index < len(a):
    a.pop(index)
    print(a)    
else:
    print("Index out of range.")

#30. Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.
a=list[int]
is_sorted = all(a[i] <= a[i + 1] for i in range(len(a) - 1))
print(is_sorted)

#31. Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.
a=list[int]
n=int(input("Enter the number of times to repeat each element: "))
b=[x for x in a for _ in range(n)]
print(b)

#32. Merge and Sort: Given two lists, create a new sorted list that merges both lists.
a=list[int]
b=list[int]
merged_sorted_list = sorted(a + b)
print(merged_sorted_list)

#33. Find All Indices: Given a list and an element, find all the indices of that element in the list.
a=list[int]
element=int(input("Enter the element to find its indices: "))
indices=[i for i, value in enumerate(a) if value == element]
print(indices)

#34. Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
a=list[int]
n=int(input("Enter the number of positions to rotate the list: "))
n = n % len(a)  # Handle cases where n is greater than the length of the list
rotated_list = a[-n:] + a[:-n]
print(rotated_list)

#35. Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).
start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
range_list = list(range(start, end + 1))
print(range_list)

#36. Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.
a=list[float]
sum_positive = sum(x for x in a if x > 0)
print(sum_positive)

#37. Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.
a=list[float]
b=sum(x for x in a if x<0)
print(b)

#38. Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
a=list
b=a==a[ : : -1]
print(b)
#39. Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
a=list(int)
b=int
if b <= 0:
    print("Number of elements per sublist must be greater than 0.")
else:
    nested_list = [a[i:i + b] for i in range(0, len(a), b)]
    print(nested_list)

#40. Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.
a=list[int]
if not a:
    print("The list is empty.")
else:
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)





#Tuple Tasks
#1. Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
a=tuple
n=('enter the element to count: ')
count = a.count(n)
print(count)

#2. Max Element: From a given tuple, determine the largest element.
a=tuple(int)
print(max(a))

#3. Min Element: From a given tuple, determine the smallest element.
a=tuple(int)
print(min(a))

#4. Check Element: Given a tuple and an element, check if the element is present in the tuple.
a=tuple
n=('enter the element to check: ')
if n in a:
    print("Element is present in the tuple.")
else:
    print("Element is not present in the tuple.")

#5. First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
a=tuple
if a:
    print("First element:", a[0])
else:
    print("Tuple is empty.")

#6. Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
a=tuple
if a:
    print("Last element:", a[-1])
else:
    print("Tuple is empty.")

#7. Tuple Length: Determine the number of elements in the tuple.
a=tuple
print("Tuple length:", len(a))

#8. Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
a=tuple
print("First three elements:", a[:3])

#9. Concatenate Tuples: Given two tuples, create a new tuple that combines both.
a=tuple
b=tuple
print("Concatenated tuple:", a + b)

#10. Check if Tuple is Empty: Determine if a tuple has any elements.
a=tuple
if not a:
    print("Tuple is empty.")
else:
    print("Tuple is not empty.")    

#11. Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
a=(1, 2, 3, 3, 4, 2, 5)
b=[]
for i in range(len(a)):
    if a[i]==3 or a[i]==2:
        b.append(i)
if b:
    print(b)
else:
    print("Element not found.")

#12. Find Second Largest: From a given tuple, find the second largest element.
a=tuple(int)
print("Second largest element:", sorted(set(a))[-2])
#13. Find Second Smallest: From a given tuple, find the second smallest element.
a=tuple(int)
print("Second smallest element:", sorted(set(a))[1])

#14. Create a Single Element Tuple: Create a tuple that contains a single specified element.
a=(5,)
print("Single element tuple:", a)

#15. Convert List to Tuple: Given a list, create a tuple containing the same elements.
list1=[1, 2, 3, 4, 5]
a=tuple(list1)
print("Converted tuple:", a)

#16. Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
a=tuple(int)
is_sorted=sorted(a)==list(a)
print("Is sorted:", is_sorted)

#17. Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
a=tuple(int)
b=tuple(int)
if b in a:
    print("Maximum of subtuple:", max(b))
else:
    print("Subtuple not found in the main tuple.")

#18. Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
a=tuple(int)
b=tuple(int)
if b in a:
    print("Minimum of subtuple:", min(b))
else:
    print("Subtuple not found in the main tuple.")

#19. Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
a=tuple(int)
n=int(input("Enter the element to remove: "))
if n in a:
    new_tuple=tuple(x for x in a if x!=n)
    print(new_tuple)
else:
    print("Element not found in the tuple.")

#20. Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
a=tuple(int)
b=int(input("Enter the number of elements per subtuple: "))
if b <= 0:
    print("Number of elements per subtuple must be greater than 0.")
else:
    nested_tuple=tuple(a[i:i+b] for i in range(0, len(a), b))
    print(nested_tuple)

#21. Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
a=tuple(int)
b=int(input("Enter the number of times to repeat each element: "))
if b <= 0:
    print("Number of repetitions must be greater than 0.")
else:
    repeated_tuple=tuple(x for x in a for _ in range(b))
    print(repeated_tuple)

#22. Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
a=int(input("Enter the starting number: "))
b=int(input("Enter the ending number: "))
range_tuple=tuple(range(a, b+1))
print(range_tuple)

#23. Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
a=tuple(int)
reversed_tuple=a[::-1]
print(reversed_tuple)

#24. Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
a=tuple(int)
b=a==a[::-1]
print("Is palindrome:", b)

#25. Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
a=tuple(int)
unique_tuple=tuple(dict.fromkeys(a))
print("Unique elements:", unique_tuple)




#Set Tasks
#1. Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
a=set
b=set
print("Union of sets:", a.union(b))

#2. Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
a=set
b=set
print("Intersection of sets:", a.intersection(b))

#3. Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.
a=set
b=set
print("Difference of sets:", a.difference(b))

#4. Check Subset: Given two sets, check if one set is a subset of the other.
a=set
b=set
print("Is subset:", a.issubset(b))

#5. Check Element: Given a set and an element, check if the element exists in the set.
a=set
element=int(input("Enter an element to check: "))
if element in a:
    print("Element exists:", element in a)
else:
    print("Element does not exist.")

#6. Set Length: Determine the number of unique elements in a set.
a=set
print("Set length:", len(a))

#7. Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.
a=list
b=set(a)
print("Set with unique elements:", b)

#8. Remove Element: Given a set and an element, remove the element if it exists.
a=set
element=int(input("Enter an element to remove: "))
if element in a:
    a.remove(element)
    print("Element removed.")
else:
    print("Element not found.")

#9. Clear Set: Create a new empty set from an existing set.
a=set
a.clear()
print("Set cleared:", a)

#10. Check if Set is Empty: Determine if a set has any elements.
a=set
if not a:
    print("Set is empty.")
else:
    print("Set is not empty.")

#11. Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.
a=set
b=set
print("Symmetric difference:", a.symmetric_difference(b))

#12. Add Element: Given a set and an element, add the element to the set if it is not already present.
a=set
b=int(input("Enter an element to add: "))
if b not in a:
    a.add(b)
    print("Element added.")
else:
    print("Element already exists in the set.")

#13. Pop Element: Given a set, remove and return an arbitrary element from the set.
a=set
if a:
    popped_element=a.pop()
    print("Popped element:", popped_element)
else:
    print("Set is empty, cannot pop an element.")

#14. Find Maximum: From a given set of numbers, find the maximum element.
a=set
print(max(a))

#15. Find Minimum: From a given set of numbers, find the minimum element.
a=set
print(min(a))

#16. Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.
a = {1, 2, 3, 4}
b={x for x in a if x % 2==0}
print(b)

#17. Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.
a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {x for x in a if x % 2 != 0}
print(b)
#18. Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).
a=set(range(1, 10))

#19. Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.
a = [1, 2, 3]
b = [3, 4, 5]
unique_set = set(a + b)
print(unique_set)

#20. Check Disjoint Sets: Given two sets, check if they have no elements in common.
a = {1, 2, 3}
b = {4, 5, 6}
if a.isdisjoint(b):
    print("there are not any common elements")
else:
    print("there are common elements")

#21. Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.
a=[1, 2, 3, 4, 4]
b=list(set(a))
print(b)

#22. Count Unique Elements: Given a list, determine the count of unique elements using a set.
a= [1, 2, 3, 3, 4, 5, 5]
b=len(set(a))
print(b)

#23. Generate Random Set: Create a set with a specified number of random integers within a certain range.
import random
count = 5
minimum=1
maximum=20
random_set=set()
while len(random_set)<count:
    random_set.add(random.randint(minimum, maximum))
print(random_set)

#Dictionary Tasks
#1. Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
a = {"name": "Alice", "age": 25}
key = "city"
print(a.get(key, "Key not found"))

#2. Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
a = {"name": "Alice", "age": 25}
key = "name"
print(key in a)

#3. Count Keys: Determine the number of keys in the dictionary.
a = {"name": "Alice", "age": 25}
print(len(a))

#4. Get All Keys: Create a list that contains all the keys in the dictionary.
a = {"name": "Alice", "age": 25}
print(list(a.keys()))

#5. Get All Values: Create a list that contains all the values in the dictionary.
a = {"name": "Alice", "age": 25}
print(list(a.values()))

#6. Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
a = {"name": "Alice"}
b = {"age": 25}
merged_dictionary = a | b
print(merged_dictionary)

#7. Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
a = {"name": "Alice", "age": 25}
key = "age"
if key in a:
    a.pop(key)
    print(a)
else:
    print("Key not found.")

#8. Clear Dictionary: Create a new empty dictionary.
a = {"name": "Alice", "age": 25}
a.clear()
print(a)

#9. Check if Dictionary is Empty: Determine if a dictionary has any elements.
a = {"name": "Alice"}
print(len(a) == 0)

#10. Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
a = {"name": "Alice", "age": 25}
key = "name"
if key in a:
    print((key, a[key]))
else:
    print("Key not found.")

#11. Update Value: Given a dictionary, update the value for a specified key.
a = {"name": "Alice", "age": 25}
a["age"] = 26
print(a)

#12. Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
a = {"a": 1, "b": 2, "c": 1, "d": 3}
value = 1
print(list(a.values()).count(value))

#13. Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
a = {"a": 1, "b": 2, "c": 3}
inverted_dictionary = {value: key for key, value in a.items()}
print(inverted_dictionary)

#14. Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value.
a = {"a": 1, "b": 2, "c": 1}
value = 1
matching_keys = [key for key, item_value in a.items() if item_value == value]
print(matching_keys)

#15. Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
keys = ["name", "age"]
values = ["Alice", 25]
a = dict(zip(keys, values))
print(a)

#16. Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
a = {"person": {"name": "Alice"}, "age": 25}
has_nested_dictionary = any(isinstance(value, dict) for value in a.values())
print(has_nested_dictionary)

#17. Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
a = {"person": {"name": "Alice", "age": 25}}
print(a["person"]["name"])

#18. Create Default Dictionary: Create a dictionary that provides a default value for missing keys.
from collections import defaultdict

a = defaultdict(lambda: "Not found")
a["name"] = "Alice"
print(a["age"])

#19. Count Unique Values: Given a dictionary, determine the number of unique values it contains.
a = {"a": 1, "b": 2, "c": 1, "d": 3}
print(len(set(a.values())))

#20. Sort Dictionary by Key: Create a new dictionary sorted by keys.
a = {"c": 3, "a": 1, "b": 2}
sorted_by_key = dict(sorted(a.items()))
print(sorted_by_key)

#21. Sort Dictionary by Value: Create a new dictionary sorted by values.
a = {"a": 3, "b": 1, "c": 2}
sorted_by_value = dict(sorted(a.items(), key=lambda item: item[1]))
print(sorted_by_value)

#22. Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
a = {"a": 1, "b": 4, "c": 7, "d": 10}
filtered_dictionary = {key: value for key, value in a.items() if value > 5}
print(filtered_dictionary)

#23. Check for Common Keys: Given two dictionaries, check if they have any keys in common.
a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}
common_keys = a.keys() & b.keys()
print(len(common_keys) > 0)
print(list(common_keys))

#24. Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.
a = (("name", "Alice"), ("age", 25))
dictionary = dict(a)
print(dictionary)

#25. Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
a = {"name": "Alice", "age": 25}
first_pair = next(iter(a.items()), None)
print(first_pair)







 

