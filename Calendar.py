#This program will:
#  - print a welcome message to the user
#  - prompt the user to view, add, update, or delete an event on the calendar
#  - depending on the user's input: view, add, update, or delete an event on the calendar
#  - the program should never terminate unless the user decides to exit

from time import sleep, strftime
FIRST_NAME = "Mark"

calendar = {

}

def welcome():
  print ("Hello, welcome to this calendar program!")
  print ("The calendar is now opening")
  sleep(1)
  print (strftime("%A %B %d, %Y"))
  print (strftime("%I:%M:%S"))
  sleep(1)
  print ("What would you like to do?")

def start_calendar():
  print (welcome())
  start = True
  while start is True:
    user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print ("The calendar is empty")
      else:
        print (calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print ("The update was successful!")
      print (calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if int(len(date)) > 10 or int(date[6:11]) < int(strftime("%Y")):
        print ("You entered an invalid date.")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print ("The calendar is empty.")
      else:
        event = input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print ("The event was successfully deleted.")
            print (calendar)
          else:
            print ("An incorrect event was specified.")
    elif user_choice == "X":
        print ("The calendar program is ending.")
        start = False
    else:
        print ("An invalid command was entered.")
        start = False

start_calendar()