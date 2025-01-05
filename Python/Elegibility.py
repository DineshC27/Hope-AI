class ElegiblityForMarriage():
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