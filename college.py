"""
College culture program admission entry 
"""

print("*** Welcom to Culture Program in our college ***")
print("*** Requested to fill all the details In other College Students ***")
print("*** This Compatition only for Computer Students ***")

college_name=input("Enter your college Name:")
department=input("Enter your Department:")
print("Compatition List \n 1.dance \n 2.sing \n 3.mime \n 4. Drama")


if department=="MCA" or department=="BCA" or department=="Bsc" or  department=="Msc":
    print("Hii guys")
    if department=="MCA" or department=="BCA":
        print("Go to Right Side and enter your competition name!...")
        competition=input("Enter your competition:")
        if competition=="dance" or competition=="sing":
            if competition=="dance":
                print("hello guys welcome to dance competition")
                members = input("Enter how many member participate:")
                if members == "solo":
                    print("Your performance time : 10 AM")
                elif members =="Group":
                    print("Your performance time : 12 PM")     
                else:
                    print("Your performance time : 2 PM")                
            elif competition=="sing":
                print("hello guys welcome to sing competition")
                type1=input("Enter which type to sing:")
                if type1=="classical":
                    print("Hey!...Hii go to the ground floor")
                elif type1=="melody":
                    print("Hey!...Hii go to the 1st floor")
                else:
                    print("Hey!...Hii go to the 5th floor")                
                
        else:
            print("Sorry!..Not Avaiable this competition")        
                
    elif department=="Bsc" or department=="Msc":
        print("Go to Left Side and enter your competition name!...")
        competition=input("Enter your competition:")
        if competition=="mime" or competition=="Drama":
            if competition=="mime":
                print("hello guys welcome to mime competition")
            elif competition=="Drama":
                print("hello guys welcome to Drama competition")
        else:
            print("Sorry!..Not Avaiable this competition")        
                
else:
    print("Sorry! You are not allowed...")    
                    