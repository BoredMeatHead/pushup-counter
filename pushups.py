print("How many pushups do you want to do today?")
pushups_today = int(input()) #gets the amount of pushup for this workout

pushups_done = 0
pushup_calorie = 0.36 #calorie for each pushup


while pushups_today > pushups_done:
    print("How many pushups did you just did?")
    x = int(input()) #gets input from user how many pushups he/she just did
    pushups_done += x #adds it to the variable
    print("In total you did", pushups_done, "pushups")
    if pushups_done == pushups_today or pushups_done > pushups_today:

        print("Great you finished your workout!")
        print("Total calorie burn:" " " "{0:.1f}".format(pushups_done*pushup_calorie))
