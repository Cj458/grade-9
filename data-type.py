# data types.

"""
text -> string
number -> 10, 0, 1 -12, 329494959595 -> integer int
        float, 2.5, 92.99

boolean -> True or False
"""



string = 'ABCDCDC'
sub_string = 'CDC'


def count_substring(string, sub_string):
        count, last_index = 0,-1 
        for curr in range(len(string)):
            if sub_string in string[curr:]:
                if string[curr:].index(sub_string) != last_index:
                    count += 1
                    last_index = string[curr:].index(sub_string)
            last_index -= 1
        return count




    

string = 'ABCDCDC'
sub_string = 'CDC'
print(count_substring(string=string, sub_string=sub_string))