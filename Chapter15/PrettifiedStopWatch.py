#! python3
# PrettifiedStopWatch.py - A pretty stopwatch program

import time, pyperclip

# Display the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press CTRl-C to quit.')

# Press enter to begin
input()
print('Started.')
# get the first lap's start time
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lap = 'lap # {} {} ({})'.format((str(lapNum)+ ':').ljust(3),
                                         str(totalTime).rjust(5),str(lapTime).rjust(6))
        print(lap, end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
        pyperclip.copy(lap)
except KeyboardInterrupt:
    # Handle the Ctrl+C exception to keep its error message from displaying
    print('\nDone.')
