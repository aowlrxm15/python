"""
날짜:2023-01-11
이름:전인준
내용:파이썬 상속 실습
"""
from sub1.StockAccount import StockAccount

kb = StockAccount('KB증권', '101-11-1000', '홍길동', 500000, '삼성전자', 10, 60000)
kb.deposit(2000000)
kb.sell(5, 70000)
kb.show()



