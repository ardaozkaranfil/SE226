inputSecond = input("Please enter a large integer representing total number of seconds.")

seconds = int(inputSecond) % 60
minutes = int(inputSecond) // 60 % 60
hours = int(inputSecond) // 3600

    print(inputSecond + " seconds is " + str(hours) + " hours," + str(minutes) + " minutes," + str(seconds) + " seconds.")