from pywinauto import Application
import datetime
import pandas as pd
import sys
sys.path.append('C:/Users/sauds/Desktop/OPen_CV_Project1-main')
from main_video import *
import time


# Read CSV file  to data frame and specify rows
data = pd.read_csv('C:/Users/sauds/Desktop/OPen_CV_Project1-main/Students_Data.csv')
data2 = pd.DataFrame(data, columns=['Name', 'Reg Number', 'Time IN', 'Date IN', 'Time OUT', 'Date OUT', 'Batch', 'Faculty'])
# This list is storing data send by arduino sensor
lines = []


# This code is for opening the CoolTerm App to connect with arduino
app = Application(backend="uia").start('C:/Users/sauds/Desktop/OPen_CV_Project1-main/CoolTermWin64Bit/CoolTerm')
# Wait for the app to launch and become responsive
app.wait_cpu_usage_lower(threshold=5, timeout=30)
# Get a reference to the main window
main_window = app.top_window()
# Click on the Connect Button
button = main_window.child_window(title="Connect", control_type="Button")
button.click()
# This minimize the CoolTerm Window
input("Start the connection and enter any key to proceed")






# This function is Loading all the images present in Images folder
Function1()


while 1:

   
    Access = 0
    with open('C:/Users/sauds/Desktop/OPen_CV_Project1-main/sensor_data.txt', 'r') as file:
        lines = file.readlines()
        Access = lines[-1].strip()

    if Access == 'Entry':

        name, reg, batch, faculty = Function2()
        Date = datetime.date.today()
        Date = Date.strftime("%d/%m/%Y")
        Time = datetime.datetime.now().time()
        Time = Time.strftime("%I:%M %p")

        if name != "\\\\\\\\Unknown////////":
            new_row = {'Name': name, 'Reg Number': reg, 'Time IN': Time, 'Date IN': Date,'Time OUT': 'NA', 'Date OUT': 'NA', 'Batch': batch, 'Faculty': faculty}
            #data2 = data2.append(new_row, ignore_index=True)
            data2 = pd.concat([data2, pd.DataFrame([new_row])], ignore_index=True)

    elif Access == 'Exit':

        name, reg, batch, faculty = Function2()
        Date = datetime.date.today()
        Date = Date.strftime("%d/%m/%Y")
        Time = datetime.datetime.now().time()
        Time = Time.strftime("%I:%M %p")

        if name != "\\\\\\\\Unknown////////":
            new_row = {'Name': name, 'Reg Number': reg, 'Time IN': 'NA', 'Date IN': 'NA','Time OUT': Time, 'Date OUT': Date, 'Batch': batch, 'Faculty': faculty}
            #data2 = data2.append(new_row, ignore_index=True)
            data2 = pd.concat([data2, pd.DataFrame([new_row])], ignore_index=True)

    elif Access == 'e':
        data2.to_csv('C:/Users/sauds/Desktop/OPen_CV_Project1-main/Students_Data.csv',mode='a', header=False, index=False)
        app.kill()
        time.sleep(.5)
        with open('C:/Users/sauds/Desktop/OPen_CV_Project1-main/sensor_data.txt', 'r+') as file:
            # Truncate the file to zero length
            file.truncate(0)
        break

    else:
        print('Invalid Input ')
        continue


