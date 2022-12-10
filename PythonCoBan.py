#Bài 1 Khởi tạo
# ghi chú
print("Bài 1")
print("Hello Phat")


#Bài 2 Comment trong Python
print("Bài 2")
# chuỗi có dạng là một comment
print("#Đây là một comment")


#Bài 3 Biến (Variable) trong Python
print("Bài 3")
A = 20021997
B = 13021997
C = A + B
print(C)


#Bài 4 Kiểu số trong Python
print("#kiểu số")
print("Bài 4")
# gán cho biến A giá trị là 4. Với kiểu dữ liệu intergers (Số nguyên)
D = 4.56
print(D) 
# kiểu dữ liệu của A
print(type(D))
# lấy toàn bộ nội dung của thư viện Decimal
# từ thư viện Decimal -> import mọi thứ(*) vào
from decimal import*
from fractions import Fraction
from numbers import Complex
from unicodedata import decimal
# lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 20
# chỉ cần 1 phần tử Decimal thì sẽ lấy kết quả Decimal(Lấy tập hợp lớn nhất)
E=(Decimal(10)/Decimal(3))
print(E)
print(type(E))

print("#kiểu phân số")
# tạo ra 1 phân số có tử là 6, mẫu là 9
Frac = Fraction(6,9)
print(Frac)
print(type(Frac))
# tinh toan
Frac1 = Fraction(2,3)
Frac2 = Fraction(3,2)
Frac3 = Frac1 + Frac2
print(Frac3)

print("#kiểu sỐ phức")
# số thực là gồm phần thực và phần ảo
F = complex(2,5)
print(F)
# in ra phần thực
print(F.real)
# in ra sô ảo
print(F.imag)

# phép chia bình thương
H = 10/3
# thương nguyên của phép chia
#H = 10//3
# lấy phần dư phép chia
#H = 10%3
# lủy thừa
#H = 10**3
print(H)



 
