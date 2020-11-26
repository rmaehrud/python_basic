# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip


name = ['kim','park','cho','choi','yoo']

for name in name:
    print("You are : ", name)

word="dreams"

for s in word:
    print("word : ",s)


my_info = {
    "name":"kim",
    "age":33,
    "city":"seoul"
}

for key in my_info:
    print("my_info",key)

for key in list(my_info.values()):
    print("my_info",key)

for key in my_info.all():
    print("my_info",key)