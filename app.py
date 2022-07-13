from ast import While
import schedule
import time

def job():
    print("Make your bed")

def task():
    print("Sweep the floor")

def arrange():
    print("Rearrange the living room") 

def wash():
    print("wash the dishes") 

def cook():
    print("cook breakfast") 

    #time
    schedule.every().day.at("8:00").do(job)
    schedule.every().day.at("8:30").do(task)
    schedule.every().day.at("9:00").do(wash)
    schedule.every().day.at("9:30").do(cook)

    
    

    while True:
        schedule.run_pending()
        time.sleep(1)