# Python String

Last Updated :  10 Mar, 2025

__

Comments

__

Improve

__

  *   *   * 

__ Suggest changes

Like Article

__ Like

__ Report

A string is a sequence of characters. Python treats anything inside quotes as
a string. This includes letters, numbers, and symbols. Python has no character
data type so single character is a string of length 1.

Python `

    
    
    s = "GfG"
    
    print(s[1]) # access 2nd char
    s1 = s + s[0] # update
    print(s1) # print
    

`

  
**Output**

    
    
    f
    GfGG
    

In this example, ****s**** holds the value "GfG" and is defined as a string.

Table of Content

  * Creating a String
  * Accessing characters in Python String
  * String Immutability
  * Deleting a String
  * Updating a String
  * Common String Methods
  * Concatenating and Repeating Strings
  * Formatting Strings

## Creating a String

Strings can be created using either ****single (')**** or****double (")****
quotes.

Python `

    
    
    s1 = 'GfG'
    s2 = "GfG"
    print(s1)
    print(s2)
    

`

  
**Output**

    
    
    GfG
    GfG
    

### Multi-line Strings

If we need a string to span multiple lines then we can use ****triple quotes
(''' or """)****.

Python `

    
    
    s = """I am Learning
    Python String on GeeksforGeeks"""
    print(s)
    
    s = '''I'm a 
    Geek'''
    print(s)
    

`

  
**Output**

    
    
    I am Learning
    Python String on GeeksforGeeks
    I'm a 
    Geek
    

## Accessing characters in Python String

Strings in Python are sequences of characters, so we can access individual
characters using ****indexing.**** Strings are indexed starting from ****0****
and ****-1**** from end****.**** This allows us to retrieve specific
characters from the string.

![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200204160843/strings.jpg)Python String syntax indexing Python `

    
    
    s = "GeeksforGeeks"
    
    # Accesses first character: 'G'
    print(s[0])  
    
    # Accesses 5th character: 's'
    print(s[4]) 
    

`

  
**Output**

    
    
    G
    s
    

****Note:**** Accessing an index out of range will cause an
****IndexError****. Only integers are allowed as indices and using a float or
other types will result in a ****TypeError****.

### Access string with [Negative
Indexing](https://www.geeksforgeeks.org/slicing-with-negative-numbers-in-
python/)

Python allows negative address references to access characters from back of
the String, e.g. -1 refers to the last character, -2 refers to the second last
character, and so on.

Python `

    
    
    s = "GeeksforGeeks"
    
    # Accesses 3rd character: 'k'
    print(s[-10])  
    
    # Accesses 5th character from end: 'G'
    print(s[-5]) 
    

`

  
**Output**

    
    
    k
    G
    

### String Slicing

[Slicing ](https://www.geeksforgeeks.org/string-slicing-in-python/)is a way to
extract portion of a string by specifying the ****start**** and ****end****
indexes. The syntax for slicing is ****string[start:end]**** , where
****start**** starting index and ****end**** is stopping index (excluded).

Python `

    
    
    s = "GeeksforGeeks"
    
    # Retrieves characters from index 1 to 3: 'eek'
    print(s[1:4])  
    
    # Retrieves characters from beginning to index 2: 'Gee'
    print(s[:3])   
    
    # Retrieves characters from index 3 to the end: 'ksforGeeks'
    print(s[3:])   
    
    # Reverse a string
    print(s[::-1])
    

`

  
**Output**

    
    
    eek
    Gee
    ksforGeeks
    skeeGrofskeeG
    

## String Immutability

****Strings in Python are immutable****. This means that they cannot be
changed after they are created. If we need to manipulate strings then we can
use methods like ****concatenation, slicing,**** or ****formatting**** to
create new strings based on the original.

Python `

    
    
    s = "geeksforGeeks"
    
    # Trying to change the first character raises an error
    # s[0] = 'I'  # Uncommenting this line will cause a TypeError
    
    # Instead, create a new string
    s = "G" + s[1:]
    print(s)
    

`

  
**Output**

    
    
    GeeksforGeeks
    

## Deleting a String

In Python, it is not possible to delete individual characters from a string
since strings are immutable. However, we can delete an entire string variable
using the [****del****](https://www.geeksforgeeks.org/python-del-to-delete-
objects/) keyword.

Python `

    
    
    s = "GfG"
    
    # Deletes entire string
    del s  
    

`

****Note:**** After deleting the string using ****del**** and if we try to
access ****s**** then it will result in a ****NameError**** because the
variable no longer exists.

## Updating a String

To update a part of a string we need to create a new string since strings are
immutable.

Python `

    
    
    s = "hello geeks"
    
    # Updating by creating a new string
    s1 = "H" + s[1:]
    
    # replacnig "geeks" with "GeeksforGeeks"
    s2 = s.replace("geeks", "GeeksforGeeks")
    print(s1)
    print(s2)
    

`

  
**Output**

    
    
    Hello geeks
    hello GeeksforGeeks
    

****Explanation:****

  * ****For s1,**** The original string ****s**** is sliced from index 1 to end of string and then concatenate "H" to create a new string ****s1****. 
  * ****For s2,**** we can created a new string s2 and used [replace() method](https://www.geeksforgeeks.org/python-string-replace/) to replace 'geeks' with 'GeeksforGeeks'.

## Common String Methods

Python provides a various built-in methods to manipulate strings. Below are
some of the most useful methods.

****len()**** : The [len()](https://www.geeksforgeeks.org/python-len-
function/) function returns the total number of characters in a string.

Python `

    
    
    s = "GeeksforGeeks"
    print(len(s))
    
    # output: 13
    

`

  
**Output**

    
    
    13
    

****upper() and lower()**** : [upper()](https://www.geeksforgeeks.org/python-
string-upper/) method converts all characters to uppercase. [lower()
](https://www.geeksforgeeks.org/python-string-lower/)method converts all
characters to lowercase.

Python `

    
    
    s = "Hello World"
    
    print(s.upper())   # output: HELLO WORLD
    
    print(s.lower())   # output: hello world
    

`

  
**Output**

    
    
    HELLO WORLD
    hello world
    

****strip() and replace()**** :
[strip()](https://www.geeksforgeeks.org/python-string-strip/) removes leading
and trailing whitespace from the string and [replace(old, new)
](https://www.geeksforgeeks.org/python-string-replace/)replaces all
occurrences of a specified substring with another.

Python `

    
    
    s = "   Gfg   "
    
    # Removes spaces from both ends
    print(s.strip())    
    
    s = "Python is fun"
    
    # Replaces 'fun' with 'awesome'
    print(s.replace("fun", "awesome"))  
    

`

  
**Output**

    
    
    Gfg
    Python is awesome
    

To learn more about string methods, please refer to [Python String
Methods](https://www.geeksforgeeks.org/python-string-methods/).

## Concatenating and Repeating Strings

We can concatenate strings using[******** \+
operator](https://www.geeksforgeeks.org/python-operators/)******** and repeat
them using [* operator](https://www.geeksforgeeks.org/python-operators/).

Strings can be combined by using ****\+ operator****.

Python `

    
    
    s1 = "Hello"
    s2 = "World"
    s3 = s1 + " " + s2
    print(s3)
    

`

  
**Output**

    
    
    Hello World
    

We can repeat a string multiple times using ***** operator****.

Python `

    
    
    s = "Hello "
    print(s * 3)
    

`

  
**Output**

    
    
    Hello Hello Hello 
    

## Formatting Strings

Python provides several ways to include variables inside strings.

### Using f-strings

The simplest and most preferred way to format strings is by using
[f-strings](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-
python/)****.****

Python `

    
    
    name = "Alice"
    age = 22
    print(f"Name: {name}, Age: {age}")
    

`

  
**Output**

    
    
    Name: Alice, Age: 22
    

### Using format()

Another way to format strings is by using [format()
](https://www.geeksforgeeks.org/python-string-format-method/)method.

Python `

    
    
    s = "My name is {} and I am {} years old.".format("Alice", 22)
    print(s) 
    

`

  
**Output**

    
    
    My name is Alice and I am 22 years old.
    

## Using __in__ for String Membership Testing

The[ ****in**** keyword ](https://www.geeksforgeeks.org/python-in-
keyword/)checks if a particular substring is present in a string.

Python `

    
    
    s = "GeeksforGeeks"
    print("Geeks" in s)
    print("GfG" in s)
    

`

  
**Output**

    
    
    True
    False
    

### Quiz:

  * [Python String Quiz](https://www.geeksforgeeks.org/quizzes/python-string-quiz/)

### ****Related Articles:****

  * [ String Slicing](https://www.geeksforgeeks.org/string-slicing-in-python/)
  * [f Strings in Python](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/)
  * [String Comparison in Python](https://www.geeksforgeeks.org/string-comparison-in-python/)
  * [7 Useful String Functions in Python](https://www.geeksforgeeks.org/7-useful-string-functions-in-python/)
  * [Convert integer to String in Python](https://www.geeksforgeeks.org/convert-integer-to-string-in-python/)
  * [Convert string to integer in Python](https://www.geeksforgeeks.org/convert-string-to-integer-in-python/)
  * [String Concatenation](https://www.geeksforgeeks.org/python-string-concatenation/)
  * [Split String into list of Characters in Python](https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/)
  * [Iterate over characters of strings in Python](https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-python/)
  * [Python program to convert a string to list](https://www.geeksforgeeks.org/python-program-convert-string-list/)
  * [Python program to convert a list to string](https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/)
  * [String Comparison in Python](https://www.geeksforgeeks.org/string-comparison-in-python/)
  * [String Formatting in Python](https://www.geeksforgeeks.org/string-comparison-in-python/)
  * [Python String Methods](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/)
  * [Python String Exercise](https://www.geeksforgeeks.org/python-string-exercise/)
  * [Escape characters in Python](https://www.geeksforgeeks.org/ways-print-escape-characters-python/)

### Recommended Problems:

  * [Welcome aboard - Python](https://www.geeksforgeeks.org//problems/welcome-aboard-python/1&selectedLang=python3)
  * [Repeat the Strings - Python](https://www.geeksforgeeks.org/problems/repeat-the-strings/1&selectedLang=python3)
  * [String Functions I - Python](https://www.geeksforgeeks.org/problems/string-functions-i/1&selectedLang=python3)
  * [Regex - Python](https://www.geeksforgeeks.org//problems/string-functions-ii/1&selectedLang=python3)
  * [Convert String to LowerCase](https://www.geeksforgeeks.org//problems/java-convert-string-to-lowercase2313/1&selectedLang=python3)
  * [String Duplicates Removal](https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1&selectedLang=python3)
  * [Reverse String](https://www.geeksforgeeks.org//problems/reverse-string--141628/1&selectedLang=python3)
  * [Check Palindrome](https://www.geeksforgeeks.org//problems/check-palindrome--141628/1&selectedLang=python3)
  * [Closest Strings](https://www.geeksforgeeks.org/problems/closest-strings0611/1&selectedLang=python3)
  * [Divisible by 7](https://www.geeksforgeeks.org/problems/divisible-by-73224/1&selectedLang=python3)
  * [Encrypt the String – II](https://www.geeksforgeeks.org/problems/encrypt-the-string-21117/1&selectedLang=python3)
  * [Equal point in a string of brackets](https://www.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets2542/1&selectedLang=python3)
  * [Isomorphic Strings](https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1&selectedLang=python3)
  * [Check if two strings are k-anagrams or not](https://www.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1&selectedLang=python3)
  * [Panagram Checking](https://www.geeksforgeeks.org/problems/pangram-checking-1587115620/1&selectedLang=python3)
  * [Minimum Deletions](https://www.geeksforgeeks.org/problems/minimum-deletitions1648/1&selectedLang=python3)
  * [Number of Distinct Subsequences](https://www.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1&selectedLang=python3)
  * [Check if string is rotated by two places](https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1&selectedLang=python3)
  * [Implement Atoi](https://www.geeksforgeeks.org/problems/implement-atoi/1&selectedLang=python3)
  * [Validate an IP address](https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1&selectedLang=python3)
  * [License Key Formatting](https://www.geeksforgeeks.org/problems/license-key-formatting/1&selectedLang=python3)
  * [Find the largest word in dictionary](https://www.geeksforgeeks.org/problems/find-largest-word-in-dictionary2430/1&selectedLang=python3)
  * [Equal 0,1, and 2](https://www.geeksforgeeks.org/problems/equal-0-1-and-23208/1&selectedLang=python3)
  * [Add Binary Strings](https://www.geeksforgeeks.org/problems/add-binary-strings3805/1&selectedLang=python3)
  * [Sum of two large numbers](https://www.geeksforgeeks.org/problems/sum-of-numbers-or-number1219/1&selectedLang=python3)
  * [Multiply two strings](https://www.geeksforgeeks.org/problems/multiply-two-strings/1&selectedLang=python3)
  * [Look and say Pattern](https://www.geeksforgeeks.org/problems/decode-the-pattern1138/1&selectedLang=python3)
  * [Longest Palindromic Subsequence](https://www.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1&selectedLang=python3)
  * [Longest substring without repeating characters](https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1&selectedLang=python3)
  * [Substrings of length k with k-1 distinct elements](https://www.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1&selectedLang=python3)
  * [Count number of substrings](https://www.geeksforgeeks.org/problems/count-number-of-substrings/0&selectedLang=python3)
  * [Interleaved Strings](https://www.geeksforgeeks.org/problems/interleaved-strings/1&selectedLang=python3)
  * [Print Anagrams together](https://www.geeksforgeeks.org/problems/print-anagrams-together/1&selectedLang=python3)
  * [Rank the permutation](https://www.geeksforgeeks.org/problems/rank-the-permutations2229/1&selectedLang=python3)
  * [A Special Keyboard](https://www.geeksforgeeks.org/problems/special-keyboard3018/1&selectedLang=python3)
  * [Restrictive Candy Crush](https://www.geeksforgeeks.org/problems/8c8f95810b05b4cab665f2997d36991bd58308a2/1&selectedLang=python3)
  * [Edit Distance](https://www.geeksforgeeks.org/problems/edit-distance3702/1)
  * [Search Pattern (KMP-Algorithm)](https://www.geeksforgeeks.org/problems/last-match1928/1&selectedLang=python3)
  * [Search Pattern (Rabin-Karp Algorithm)](https://www.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4b9596b/1&selectedLang=python3)
  * [Search Pattern (Z-algorithm)](https://www.geeksforgeeks.org/problems/8dcd25918295847b4ced54055eae35a8501181c1/1&selectedLang=python3)
  * [Shortest Common Supersequence](https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1&selectedLang=python3)
  * [Number of words with K maximum distinct vowels](https://www.geeksforgeeks.org/problems/7b9d245852bd8caf8a27d6d3961429f0a2b245f1/1&selectedLang=python3)
  * [Longest substring to form a Palindrome](https://www.geeksforgeeks.org/problems/longest-substring-whose-character-rearranged-can-form-a-palindrome/1&selectedLang=python3)
  * [Longest Valid Parenthesis](https://www.geeksforgeeks.org/problems/longest-valid-parentheses5657/1&selectedLang=python3)
  * [Distinct Palindromic Substrings](https://www.geeksforgeeks.org/problems/distinct-palindromic-substrings5141/1&selectedLang=python3)

  

__ Comment

More info

[Campus Training Program](https://www.geeksforgeeks.org/campus-training-
program/)

[ Next Article ](https://www.geeksforgeeks.org/why-are-python-strings-
immutable/)

[Why are Python Strings Immutable?](https://www.geeksforgeeks.org/why-are-
python-strings-immutable/)

[![author](https://media.geeksforgeeks.org/auth/profile/8wh06px7rkj21jihprcr)
__ ](https://www.geeksforgeeks.org/user/abhishek1/)

[abhishek1](https://www.geeksforgeeks.org/user/abhishek1/)

Follow

__

Improve __

Article Tags :

  * [Misc](https://www.geeksforgeeks.org/category/misc/)
  * [Python](https://www.geeksforgeeks.org/category/programming-language/python/)
  * [python-string](https://www.geeksforgeeks.org/tag/python-string/)

Practice Tags :

  * [Misc](https://www.geeksforgeeks.org/explore?category=Misc)
  * [python](https://www.geeksforgeeks.org/explore?category=python)