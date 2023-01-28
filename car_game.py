command = ""
started = False                     #Making car stopped in initial state
while True:
    command = input("> ").lower()   #Receiving input from user
    if command == "start":
        if started:                 #Does car already started state?
            print("Car is already started .....")
        else:
            started = True          #Make the state started
            print("Car Started ....")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car StoppedQ")
    elif command =="help":
        print("""
Start - To start the car
Stop - To stop the car
quit - To quit
        """)
    elif command =="quit":
        break
    else:
        print("I don't understand that")

