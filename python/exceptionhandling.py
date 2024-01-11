try:
    numerator= int (input("Enter numerator:"))
    denominator= int (input("Enter denominator"))

    result= numerator/denominator
    print(result)

    my_list=[1,2,3]
    i= int(input ("Enter Index:"))
    print (my_list)

except ZeroDivisionError:
    print("Denominator cannot be 0. please try again")
except IndexError:
    print("Index cannot br greator than size of list")
    print("Program ends")    