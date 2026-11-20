def squareit():
    while True:
        try:
            s = int(input("enter a number:"))


        except:
            print("this is not a number!")

        else:
            
            print("thank you")
            print( s**2)


squareit()