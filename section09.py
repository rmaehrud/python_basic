# Section09
# 파일 읽기,쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, .: 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open


#파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

# 예제 2
with open('./resource/review.txt', 'r') as f: #close 생략가능
    c= f.read()
    print(c)
    print(list(c))
    print(iter(c))





# 예제 3
with open('./resource/review.txt', 'r') as f: #close 생략가능
    for c in f:
        print(c.strip())

print("-----------------------")
print("-----------------------")

# 예제4
with open('./resource/review.txt', 'r') as f: #close 생략가능
    content = f.read()
    print('>', content)
    content = f.read()
    print('>', content) # 내용 없음

print("-----------------------")
print("-----------------------")


# 예제 5
with open('./resource/review.txt', 'r') as f: #close 생략가능
    line = f.readline()
    # print(line)
    while line:
        print(line, end='####')
        line = f.readline()

# 예제 6
with open('./resource/review.txt', 'r') as f: #close 생략가능
    contents = f.readlines()# 리스트 형태로
    print(contents)
    for c in contents:
        print(c, end = '******')

print()
#예제 7
score=[]
with open('./resource/score.txt','r') as f:
    for line in f:
        score.append(int(line))
    print(score)


print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기
# 예제2
with open('./resource/text.txt','a') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('./resource/text.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

# 예제 4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['kim\n','park\n','cho\n']
    f.writelines(list)

with open('./resource/text4.txt','w') as f:
    print('Test contests1!',file=f)
    print('Test contests12',file=f)

with open('./resource/text.txt','r') as f:
    a = f.read()
    print(a)



