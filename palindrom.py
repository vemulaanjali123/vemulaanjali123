def palindrome(string):
    # Remove any spaces and convert the string to lowercase
    string = string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return string == string[::-1]
