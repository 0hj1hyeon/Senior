##20204111 오지현
num = input("0부터 5자리 사이의 숫자를 입력하세요")

length = len(num)
for length in range(length,5):
    num = '0' + num

for i in num:
    print(i, end='   ')















