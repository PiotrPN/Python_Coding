from pprint import pprint as pp
def count_chars(file_name):
    file=open(file_name,"r")
    chars={}
    for line in file:
        for char in line:
            chars.setdefault(char,0)
            chars[char]+=1
    return chars

pp(count_chars("dantes_inferno.txt"))