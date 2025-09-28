1.# Class containing the method to find string length
class Solution:
    # Function to return length of a string
    def findLength(self, s):
        # Return length using built-in function
        return len(s)

# Driver code
if __name__ == "__main__":
    # Create object of Solution class
    obj = Solution()
    # Input string
    s = "Hello World"
    # Call function and print result
    print(obj.findLength(s))
  ...........................................................................................................................
2.
# Class containing the method to access characters
class Solution:
    # Function to print each character of a string
    def accessCharacters(self, s):
        # Loop through each index
        for i in range(len(s)):
            # Print the character at index i
            print(s[i])

# Driver code
if __name__ == "__main__":
    # Create object of Solution class
    obj = Solution()
    # Input string
    s = "Hello"
    # Call the function
    obj.accessCharacters(s)
..................................................................................................................
# Function to take a string and return a modified string
def modify_string(s):
    # Assign existing string to a new variable
    new_str = s
    # Append extra text
    new_str += " World"
    # Return the modified string
    return new_str

# Original string
original = "Hello"

# Pass string to function and store returned value
result = modify_string(original)

# Print results
print("Original:", original)
print("Returned:", result)
..................................................................................................................
# Class containing the compareStrings function
class Solution:
    # Function to compare two strings
    def compareStrings(self, str1, str2):
        # Return true if strings are equal
        return str1 == str2

# Driver code
if __name__ == "__main__":
    # Input first string
    str1 = input()

    # Input second string
    str2 = input()

    # Create Solution object
    obj = Solution()

    # Compare strings and print result
    if obj.compareStrings(str1, str2):
        print("Strings are equal")
    else:
        print("Strings are not equal")
