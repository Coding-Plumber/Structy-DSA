# anagrams
# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

# First thoughts - I know there are methods of sorting the string and then comparing them using in-built methods but i am avoiding doing it that way 

# Initial Approach - I will make a dict and loop over str1 to store the values which will look something like this

# dict = { 'a': 3, 'b': 2, 'e': 4}

# I will then do a second loop and deduct 1 each time, if i ever add 1 i can return False there. 
# If at the end i have any remaining values in the dict i know it's not a matching anagram and will return False 


# First code approach 

def anagrams(s1, s2):
  dict = {}
  

  for char in s1:
    if char not in dict:
      dict[char] = 1
    else:
      dict[char] += 1

  for char in s2:
    if char in dict:
      dict[char] -= 1
    if char not in dict:
      return False

  for char in dict:
    if dict[char] != 0:
      return False

  return True

# Time: O(n + m + k)
# Space: O(k)


# Refined version 

def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0 
        count[char] += 1 
    
    return count

# Time: O(n + m)
# Space: O(n + m) (Because we hold two dicts in memory)

