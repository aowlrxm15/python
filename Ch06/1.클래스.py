"""
날짜:2023-01-11
이름:전인준
내용:파이썬 클래스 실습
"""
from sub1.Car import Car
from sub1.Account import Account

sonata = Car('소나타', '흰색', 3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

bmw = Car('BMW', '검정', 5000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

kb = Account('국민은행', '101-12-1110', '이순신', 30000)
kb.deposit(20000)
kb.withdraw(5000)
# 캡슐화
# kb.balance += 100
kb.show()

wr = Account('우리은행', '101-21-0000', '장보고', 50000)
wr.deposit(10000)
wr.withdraw(2000)
wr.show()