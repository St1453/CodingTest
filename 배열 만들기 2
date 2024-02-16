'''
https://school.programmers.co.kr/learn/courses/30/lessons/181921
'''

def gen(length_of_number):
    a=0
    collection=set()
    s=set([0])
    num='5'
    while a<length_of_number:
        for j in s:
            collection.add(j+int(num))
        s=collection|s
        num=num+'0'
        a+=1
    return collection

def solution(l,r):
    answer = []
    for i in gen(len(str(r))):
        if l<=i<=r:
            answer.append(i)
    if answer:
        answer.sort()
    else:
        answer=[-1]
    return answer
