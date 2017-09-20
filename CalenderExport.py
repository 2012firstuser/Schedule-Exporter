# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:54:27 2017
WPI Outlook Schedule Importer A and B term 2017
@author: Akash Shaji
"""


from datetime import datetime, date, time, timedelta
from ics import eventlist, Event, Calendar

"""
Takes in the name of the course, the term,and the days & locations part of schedule planner and parses it.
Can export the a term data to file
Sample input:
>>CS 1102
>>a
>>MTThF 9:00am - 9:50am - FL PH-LWR
"""
class classInfo:
    name = None
    begin = None
    end = None
    days = ""
    location = None
    evList = eventlist.EventList()
    term = None
    def __init__(self,name,term, dayAndLocation):
        self.name = name
        while(term.lower() != "a" and term.lower() != "b"):
            term = input("Please enter a or b term.")
        self.term = term.lower()
        
        while(dayAndLocation[0] != " "):
            self.days += dayAndLocation[0]
            dayAndLocation = dayAndLocation[-len(dayAndLocation)+1:]
        dayAndLocation = dayAndLocation[-len(dayAndLocation)+1:]
        
        tempTime = ""
        while(dayAndLocation[0] != " "):
            tempTime += dayAndLocation[0]
            dayAndLocation = dayAndLocation[-len(dayAndLocation)+1:]
        self.begin = datetime.strptime(tempTime,"%I:%M%p").time()
        #couldn't get timezones working with this library so I went with this workaround.
        self.begin = self.begin
        dayAndLocation = dayAndLocation[-len(dayAndLocation)+3:]
            
        tempTime = ""
        while(dayAndLocation[0] != " "):
            tempTime += dayAndLocation[0]
            dayAndLocation = dayAndLocation[-len(dayAndLocation)+1:]  
        self.end = datetime.strptime(tempTime,"%I:%M%p").time()
        self.end = self.end.replace(tzinfo=None)
        self.location = dayAndLocation[-len(dayAndLocation)+3:]
        
    def exportClass(self,day):
        e = Event()
        e.name = self.name
        e.begin = datetime.combine(day,self.begin)  + timedelta(hours=4)
        e.end = datetime.combine(day,self.end) + timedelta(hours=4)
        e.location = self.location
        return(e)
    def exportToFile(self):
        c = Calendar()
        
        #e = self.exportClass(datetime(year,month,date))
        #c.events.append(e) 
        if(self.term == "a"):
            if(self.days.find('M') >-1):
                e = self.exportClass(datetime(2017,8,24))
                c.events.append(e)
                e = self.exportClass(datetime(2017,8,28))
                c.events.append(e)
                tempday = datetime(2017,9,11)
                e = self.exportClass(tempday)
                c.events.append(e)
                itterations = 4
                for x in range (0,itterations):
                    tempday = tempday + timedelta(days=7)
                    e = self.exportClass(tempday)
                    c.events.append(e)
            if(self.days.find('T') >-1):
                if(not (self.days[self.days.find('T')+ 1] == 'h')):
                    tempday = datetime(2017,8,29)
                    e = self.exportClass(tempday)
                    c.events.append(e)
                    itterations = 6
                    for x in range (0,itterations):
                        tempday = tempday + timedelta(days=7)
                        e = self.exportClass(tempday)
                        c.events.append(e)
            if(self.days.find('W') >-1):
                tempday = datetime(2017,8,30)
                e = self.exportClass(tempday)
                c.events.append(e)
                itterations = 6
                for x in range (0,itterations):
                    tempday = tempday + timedelta(days=7)
                    e = self.exportClass(tempday)
                    c.events.append(e)
            if(self.days.find('T') > -1):
                if((self.days.find('T',self.days.find('T') + 1) > -1) or (self.days[self.days.find('T')+ 1] == 'h')):
                    tempday = datetime(2017,8,31)
                    e = self.exportClass(tempday)
                    c.events.append(e)
                    itterations = 6
                    for x in range (0,itterations):
                        tempday = tempday + timedelta(days=7)
                        e = self.exportClass(tempday)
                        c.events.append(e)
            if(self.days.find('F') > -1):
                tempday = datetime(2017,8,25)
                e = self.exportClass(tempday)
                c.events.append(e)
                itterations = 6
                for x in range (0,itterations):
                    tempday = tempday + timedelta(days=7)
                    e = self.exportClass(tempday)
                    c.events.append(e) 
        if(self.term == "b"):
            if(self.days.find('M') >-1):
                e = self.exportClass(datetime(2017,8,24))
                c.events.append(e)
                e = self.exportClass(datetime(2017,8,28))
                c.events.append(e)
                tempday = datetime(2017,9,11)
                e = self.exportClass(tempday)
                c.events.append(e)
                itterations = 4
                for x in range (0,itterations):
                    tempday = tempday + timedelta(days=7)
                    e = self.exportClass(tempday)
                    c.events.append(e)
            if(self.days.find('T') >-1):
                if(not (self.days[self.days.find('T')+ 1] == 'h')):
                    tempday = datetime(2017,8,29)
                    e = self.exportClass(tempday)
                    c.events.append(e)
                    itterations = 6
                    for x in range (0,itterations):
                        tempday = tempday + timedelta(days=7)
                        e = self.exportClass(tempday)
                        c.events.append(e)
            if(self.days.find('W') >-1):
                tempday = datetime(2017,8,30)
                e = self.exportClass(tempday)
                c.events.append(e)
                itterations = 6
                for x in range (0,itterations):
                    tempday = tempday + timedelta(days=7)
                    e = self.exportClass(tempday)
                    c.events.append(e)
            if(self.days.find('T') > -1):
                if((self.days.find('T',self.days.find('T') + 1) > -1) or (self.days[self.days.find('T')+ 1] == 'h')):
                    tempday = datetime(2017,8,31)
                    e = self.exportClass(tempday)
                    c.events.append(e)
                    itterations = 6
                    for x in range (0,itterations):
                        tempday = tempday + timedelta(days=7)
                        e = self.exportClass(tempday)
                        c.events.append(e)
            if(self.days.find('F') > -1):
                tempday = datetime(2017,8,25)
                e = self.exportClass(tempday)
                c.events.append(e)
                itterations = 6
                for x in range (0,itterations):
                    tempday = tempday + timedelta(days=7)
                    e = self.exportClass(tempday)
                    c.events.append(e) 
        with open(self.name + self.days +'.ics', 'w') as f:
            f.writelines(c)
cont = ""
while(not cont == "n"):
     name = input("Please enter the name of the class: ")           
     term = input("Please enter a or b term: ")      
     cont = ""
     while(not cont == "n"):
         schedule = input("Please copy the dates and locations section from wpi.collegescheduler.com.\nIt should look like this: \"MTThF 9:00am - 9:50am - FL PH-LWR\"\n") 
         c = classInfo(name,term,schedule)
         c.exportToFile()
         cont = input("Add another time for this class? (y//n)")
     cont = input("Do another class? (y\\n) :")
    
#with open('my.ics', 'w') as my_file:
     #my_file.writelines(c.getDates)

#c = eventlist.EventList()
#c.append()
