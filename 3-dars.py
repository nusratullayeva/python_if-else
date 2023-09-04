# 1-masala
# inputNumber = int(input('Son kiriting: '))
# if inputNumber > 0:
#     print('Siz musbat son kiritdingiz!')
# else:
#     print('Siz manfiy son kiritdingiz!')



# 2-masala
# inputNumber = int(input('Son kiriting: '))
# if inputNumber > 10:
#     print(f'{inputNumber} soni 10dan katta')
# elif inputNumber < 10:
#     print(f'{inputNumber} soni 10 dan kichik')
# else:
#     print(f'son 10 ga teng')



# 3-masala
# inputNumber = int(input('Son kiriting: '))
# if inputNumber == 1:
#     print('siz 1 sonini kiritdingiz')
# elif inputNumber == 2:
#     print('siz 2 sonini kiritdingiz')
# elif inputNumber == 3:
#     print('siz 3 sonini kiritdingiz')
# elif inputNumber == 4:
#     print('siz 4 sonini kiritdingiz')
# elif inputNumber == 5:
#     print('siz 5 sonini kiritdingiz')
# else:
#     print('siz boshqa son kiritdingiz')









# Darslik masalalari!

# 2-masala
# inputNumber = int(input('Son kiriting: '))
# if inputNumber > 0:
#     print(f'{inputNumber + 1}')
# elif inputNumber < 0:
#     print(f'{inputNumber - 2}')



# 3-masala
# inputNumber = int(input('Son kiriting: '))
# if inputNumber > 0:
#     print(f'{inputNumber + 1}')
# elif inputNumber < 0:
#     print(f'{inputNumber - 2}')
# elif inputNumber == 0:
#     print(f'10')



# 4-masala
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
#
# musbat_sonlar_soni = 0
# if a > 0:
#     musbat_sonlar_soni += 1
# if b > 0:
#     musbat_sonlar_soni += 1
# if c > 0:
#     musbat_sonlar_soni += 1
#
# print(f"Uchta berilgan sonlarning orasida {musbat_sonlar_soni} ta musbat son bor.")



# 5-masala
# a = int(input('A sonni kiriting: '))
# b = int(input('B sonni kiriting: '))
# c = int(input('C sonni kiriting: '))
# musbat, manfiy = 0, 0
# if a > 0:
#     musbat += 1
# else:
#     manfiy += 1
# if a > 0:
#     musbat += 1
# else:
#     manfiy += 1
# if a > 0:
#     musbat += 1
# else:
#     manfiy += 1
# print(f'Kiritilgan sonlar {musbat} ta musbat soni va {manfiy} ta manfiy son bor')



# 6-masala
# inputNum = int(input('1-sonni kiriting: '))
# inputNum2 = int(input('2-sonni kiriting: '))
# if inputNum > inputNum2:
#     print(f'{inputNum} soni {inputNum2} dan katta!')
# elif inputNum2 > inputNum:
#     print(f'{inputNum2} soni {inputNum} dan katta.')



# 7-masala
# inputNum = int(input("Birinchi sonni kiriting: "))
# inputNum2 = int(input("Ikkinchi sonni kiriting: "))
#
# if inputNum < inputNum2:
#     print("Birinchi son kichik")
# elif inputNum == inputNum2:
#     print('Ikkalasi ham teng!')
# else:
#     print("Ikkinchi son kichik")



# 13-masala
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
#
# if a > b:
#     if b > c:
#         print(f"O'rtacha son {b}")
#     elif a > c:
#         print(f"O'rtacha son {c}")
#     else:
#         print(f"O'rtacha son {a}")
# else:
#     if b < c:
#         print(f"O'rtacha son {b}")
#     elif a < c:
#         print(f"O'rtacha son {c}")
#     else:
#         print(f"O'rtacha son {a}")



# 14-masala
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
#
# if a > b:
#     if b > c:
#         print(f"Kichik son: {c}\nKatta son: {a}")
#     elif a > c:
#         print(f"Kichik son: {b}\nKatta son: {a}")
#     else:
#         print(f"Kichik son: {b}\nKatta son: {c}")
# else:
#     if b < c:
#         print(f"Kichik son: {a}\nKatta son: {c}")
#     elif a < c:
#         print(f"Kichik son: {a}\nKatta son: {b}")
#     else:
#         print(f"Kichik son: {c}\nKatta son: {b}")



# 15-masala
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
#
# if a + b > b + c:
#     print(f"Katta sonlar: {a}, {b}")
# elif a + b < b + c:
#     print(f"Katta sonlar: {b}, {c}")
# else:
#     print(f"Katta sonlar: {a}, {c}")



# 28-masala
# year = int(input("Yilni kiriting: "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} kabisa yili, 366 kun bor.")
#         else:
#             print(f"{year} kabisa yili emas, 365 kun bor.")
#     else:
#         print(f"{year} kabisa yili, 366 kun bor.")
# else:
#     print(f"{year} kabisa yili emas, 365 kun bor.")



# 29-masala
# num = int(input("Sonni kiriting: "))
#
# if num == 0:
#     print("Son 0 ga teng.")
# elif num > 0:
#     if num % 2 == 0:
#         print("Musbat juft son.")
#     else:
#         print("Musbat toq son.")
# else:
#     if num % 2 == 0:
#         print("Manfiy juft son.")
#     else:
#         print("Manfiy toq son.")



# 30-masala
# def classify_numbers(numbers):
#     two_digit_even = []
#     three_digit_odd = []
#     others = []
#     for number in numbers:
#         if number % 2 == 0 and 10 <= number <= 99:
#             two_digit_even.append(number)
#         elif number % 2 == 1 and 100 <= number <= 999:
#             three_digit_odd.append(number)
#         else:
#             others.append(number)
#     return two_digit_even, three_digit_odd, others
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# two_digit_even, three_digit_odd, others = classify_numbers(numbers)
# print(f"Two digit even numbers: {two_digit_even}")
# print(f"Three digit odd numbers: {three_digit_odd}")
# print(f"Others: {others}")



# 8-masala
# def print_numbers_in_descending_order(a, b):
#     if a > b:
#         a, b = b, a
#     print(b, a)
# a = 999
# b = 100
# print_numbers_in_descending_order(a, b)
