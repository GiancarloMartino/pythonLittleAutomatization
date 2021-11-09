# A little program in python for those who spend too much time on the computer and forget that overexposure 
# will kill him in a short time. :D


import time
import webbrowser
pause_totali=4
conta_pause=0
print("BreakMaker is running...")
while(conta_pause < pause_totali):
    time.sleep(1500) 
    webbrowser.open("https://www.youtube.com/watch?v=Cdx16vY7DZc")
    conta_pause += 1


# the time value is in seconds, and you can adjust it!