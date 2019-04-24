# -*- coding: utf-8 -*-

# UTF-8 encoding when using korean

import random
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

pre = list() #발표자
tog = list() #함께 읽기

names = list()

#windows -> 'cls', ubuntu,mac -> 'clear'


all_week = input("이번 기수의 총 활동 주를 입력해주세요(숫자만):")
de = input("몇주 차를 기점으로 돌리시겠습니까(숫자 4 이하) : ")

while True : #주차가 나누어 떨어질때까지 나누는 주차를 다시 받는다.
    if all_week%de == 0 :
        break
    else :
        de = input("약수로 입력해 주시기 바랍니다: ")


os.system('clear')  #windows -> 'cls', ubuntu,mac -> 'clear'

n = input("기수의 인원수를 입력하세요(숫자만):")


print "이름을 입력하세요"

for i in range(0, n):
    name = raw_input("이름 : ")
    names.append(name)
    os.system('clear')  #windows -> 'cls', ubuntu,mac -> 'clear'

for x in range(0,all_week/de):
    for week in range(0, de) :
    
        random_pick = random.sample(names, 4)
        
        
        print(str((x*4)+(week+1))+"주차 발표자는 '" +random_pick[0]+"', '"+random_pick[2] +"', 함께읽기는 '"+random_pick[1]+"', '"+random_pick[3]+ "' 입니다.")
        
        clear = random_pick
        clear = []
