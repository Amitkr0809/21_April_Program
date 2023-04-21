# check given year is leap year or not


year = int(input("enter year : "))
if ((year % 4 == 0) or (year % 400)):
    print("Given year",year ,"is leap year")