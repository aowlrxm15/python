"""
날짜:2023-01-12
이름:전인준
내용:파이썬 외부 패키지모듈 실습
"""

from openpyxl import Workbook

# 새로운 엑셀파일 생성
workbook = Workbook()

# 첫번째 시트 활성화
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '파이썬 엑셀 실습'
sheet.append(['a101', '김유신', '010-1234-1001', 25, '김해시'])
sheet.append(['a102', '김춘추', '010-1234-1002', 26, '경주시'])
sheet.append(['a103', '장보고', '010-1234-1003', 27, '부산시'])
sheet.append(['a104', '강감찬', '010-1234-1004', 28, '서울시'])
sheet.append(['a105', '이순신', '010-1234-1005', 29, '제주시'])

# 저장닫기
workbook.save('C:/Users/G/Desktop/Member.xlsx')
workbook.close()

print('프로그램 종료...')
