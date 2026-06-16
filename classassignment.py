class MultiThings():
    def SubfieldsInAI():
        print("Machine Learning")
        message = "Machine Learning"
        print("Neural Networks")
        message = "Neural Networks"
        print("Vision")
        message = "Vision"
        print("Robotics")
        message = "Robotics"
        print("Speech Processing")
        message = "Speech Processing"
        print("Natural Language Processing")
        message = "Natural Language Processing"
        return message


    def OddEven():
        num=int(input("Enter the number"))
        if((num%2)==1):
            print(num,"is Odd number")
            message ="is Odd number"
        else:
            print(num,"is Even number")
            message="is Even number"
            return message


    def ElegiblityForMarriage():
        gender= input("Your Gender:")
        age=int(input("Your age:"))
        if(gender=="Male" and age >=21):
            print("ELIGIBLE")
            message="ELIGIBLE"
        elif(gender=="Female" and age >=18):
            print("ELIGIBLE")
            message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
            return message

    def percentage():

        total = 500
        obtained = 468
        percentage = (obtained / total) * 100
        print("Percentage =", percentage)
    
        return

    def triangle():

        Height=32
        BreadthTri=34
        AreaofTriangle=(Height*BreadthTri)/2
        print("Area of Triangle",AreaofTriangle)
        Height1=2
        Height2=4
        BreadthPer=4
        AreaofPerimeter=Height1+Height2+BreadthPer
        print("Perimeter of Triangle",AreaofPerimeter)
    
        return
      