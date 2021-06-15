'''
A very useful data type you can import from a standard library is a default dictionary. In previous problems we were always using dictionaries to "accumulate" frequency counts of things, for example the frequency of letters in a string would be calculated as below:
'''

my_dict = {}
my_string = "I want to go home now"
for char in my_string:
    if char in my_dict.keys():
        my_dict[char]+=1
    else:
        my_dict[char]=1
# A frequency count of the letters in my_dict.
print(my_dict)