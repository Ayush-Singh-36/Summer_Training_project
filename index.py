
# #variables
# age = 25
# print(age)
# print(type(age))
# data = [10, 20, 30]
# print(data[1])
# print(data[-2])
# data.append(40) #this function is basically used to add elements in the last of a list
# print(data) 
# #datatypes:-
# #premitive:- int, string, float, bool
# #non-premitive:- list, tuple, dict, set

# #insert:- this function is basically used to get a new element on a specific index
# data.insert(0, 5)
# print(data)

# #remove:- is basically used to remove any value from the list
# data.remove(20)
# print(data)

# year = float(input("Enter your No. of years working for this company:\n"))
# current_salary = int(input("Enter you current salary\n"))
# gender = input("Enter your gender:\n")
# if gender == "male" or "Male" or "M" or "m":
#     if current_salary >= 15000:
#         hram = current_salary-90%(current_salary)
#         dram = current_salary-85%(current_salary)
#         pfm = 15%(current_salary)
#         bonus_male = hram+dram
#         if year <= 5:
#             expected_salary = current_salary+hram+dram+bonus_male+pfm
#         else:
#             expected_salary = current_salary+hram+dram+pfm

#     elif current_salary >= 25000:
#         hram = current_salary-85%(current_salary)
#         dram = current_salary-70%(current_salary)
#         pfm = 20%(current_salary)
#         bonus_male = hram+dram
#         if year <= 5:
#             expected_salary = current_salary+hram+dram+bonus_male+pfm
#         else:
#             expected_salary = current_salary+hram+dram+pfm

#     else:
#         hram = current_salary-80%(current_salary)
#         dram = current_salary-65%(current_salary)
#         pfm = 25%(current_salary)
#         bonus_male = hram+dram
#         if year <= 5:
#             expected_salary = current_salary+hram+dram+bonus_male+pfm
#         else:
#             expected_salary = current_salary+hram+dram+pfm



# if gender == "female" or "Female" or "F" or "f":
#     if current_salary >= 15000:
#         hraf = current_salary-85%(current_salary)
#         draf = current_salary-70%(current_salary)
#         pff = 18%(current_salary)
#         bonus_female = hraf+draf
#         if year <= 5:
#             expected_salary = current_salary+hraf+draf+bonus_female+pff
#         else:
#             expected_salary = current_salary+hraf+draf+pff

#     elif current_salary >= 25000:
#         hraf = current_salary-80%(current_salary)
#         draf = current_salary-65%(current_salary)
#         pff = 22%(current_salary)
#         bonus_female = hraf+draf
#         if year <= 5:
#             expected_salary = current_salary+hraf+draf+bonus_female+pff
#         else:
#             expected_salary = current_salary+hraf+draf+pff

#     else:
#         hraf = current_salary-75%(current_salary)
#         draf = current_salary-60%(current_salary)
#         pff = 27%(current_salary)
#         bonus_female = hraf+draf
#         if year <= 5:
#             expected_salary = current_salary+hraf+draf+bonus_female+pff
#         else:
#             expected_salary = current_salary+hraf+draf+pff

# print("Your expected salary could be:- \n", expected_salary)

# year = float(input("Enter your No. of years working for this company:\n"))
# current_salary = int(input("Enter you current salary\n"))
# gender = input("Enter your gender:\n")
# if year <= 5:
#     if gender == "male" or "Male" or "M" or "m":
#         if current_salary >= 15000:
#             hram = current_salary-90%(current_salary)
#             dram = current_salary-85%(current_salary)
#             pfm = 15%(current_salary)
#             bonus_male = hram+dram
#             if year <= 5:
#                 expected_salary = current_salary+hram+dram+bonus_male+pfm
#             else:
#                 expected_salary = current_salary+hram+dram+pfm

#         elif current_salary >= 25000:
#             hram = current_salary-85%(current_salary)
#             dram = current_salary-70%(current_salary)
#             pfm = 20%(current_salary)
#             bonus_male = hram+dram
#             if year <= 5:
#                 expected_salary = current_salary+hram+dram+bonus_male+pfm
#             else:
#                 expected_salary = current_salary+hram+dram+pfm

#         else:
#             hram = current_salary-80%(current_salary)
#             dram = current_salary-65%(current_salary)
#             pfm = 25%(current_salary)
#             bonus_male = hram+dram
#             if year <= 5:
#                 expected_salary = current_salary+hram+dram+bonus_male+pfm
#             else:
#                 print("You'll not get bonuses")



# if gender == "female" or "Female" or "F" or "f":
#     if current_salary >= 15000:
#         hraf = current_salary-85%(current_salary)
#         draf = current_salary-70%(current_salary)
#         pff = 18%(current_salary)
#         bonus_female = hraf+draf
#         if year <= 5:
#             expected_salary = current_salary+hraf+draf+bonus_female+pff
#         else:
#             expected_salary = current_salary+hraf+draf+pff

#     elif current_salary >= 25000:
#         hraf = current_salary-80%(current_salary)
#         draf = current_salary-65%(current_salary)
#         pff = 22%(current_salary)
#         bonus_female = hraf+draf
#         if year <= 5:
#             expected_salary = current_salary+hraf+draf+bonus_female+pff
#         else:
#             expected_salary = current_salary+hraf+draf+pff

#     else:
#         print("You'll not get bonuses")

# num = eval(input("Enter your number:- \n"))
# if num > 0:
#     print(num * -1)
# elif num <= 0:
#     print(num)
# else:
#     print("Check your input")

# num = int(input("Enter your number:- \n"))
# #print(num)
# if num < 0:
#     print(num * -1)

# var1 = input("Enter anything:-\n")
# print(var1[::-1])

# for i in var1:
#     var2 = str(var1)[::-1]

# print(var2)

# for i in var1:
#     print(i+i[::-1])


# import random
# num = random.randint(0, 100)
# while True:
#     n = int(input("Enter you number:-\n"))
#     if num == n:
#         print("You've gussed correct")
#         break
#     if num > n:
#         print("Guess something lower")
#     if num < n:
#         print("Guess something higher")
        
# import random
# num = [24, 25, 26, 27, 28, 29, 30, 31, 23, 67]
# random.shuffle(num)
# while True:
#     guess = random.randint(0, 10)
#     if num.index(24) == guess:
#         print("System gussed it right!")
#         print(f"Actual value - {num.index(24)}\nGussed value - {guess}")
#         break
    
