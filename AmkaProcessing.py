
stop = False
current_year = 22


while (not (stop)):
    amka = (input("Enter your AMKA: "))
    man = True
    while (len(amka) != 11 and not(stop)):
        print("It has to be 11 digits")
        amka = (input("Enter your AMKA: "))

    assist = int(amka[4]+amka[5])
    age = current_year - assist;
    if (age < 0): age += 100;

    gender = int(amka[9])
    if (gender % 2 == 0):
        man = False
    if (man):
        print("It is a man. Age: " + str(age))
    else: print("It is a woman. Age: " + str(age))


    if (input("Do you wish to try another AMKA? Y/N ") != "Y"): stop = True
