while True:

    def menu():
        print("Welcome to Super Artistic Robot")
        print("option 1: Bowtie")
        print("option 2: Diamond")
        print("option 3: Hourglass")
        print("option 4: Trident")
        print("option 5: Exit")
        return input("Choose a painting(1-5):")

    def print_bowtie(H):
        for i in range(1, H + 1, 2):
            star = "*" * i
            space = " " * ((H - i) * 2)
            print(f"{star}{space}{star}")
        for i in range(H - 2, 0, -2):
            star = "*" * i
            space = " " * ((H - i) * 2)
            print(f"{star}{space}{star}")

    def print_diamond(H):
        for i in range(1, H + 1, 2):
            star = "*" * i
            space = " " * ((H - i) // 2)
            print(f"{space}{star}{space}")
        for i in range(H - 2, 0, -2):
            star = "*" * i
            space = " " * ((H - i) // 2)
            print(f"{space}{star}{space}")

    def print_hourglass(H):
        for i in range(H, 1, -2):
            star = "*" * i
            space = " " * ((H - i) // 2)
            print(f"{space}{star}{space}")
        for i in range(1, H + 2, 2):
            star = "*" * i
            space = " " * ((H - i) // 2)
            print(f"{space}{star}{space}")

    def print_trident(t, s, h):
        for i in range(t):
            star = "*"
            space = " " * s
            print(f"{star}{space}{star}{space}{star}")
        star1 = "*" * (2 * s + 3)
        print(star1)
        for i in range(h):
            star = "*"
            space1 = " " * (s + 1)
            print(f"{space1}{star}")

    choice=menu()
    if choice=="1":
        a=int(input("enter an odd number (5+):"))
        print_bowtie(a)
    elif choice=="2":
        b=int(input("enter an odd number (5+):"))
        print_diamond(b)
    elif choice=="3":
        c=int(input("enter an odd number (5+):"))
        print_hourglass(c)
    elif choice=="4":
        t=int(input("enter the height of the tines:"))
        s=int(input("enter the spacing between tines starting from 1 :"))
        h=int(input("enter the length of the handle:"))
        print_trident(t,s,h)
    elif choice=="5":
        print("Goodbye,have a wonderful day!")
        break
    else:
        print("Invalid choice, try again")



