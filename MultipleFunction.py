class MultipleFunction():
    def():
        num=int(input("Enter the number"))
        if((num%2)==1):
            print("odd number")
            message="odd number"
        else:
            print("even number")
            message= "even number"
        return message

    def BMI():
        BMI=int(input("Enter the BMI Index:",))
        if(BMI<=18):
            print("Underweight")
            message ="Underweight"
        elif(BMI<=20):
            print("Normal")
            message = "Normal"
        elif(BMI<=30):
            print("Overweight")
            message = "Overweight"
        else:
            print("very Overweight")
            message = "very Overweight"
        return message