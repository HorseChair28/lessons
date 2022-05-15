a=457
b=a/100
c=a//100
d=a%100
print(b,c,d)

num = 407
is_three_digits = 0 < num // 100 <= 9
print(is_three_digits)
tens = num % 100 // 10
print(tens) # 5
print(tens == 5) # True