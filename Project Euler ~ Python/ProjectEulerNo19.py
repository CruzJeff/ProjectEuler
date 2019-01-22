<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:53:59 2017

@author: User
"""

#Lists that contain the elements needed to describe a Calendar
Weekdays = ["EndOfWeek","Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Thirty_Days = ["Apr","Jun","Sep","Nov"]
ThiryOne_Day = ["Jan","Mar","May","Jul","Aug","Oct","Dec"]
Days = [x for x in range(1,32)]
Years = [x for x in range(1901,2002)]

#Initial Date
Calendar = {"Day":1, "Month":"Jan", "Year":1901,"Weekday":"Tue"}

#Placeholder Variables for Indices
Year = 0
Month = 0
Weekday = 2 #Starting at 2 because our first day is a Tuesday
Day = 0

#Variable to hold result
Counter = 0

#Variable for Leap_Year
Leap_Year = False

while Years[Year] < 2001:
    #Print the Day at the beginning of each iteration
    print(Calendar)
    #Move weekday back to beginning of Days list and update counter
    if Calendar["Weekday"] == "Sun":
        if Calendar["Day"] == 1:
            Counter += 1
            Weekday = 0
        else:
            Weekday = 0
    #Check if Leap Year 
    if Years[Year] % 4 == 0:
        Leap_Year = True
    else:
        Leap_Year = False
    #Special Case for February 28th
    if Calendar["Month"] == "Feb" and Calendar["Day"] == 28:
        if Leap_Year:
            Day += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Weekday"] = Weekdays[Weekday]
        else:
            Day = 0
            Month += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Month"] = Months[Month]
            Calendar["Weekday"] = Weekdays[Weekday]
    #Special Case for February 29th
    elif Calendar["Month"] == "Feb" and Calendar["Day"] == 29:
        Day = 0
        Month += 1
        Weekday += 1
        Calendar["Day"] = Days[Day]
        Calendar["Month"] = Months[Month]
        Calendar["Weekday"] = Weekdays[Weekday]
    #Special Case for December 31st
    elif Calendar["Month"] == "Dec" and Calendar["Day"] == 31:
        Month = 0
        Day = 0
        Weekday += 1
        Year += 1
        Calendar["Day"] = Days[Day]
        Calendar["Month"] = Months[Month]
        Calendar["Weekday"] = Weekdays[Weekday]
        Calendar["Year"] = Years[Year]
    #Case for Day 30s
    elif Calendar["Day"] == 30:
        if Calendar["Month"] not in Thirty_Days:
            Day += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Weekday"] = Weekdays[Weekday]
        else:
            Day = 0
            Month += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Month"] = Months[Month]
            Calendar["Weekday"] = Weekdays[Weekday]
    #Case for Day 31s
    elif Calendar["Day"] == 31:
        Day = 0
        Month += 1
        Weekday += 1
        Calendar["Day"] = Days[Day]
        Calendar["Month"] = Months[Month]
        Calendar["Weekday"] = Weekdays[Weekday]
    #Case for Progressing Day
    else:
        Day += 1
        Weekday += 1
        Calendar["Day"] = Days[Day]
        Calendar["Weekday"] = Weekdays[Weekday]
    


print(Counter)
            
            
    
        
    
=======
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:53:59 2017

@author: User
"""

#Lists that contain the elements needed to describe a Calendar
Weekdays = ["EndOfWeek","Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Thirty_Days = ["Apr","Jun","Sep","Nov"]
ThiryOne_Day = ["Jan","Mar","May","Jul","Aug","Oct","Dec"]
Days = [x for x in range(1,32)]
Years = [x for x in range(1901,2002)]

#Initial Date
Calendar = {"Day":1, "Month":"Jan", "Year":1901,"Weekday":"Tue"}

#Placeholder Variables for Indices
Year = 0
Month = 0
Weekday = 2 #Starting at 2 because our first day is a Tuesday
Day = 0

#Variable to hold result
Counter = 0

#Variable for Leap_Year
Leap_Year = False

while Years[Year] < 2001:
    #Print the Day at the beginning of each iteration
    print(Calendar)
    #Move weekday back to beginning of Days list and update counter
    if Calendar["Weekday"] == "Sun":
        if Calendar["Day"] == 1:
            Counter += 1
            Weekday = 0
        else:
            Weekday = 0
    #Check if Leap Year 
    if Years[Year] % 4 == 0:
        Leap_Year = True
    else:
        Leap_Year = False
    #Special Case for February 28th
    if Calendar["Month"] == "Feb" and Calendar["Day"] == 28:
        if Leap_Year:
            Day += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Weekday"] = Weekdays[Weekday]
        else:
            Day = 0
            Month += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Month"] = Months[Month]
            Calendar["Weekday"] = Weekdays[Weekday]
    #Special Case for February 29th
    elif Calendar["Month"] == "Feb" and Calendar["Day"] == 29:
        Day = 0
        Month += 1
        Weekday += 1
        Calendar["Day"] = Days[Day]
        Calendar["Month"] = Months[Month]
        Calendar["Weekday"] = Weekdays[Weekday]
    #Special Case for December 31st
    elif Calendar["Month"] == "Dec" and Calendar["Day"] == 31:
        Month = 0
        Day = 0
        Weekday += 1
        Year += 1
        Calendar["Day"] = Days[Day]
        Calendar["Month"] = Months[Month]
        Calendar["Weekday"] = Weekdays[Weekday]
        Calendar["Year"] = Years[Year]
    #Case for Day 30s
    elif Calendar["Day"] == 30:
        if Calendar["Month"] not in Thirty_Days:
            Day += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Weekday"] = Weekdays[Weekday]
        else:
            Day = 0
            Month += 1
            Weekday += 1
            Calendar["Day"] = Days[Day]
            Calendar["Month"] = Months[Month]
            Calendar["Weekday"] = Weekdays[Weekday]
    #Case for Day 31s
    elif Calendar["Day"] == 31:
        Day = 0
        Month += 1
        Weekday += 1
        Calendar["Day"] = Days[Day]
        Calendar["Month"] = Months[Month]
        Calendar["Weekday"] = Weekdays[Weekday]
    #Case for Progressing Day
    else:
        Day += 1
        Weekday += 1
        Calendar["Day"] = Days[Day]
        Calendar["Weekday"] = Weekdays[Weekday]
    


print(Counter)
            
            
    
        
    
>>>>>>> origin/master
        