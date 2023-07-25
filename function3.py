# function3.py

# 가변인자
def union(*ar):
    # 지역변수(리스트)
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM","SPAM"))
print(union("HAM",'SPAM','EGG'))

# 내장함수
#필터링 함수 정의
def getBiggerThan20(i):
    return i>20

lst=[10,25,30]
iterL=filter(None,lst)
for i in iterL:
    print(i)

iterL2=filter(getBiggerThan20,lst)
for k in iterL2:
    print(k)

print("---람다함수---")
iterL=filter(lambda x:x>20,lst)
for i in iterL:
    print(i)