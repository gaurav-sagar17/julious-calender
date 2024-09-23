def print_week(arr,left = 0,right = 0 ):
    position = [5,6,8,7,5,7,5]
    if(right == 0 and left == 0) :
        for i in range(7) :
            print(" "*(position[i]-2),end="") 
            if(arr[i]<10) :
                print(" ",end="")
            print(arr[i],end="")
            print(" "*7,end=" ")
        print()
    elif(right>0) :
        for i in range(7-right) :
            print(" "*(position[i]-2),end="") 
            print(arr[i],end="")
            print(" "*7,end=" ")
        print()
    else :
        # for i in range(left) :
        #     print(" "*(position[i]+10),end="")
        # print(" "*4,end="")
        # for i in range(left,7) :
        #     print(" "*position[i],end="") 
        #     if(i == 6) :
        #         print("\b"*2,end="")
        #     print(arr[i],end="")
        #     print(" "*(left-(left-i)+4),end="")
        #     # print(" "*7,end=" ")
        # for i in range(left) :
        #     print(" "*position[i],end=" ") 
        #     print(" "*7,end="")
        # for i in range(left,7) :
        #     print(" "*position[i],end="") 
        #     print(arr[i],end="")
        #     print("
        #  "*7,end="")
        # print(" "*13,end="")
        # for i in range(7) :
        #     if(i<left) :
        #         print(" "*(position[i]-2),end="") 
        #         print(" ",end="")
        #         print(" "*7,end=" ")
        #         continue 

        #     print(" "*(position[i]-2),end="") 
        #     if(arr[i]<10) :
        #         print(" ",end="")
        #     print(arr[i],end="")
        #     print(" "*7,end=" ")
        for i in range(left+1) :
            print(" "*(position[i]+1),end="")
            if(i==left) :
                break 
            print(" "*7,end="")
        # print("a",end="")
        print("\b",end="")
        print("\b",end="")
        print(1,end="")
        for i in range(left+1,7) :
            print(" "*7,end="")
            print(" "*(position[i]),end="") 
            print(arr[i],end="") 
        print()
        





def printing(n,starting_day,p=False) : #n: total no. of days for the month , starting_day : day at which the month starts 
    mapping = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"] 
    # print_week(days)
    if(p==True) :
        for i in range(7) :
            print(days[i],end=" "*7)
        print() 
    initial_row = [0]*7 
    day_code = mapping[starting_day.lower()]
    finishing = 0
    for i in range(1,n+1) :
        try :
            initial_row[day_code] = i 
            day_code += 1

        except : 
            finishing = i 
            break 
    if(p==True):
        print_week(initial_row,mapping[starting_day.lower()])
        # rest  = [0]*7 
    count = 0
    
    while(finishing<n+1) : 
        if(count == 7) :
            if(p==True):
                print_week(initial_row)
            count = 0
        initial_row[count] = finishing
        finishing += 1
        count += 1
    ## use count to remove bekar elemensts
    if(p==True) :
        print_week(initial_row,right=7-count)
    # print(count)
    return days[count%7] ## returbn starting of the nest month

def main() :
    days = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    mapping = {"january":0,"february":1,"march":2,"april":3,"may":4,"june":5,"july":6,"august":7,"september":8,"october":9,"november":10,"december":11}
    leap_number = [31,29,31,30,31,30,31,31,30,31,30,31]
    running_leap = [0]*12
    rl = 0
    
    non_leap_number = [31,28,31,30,31,30,31,31,30,31,30,31]
    running_non_leap = [0]*12
    rnl = 0

    for  i in range(12) :
        rl += leap_number[i]
        rnl += non_leap_number[i]
        running_leap[i] = rl 
        running_non_leap[i] = rnl 

    starting_leap = [0]*12
    starting_non_leap = [0]*12 

    ## satrting day of each month
    temp1 = printing(leap_number[0],"monday") 
    starting_leap[0] = "monday"
    temp2 = printing(non_leap_number[0],"monday") 
    starting_non_leap[0] = "monday"
    for i in range(1,12) :
        starting_leap[i] = temp1
        starting_non_leap[i] = temp2
        temp1 = printing(leap_number[i],temp1) 
        temp2 = printing(non_leap_number[i],temp2) 

    # print(starting_leap)
    print("                        WELOCME TO JULIOUS CALENDER                      ")
    
    leap = False 
    month = input("enter the month u wish to view ")
    year = int(input("enter the year u mish to view : "))
    if(year % 100 == 0) :
        if(year % 400 == 0) :
                leap = True 
    elif(year % 4 == 0) :
        leap = True
    print(" "*7,days[mapping[month]]," "*7)
    if(leap==True) :
        # print(" "*7,days[mapping[month]]," "*7)
        printing(leap_number[mapping[month]],starting_leap[mapping[month]],p=True)
    else :
        printing(non_leap_number[mapping[month]],starting_non_leap[mapping[month]],p=True)
    temp = mapping[month]
    while(True):
        print("a.NEXT  ")
        print("b.PREV  ") 
        print("c.EXIT  ")
        option = input("enter your choice : ") 
        if(option.lower() == "c") :
            break 
        else :
            
            if(option.lower()=="a" ) :
                temp = (temp+1)%12
                print(" "*7,days[temp]," "*7)
                if(leap==True) :
                    printing(leap_number[temp],starting_leap[temp],p=True)
                else :
                    printing(non_leap_number[temp],starting_non_leap[temp],p=True)
            if(option.lower()=="b") :
                temp = (temp-1)

                if(temp < 0) :
                    temp += 12
                print(" "*7,days[temp]," "*7)
                if(leap==True) :
                    printing(leap_number[temp],starting_leap[temp],p=True)
                else :
                    printing(non_leap_number[temp],starting_non_leap[temp],p=True)

    




        


if(__name__=="__main__") :
    main() 




