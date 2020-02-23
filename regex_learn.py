import re
#number regex
message="ala ma kota numer +48 111-222-333 i numer +48 666-777-444, skjsjkdssdfucbjskdsdjkjdsf"
phoneNumRegex=re.compile(r"\+\d\d (\d\d\d-\d\d\d-\d\d\d)")
a=phoneNumRegex.search(message)
print(a.group(0))
print(a.group(1))
print(a.group(2))
print(phoneNumRegex.findall(message))

#pipeline expressions
batRegex=re.compile(r"bat(man|mobile|copter|bat)")
text="batman is in batmobile or batcopter to batbat"
print(batRegex.findall(text))

batmon="batmobile has lost a wallet"
a=batRegex.search(batmon)
print(a.group())

#repetitions
#  ? is 0 or 1
#  * 0 or more
#  + 1 or more
#  {x} exactly x
#  {x,x} x to y
batRegex=re.compile(r"Bat(wo)*man")
batstory1="Batman story"
batstory2="Batwoman story"
a=batRegex.search(batstory1)
b=batRegex.search(batstory2)
print(a.group())
print(b.group())

batRegex=re.compile(r"Bat(wo)*man")
a=batRegex.search("Batwowowoman find a cat")
print(a.group())

batRegex=re.compile(r"Bat(wo)+man")
a=batRegex.search("Batwoman has a ham")
print(a.group())

phoneNumRegex=re.compile(r'(\d\d\d-\d\d\d-\d\d\d(\,)?){3}')
message="ala ma 121-242-343,333-211-567,987-675-554"
a=phoneNumRegex.search(message)
print(a.group())

pinRegex=re.compile(r'(\d){4,8}')
pin=pinRegex.search("my pin is 67722")
print(pin.group())

# more of findall
message="ala +48 912-321-234  ola 923-777-575    sssad,sdfds  wnc +78 545-555-322"
phoneNumRegex=re.compile(r"\d\d\d-\d\d\d-\d\d\d")   #without groups is a list of strings
print(phoneNumRegex.findall(message))
phoneNumRegex=re.compile(r"(\+\d\d\ )?(\d\d\d-\d\d\d-\d\d\d)")  #with groups is a list of tuples
print(phoneNumRegex.findall(message))

# . * ?
vovelRegex=re.compile(r"[aeiouy]",re.IGNORECASE)
text="Ala ma kota a sierotka Marysia A V X Y N I O "
print(vovelRegex.findall(text))
catRegex=re.compile(r'cat \w+ \w+ \w+ \w+')
cats="cat one had a hat, cat two had a baloon, cat three had a map"
print(catRegex.findall(cats))

# sub()
