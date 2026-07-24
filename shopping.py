import random
print(".................................")
print("\tStore Name")
print(".................................")
n = input("Enter your name:-\n")
a = input("Enter your age:-\n")
c = input("Enter your Contact:-\n")
grand_total = 0
running = True
def mobile():
    total = 0
    list1 = []
    for i in range(0, 16):
        price1 = random.randint(75000, 145000)
        list1.append(price1)
    global running
    while running:
        mb = int(input("\nWe have Phone of 4 different company, which one do you want, Enter Serial Number of the product as your choice:- \n\n1)Apple\n2)Google\n3)Samsung\n4)Realme\n\n"))
        if mb == 5:
            break
        if mb == 1:
            while running:
                var1 = int(input(f"\nCurrently we have 4 Models of apple enter Serial Number of the product as your choice:-\n\n1) Iphone SE\n2) Iphone 16 Pro Max\n3) Iphone 15 Pro\n4) Iphone 15\n\n"))
                a = list1
                if var1 == 1:
                    for i in a:
                        if i[0] > 30000 and i[0] < 50000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 45000 and i[0] < 75000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 45000 and i[0] < 65000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 35000 and i[0] < 55000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                
                
                print(f"\nNice, your total bill will be {bill}\n")
                ask = int(input("\nDo you want to continue with mobile shopping or anyother product or exit? - \npress '1' for mobile shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        if mb == 2:
            while running:
                var1 = int(input(f"Currently we have 4 Models of Google Pixels:-\n\n1) Pixel 8 Pro\n2) Pixel 9\n3) Pixel 10 Pro\n 4) Pixel 8\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 45000 and i[0] < 65000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 55000 and i[0] < 75000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 75000 and i[0] < 90000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 35000 and i[0] < 50000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with mobile shopping or anyother product or exit? - \npress '1' for mobile shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        elif mb == 3:
            while running:
                var1 = int(input(f"Currently we have 4 Models of Samsung Phones:-\n\n1) Galaxy S23 Ultra\n2) Galaxy S24\n3) Galaxy S25 Ulta\n4)Galaxy S26 Ultra\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 45000 and i[0] < 65000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 55000 and i[0] < 75000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 75000 and i[0] < 85000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 85000 and i[0] < 95000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                o = int(input("Do you wish to continue? - If Yes press '1', If No press '2'\n"))
                ask = int(input("\nDo you want to continue with mobile shopping or anyother product or exit? - \npress '1' for mobile shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        elif var1 == 4:
            while running:
                var1 = int(input(f"Currently we have 4 Models of Realme:\n\n1) Realme GT\n2) Realme 13\n3) Realme Narzo\n4) Realme C series\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 25000 and i[0] < 50000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 15000 and i[0] < 26000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 8500 and i[0] < 24000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 6000 and i[0] < 22000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with mobile shopping or anyother product or exit? - \npress '1' for mobile shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break
    return total
def cloths():
    total = 0
    list1 = []
    for i in range(0, 16):
        price1 = random.randint(1000, 10000)
        list1.append(price1)
    global running
    while running:
        mb = int(input("\nWe have cloths of 4 different brands, which one do you want, Enter Serial Number of the product as your choice:- \n\n1)Zara\n2)H&M\n3)Armani\n4)Gucci\n\n"))
        if mb == 5:
            break
        if mb == 1:
            while running:
                var1 = int(input(f"\nCurrently we have 4 Models of Zara enter Serial Number of the product as your choice:-\n\n1) T-shirts\n2) Denim jeans\n3) Shirts\n4) Hoodie\n\n"))
                a = list1
                if var1 == 1:
                    for i in a:
                        if i[0] > 2000 and i[0] < 8000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 7000 and i[0] < 15000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 45000 and i[0] <65000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 2000 and i[0] < 5000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"\nNice, your total bill will be {bill}\n")
                ask = int(input("\nDo you want to continue with cloths shopping or anyother product or exit? - \npress '1' for cloths shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        if mb == 2:
            while running:
                var1 = int(input(f"Currently we have 4 Models of H&M:-\n\n1) T-shirts\n2) Denim jeans\n3) Shirts\n 4) Hoodie,\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 499 and i[0] < 3000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 1500 and i[0] < 4000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 1500 and i[0] < 5000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 1000 and i[0] < 3000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with cloths shopping or anyother product or exit? - \npress '1' for cloths shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        elif mb == 3:
            while running:
                var1 = int(input(f"Currently we have 4 Models of Armani:-\n\n1) T-shirts\n2) Denim jeans\n3) Shirts\n4)Hoodie\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 3500 and i[0] < 7000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 4500 and i[0] < 10000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 7000 and i[0] < 13000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 6500 and i[0] < 15000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with cloths shopping or anyother product or exit? - \npress '1' for cloths shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    cloths() 
                elif ask == 3:
                    running = False
                    break
        elif var1 == 4:
            while running:
                var1 = int(input(f"Currently we have 4 Models of Gucci:\n\n1) T-shirts\n2) Denim jeans\n3) Shirts\n4) Hoodie\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 45000 and i[0] < 95000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 67000 and i[0] < 130000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 60000 and i[0] < 130000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 90000 and i[0] < 165000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with cloths shopping or anyother product or exit? - \npress '1' for cloths shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break
    return total
def sports():
    total = 0
    list1 = []
    for i in range(0, 16):
        price1 = random.randint(1000, 10000)
        list1.append(price1)
    global running
    while running:
        mb = int(input("\nWe have full kit of 4 different sports, which one do you want, Enter Serial Number of the product as your choice:- \n\n1)Cricket\n2)Football\n3)Badminton\n4)Basketball\n\n"))
        if mb == 5:
            break
        if mb == 1:
            while running:
                var1 = int(input(f"\nCurrently we have 4 kits of Cricket enter Serial Number of the product as your choice:-\n\n1) Includes - Bat & Ball\n2) Includes - Bat & Ball with some paddings\n3) Includes - Bat & Ball with some paddings and Helmet\n4) Includes - Bat & Ball with some paddings, Helmet and Jersey\n\n"))
                a = list1
                if var1 == 1:
                    for i in a:
                        if i[0] > 1000 and i[0] < 1500:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 3000 and i[0] < 5000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 7000 and i[0] <8000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 7000 and i[0] < 10000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"\nNice, your total bill will be {bill}\n")
                ask = int(input("\nDo you want to continue with sports shopping or anyother product or exit? - \npress '1' for sports shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        if mb == 2:
            while running:
                var1 = int(input(f"Currently we have 4 kits of Football:-\n\n1) Football\n2) Football + Shoes\n3) Football + Shoes + Uniform\n 4) Football + Shoes + Uniform + Shin Gurads\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 499 and i[0] < 3000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 1500 and i[0] < 4000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 2000 and i[0] < 6000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 5000 and i[0] < 8000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with sports shopping or anyother product or exit? - \npress '1' for sports shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        elif mb == 3:
            while running:
                var1 = int(input(f"Currently we have 4 Models of Badminton:-\n\n1) Badminton rackets + Shuttlecocks\n2) Badminton rackets + Shuttlecocks + Non-marking Shoes\n3) Badminton rackets + Shuttlecocks + Non-marking Shoes + Spare Overgrips\n4)Badminton rackets + Shuttlecocks + Non-marking Shoes + Spare Overgrips + Apperel\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 4000 and i[0] < 5000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 4500 and i[0] < 7000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 6000 and i[0] < 8500:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 7000 and i[0] < 9000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with sports shopping or anyother product or exit? - \npress '1' for sports shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break
        elif var1 == 4:
                    while running:
                        var1 = int(input(f"Currently we have 4 Models of BasketBall:\n\n1) Basketball + Apparel\n2) Basketball + Apparel + Footwear & socks\n3) Basketball + Apparel + Footwear & socks + Protective Gear\n4) Basketball + Apparel + Footwear & socks + Protective Gear + Accessories\n\n"))
                        if var1 == 1:
                            for i in a:
                                if i[0] > 2000 and i[0] < 4000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        elif var1 == 2:
                            for i in a:
                                if i[0] > 6000 and i[0] < 8000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        elif var1 == 3:
                            for i in a:
                                if i[0] > 10000 and i[0] < 13000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        elif var1 == 4:
                            for i in a:
                                if i[0] > 9000 and i[0] < 15000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        else:
                            print("Invalid choice!")
                            continue
                        print(f"Nice, your total bill will be {bill}")
                        ask = int(input("\nDo you want to continue with sports shopping or anyother product or exit? - \npress '1' for sports shopping, press '2' for any other product, press '3' for exit\n\n"))
                        if ask == 1:
                            break
                        elif ask == 2:
                            return
                        elif ask == 3:
                            running = False
                            break
    return total
def books():
    total = 0
    list1 = []
    for i in range(0, 16):
        price1 = random.randint(1000, 10000)
        list1.append(price1)
    global running
    while running:
        mb = int(input("\nWe have 4 different Genre of books, which one do you want, Enter Serial Number of the product as your choice:- \n\n1)Historical\n2)Technological\n3)Spiritual\n4)Poetry\n\n"))
        if mb == 5:
            break
        if mb == 1:
            while running:
                var1 = int(input(f"\nCurrently we have 4 books for Historical genre enter Serial Number of the product as your choice:-\n\n1) India: A History by John Keay\n2) India's Struggle for Independence by Bipan Chandra\n3) The Anarchy by William Dalrymple\n4) India After Gandhi by Ramachandra Guha\n\n"))
                a = list1
                if var1 == 1:
                    for i in a:
                        if i[0] > 1000 and i[0] < 1500:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 1000 and i[0] < 2000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 900 and i[0] <2000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 1000 and i[0] < 2000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"\nNice, your total bill will be {bill}\n")
                ask = int(input("\nDo you want to continue with books shopping or anyother product or exit? - \npress '1' for books shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        if mb == 2:
            while running:
                var1 = int(input(f"Currently we have 4 books of Technological genre enter Serial Number of the product as your choice:-\n\n1) Football\n2) Football + Shoes\n3) Football + Shoes + Uniform\n 4) Football + Shoes + Uniform + Shin Gurads\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 499 and i[0] < 3000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 1500 and i[0] < 4000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 2000 and i[0] < 6000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 5000 and i[0] < 8000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with books shopping or anyother product or exit? - \npress '1' for books shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break

        elif mb == 3:
            while running:
                var1 = int(input(f"Currently we have 4 Models of Badminton:-\n\n1) Badminton rackets + Shuttlecocks\n2) Badminton rackets + Shuttlecocks + Non-marking Shoes\n3) Badminton rackets + Shuttlecocks + Non-marking Shoes + Spare Overgrips\n4)Badminton rackets + Shuttlecocks + Non-marking Shoes + Spare Overgrips + Apperel\n\n"))
                if var1 == 1:
                    for i in a:
                        if i[0] > 4000 and i[0] < 5000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 2:
                    for i in a:
                        if i[0] > 4500 and i[0] < 7000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 3:
                    for i in a:
                        if i[0] > 6000 and i[0] < 8500:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                elif var1 == 4:
                    for i in a:
                        if i[0] > 7000 and i[0] < 9000:
                            bill = (i[0]*0.18)+i[0]
                            total += bill
                else:
                    print("Invalid choice!")
                    continue
                print(f"Nice, your total bill will be {bill}")
                ask = int(input("\nDo you want to continue with books shopping or anyother product or exit? - \npress '1' for books shopping, press '2' for any other product, press '3' for exit\n\n"))
                if ask == 1:
                    break
                elif ask == 2:
                    return
                elif ask == 3:
                    running = False
                    break
        elif var1 == 4:
                    while running:
                        var1 = int(input(f"Currently we have 4 Models of BasketBall:\n\n1) Basketball + Apparel\n2) Basketball + Apparel + Footwear & socks\n3) Basketball + Apparel + Footwear & socks + Protective Gear\n4) Basketball + Apparel + Footwear & socks + Protective Gear + Accessories\n\n"))
                        if var1 == 1:
                            for i in a:
                                if i[0] > 2000 and i[0] < 4000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        elif var1 == 2:
                            for i in a:
                                if i[0] > 6000 and i[0] < 8000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        elif var1 == 3:
                            for i in a:
                                if i[0] > 10000 and i[0] < 13000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        elif var1 == 4:
                            for i in a:
                                if i[0] > 9000 and i[0] < 15000:
                                    bill = (i[0]*0.18)+i[0]
                                    total += bill
                        else:
                            print("Invalid choice!")
                            continue
                        print(f"Nice, your total bill will be {bill}")
                        ask = int(input("\nDo you want to continue with books shopping or anyother product or exit? - \npress '1' for books shopping, press '2' for any other product, press '3' for exit\n\n"))
                        if ask == 1:
                            break
                        elif ask == 2:
                            return
                        elif ask == 3:
                            running = False
                            break
    return total
def choice():
    global running
    while running:
        ch = int(input("\nWhat do you want to buy:-\n1) Mobile Phones \n2) Cloths \n3) Sports \n4) Books \n5) Exit \n\nEnter Serial Number of the product as your choice:-\n\n"))
        if ch == 1:
            grand_total = mobile()
        elif ch == 2:
            grand_total = cloths()
        elif ch == 3:
            grand_total = sports()
        elif ch == 4:
            grand_total = books()
        elif ch == 5:
            running = False  # Sets flag to False, which will break this main menu loop
            print(f"\n------------------------------\n\tFinal Bill\n------------------------------\nCustomer Name: {n}\nAge: {a}\nContact: {c}\n------------------------------\n\tGrand Total: Rs. {grand_total}\n------------------------------\n")
        else:
            print("Invalid input! Please choose a number between 1 and 5.")

    print("\nThanks for visiting us!")
choice()
