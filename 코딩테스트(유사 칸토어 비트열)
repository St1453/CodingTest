'''
Source : https://school.programmers.co.kr/learn/courses/30/lessons/148652
'''


def recur(n,index):
    if n==1:
        return '11011'[:index].count('1')
    quotient,remainder=divmod(index,5**(n-1))
    count_of_one=0
    if quotient<=1:
        count_of_one=4**(n-1)*quotient+recur(n-1,remainder)
    if quotient==2:
        count_of_one=4**(n-1)*2
    if quotient>2:
        count_of_one=4**(n-1)*(quotient-1)+recur(n-1,remainder)
    return count_of_one

def solution(n,l,r):
    return recur(n,r)-recur(n,l-1)
