class Math():
    def Subfields():
        lis = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for tmp in lis:
            print(tmp)
    def OddEven():
        num=int(input("Enter a number : "))
        if(num%2!=0):
            print(num," is Odd number")
        else:
            print(num," is Even number")
    def Elegible():
        gen=input("Your Gender:")
        age = int(input("Your Age:"))
        if(gen=="Male"):
            if(age<21):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(gen=="Female"):
            if(age<18):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        tot = sub1+sub2+sub3+sub4+sub5
        print("Total : ",tot)
        print("Percentage : ",tot*100/500)
    def triangle():
        hg = int(input("Height :"))
        bth = int(input("Breadth :"))
        print("Area formula: (Height*Breadtg)/2")
        print("Area of Triangle:",(hg*bth)/2)
        hg1 = int(input("Height1 :"))
        hg2 = int(input("Height2 :"))
        bdh = int(input("Breadth :"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",hg1+hg2+bdh)