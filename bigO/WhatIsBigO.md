# What is Big-O Notation

- Notation to describe the performance of algorithms 
- Emphasis on how performance scales with input size 
- Approximation 


## Why use Big-O Notation?

- Allows us to compare performance of algorithms
- Does not rely upon environment (language, hardware, etc ..)

## Big-O Simplification Rules
- Drop any constant factors 
    
    O(4n) -> O(n) 
    O(999n) -> O(n) 

A for loop looping from either 10 indexes or 1000 indexes is still classed as O(n)
    
We drop these constant factors regardless if they are large or not because Big-O is more focused on how the algorithm's performance scales with the input size as it approaches infinity.




One thing to watch out for is if our N is divided by something 

    O(n/2) -> O(1/2 n) -> O(n) 

An example of n/2 would be if we only processed half an array in a loop:

    ```python
    def process_half_array(arr):
        for i in range(len(arr) // 2):
            # Do something with arr[i]
    ```

If we had an array with 1 million results and we scanned through them at O(n/2) which would be scanning 0.5 million results or scanning 1 million, it still comes back to being O(n)

- Drop smaller terms in a sum 

    O(n² + n) -> O(n²)
    O(n + n⁴ + n²) -> O(n⁴)
    O(n⁴ - n³) -> O(n⁴)

    We are mostly concerned about the dominant term as n approaches infinity so n⁴ grows much faster than n² which makes it the dominant term.

    When n = 1,000: 1,000⁴ + 1,000² = 1,000,000,000,000 + 1,000,000 = 1,000,001,000,000
    As you can see, the n² term barely contributes to the total as n grows larger.


    Let's say we have O(4n² + n + 5) we drop any constants so we now have:

    O(n² + n + 5)
    
    Next we drop the smaller terms in the sum which leaves us with:

    O(n²)


    Another example: if we had O(n²/2 + 900)

    We can get rid of any constants so we can remove the /2 which leaves us with:

    O(n² + 900)

    900 is also a constant so we remove that and are left with:

    O(n²)



## Algorithm Speeds

Polynomial - A polynomial function is one where the variable is raised to a fixed power. 

O(n^k)

Examples 
- O(n)    linear (k=1)
- O(n²)   quadratic (k=2)
- O(n³)   cubic (k=3)
- O(n⁴)   quartic (k=4)

The higher the power the faster it grows

Exponential - An exponential function is one where the variable is in the exponent 

O(k^n)

Examples 
- O(2^n)
- O(3^n)


Some comparisons between polynomial and Exponential

n   n²    2^n

1   1     2
2   4     4 
5   25    32  
10  100   1024
20  400   1,048,576

As you can see the exponential (2^n) grows much faster than the polynomial function (n²) as n increases. 




**Worse**

factorial        O(n!) - n Factorial is for example 8*7*6..*1 = 40,320 
exponential      O(c^n) : O(2^n), O(3^n)
polynomial       O(n^c) : O(n²), O(n³)
linear           O(n) 
logarithmic      O(log(n))
constant         O(1)

**Better**



**Log refresher**
- A logarithm is the inverse operation to exponential. 

log_b(x) = y 
This means b^y = x 

Where:
- b is the base of the logarithm 
- x is the number we're taking the logarithm of (called the argument)
- y is the result of the logarithm 

Common Bases:
- Base 10 (common logarithm): Often written as just "log"
- Base e (natural logarithm): Written as "ln" (e is Euler's number, approx. 2.71828) 
- Base 2 (binary logarithm): Often used in computer science because computers use binary systems

log2(4) = 2 because 2² = 4
log2(8) = 3 because 2³ = 8 
log2(64) = 6 because 2⁶ = 64

You get the idea.



**Constant O(1)**

This means it takes 1 operation to complete.

An example of this would be accessing the first or last index of an array. If we did array[0], it takes 1 operation. However, if we needed to look for something within that array that we didn't know the location of, that would be O(n) even if we found it straight away within our search.


**Big-O examples**

a = 4 
sum = a + 10 

constant time complexity 

str = "hello"

print(str[1])

constant time complexity

stuff = { 'a': 1, 'b': 2, 'c': 3 }
print('b' in stuff)

This is still constant time in a Python dictionary

colors = ['red', 'blue', 'green', 'yellow']
print('green' in colors)

This is linear time because of how lists operate in Python

list = [5, 9, 2, -2, 12]
sum = 0 
for item in list:
    sum += item 
print(sum)

This is linear time of O(n) complexity 


sentence = "hello world how are you?"
print(sentence.split(" "))

This checks every char so it's also O(n)


letters = ['a', 'b', 'c', 'd', 'e', 'f']
for letter1 in letters:
    for letter2 in letters:
        print(letter1 + ' ' + letter2)

# n = letters length 
# time: O(n²)

def function2(n):
    for i in range(0, int(n / 2)):
        print(i)

function2(20)

# time: O(n / 2) simplified to O(n)
# space: O(1)

def function(n):
    nums = []
    for i in range(1, n):
        nums.append(i)
    return nums

print(function(10))

# time: O(n)
# space: O(n)
