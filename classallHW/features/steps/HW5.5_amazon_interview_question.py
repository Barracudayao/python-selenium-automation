'''
5*[Not required]. Solve Amazon interview question:
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?
'''

# str1 = "Google"
# str2 = "Amazon"


def uniq_letter(string: str):
    if not string:
        return ValueError

    string = string.lower()
    for i in string:
        if string.count(i) == 1:
            return i
    return ""


print(uniq_letter("dfglltrew"))







