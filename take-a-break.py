import time
import webbrowser
total_breaks= 3
break_count= 0
print("The current time is "+time.ctime())
count = 0
while (break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count = break_count + 1;
