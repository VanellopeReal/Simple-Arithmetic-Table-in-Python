key = True
whileKey = True
already_run = False
while key == True:
    if already_run == True:
        run = str(input("\nYou want to still using the program? (yes/no | y/n) ")).strip().lower()
        if run == "yes" or run == "y":
            already_run = False
            whileKey = True
        elif run == "no" or run == "n":
            key == False
            quit()
        elif run != "yes" and run != "no" and run != "n" and run != "y":
            print("\nThere's no option to: {}, the program will still running.\n".format(run))
            already_run = False
            whileKey = True
    number = float(input("Which number you need to see the arithmetic table? "))
    choose = int(input("How much multiply rows you need? [common = 10] "))
    print("\n")
    while whileKey == True:
        for i in range(choose):
            print("=" * 15)
            print("{} x {} = {}".format(number, choose, number * choose))
            choose -= 1
            already_run = True
        print("="*15)
        whileKey = False