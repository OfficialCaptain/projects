currentTimestr = input("What is the current time?: ")
waitingTimestr = input("How many hours do you have to wait?: ")

currentTimeint = int(currentTimestr)
waitingTimeint = int(waitingTimestr)

hours = waitingTimeint + currentTimeint
sumo = hours % 24
print(sumo)
