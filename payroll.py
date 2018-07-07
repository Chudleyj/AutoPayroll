import pyautogui
import time
import webbrowser

webbrowser.open('My payroll site link')
time.sleep(5)
for x in range (0,7):
    pyautogui.press('tab') #Employees Tab
pyautogui.press('enter')

for x in range(0,30):
    time.sleep(0.25)
    pyautogui.press('tab')#Part Time Employee Timesheet
pyautogui.press('enter')

time.sleep(0.25)
for x in range(0,16):
    pyautogui.press('tab')#Select Time Period
time.sleep(0.25)
for x in range(0,2):
    pyautogui.press('down')#Choose Date Dropdown
    time.sleep(0.25)
pyautogui.press('enter')

time.sleep(0.5)
pyautogui.press('tab')#Adjust timesheet for this period
pyautogui.press('enter')

time.sleep(1)
for x in range(0,3):
    pyautogui.press('tab')

for x in range(0,12): #Jump to Monday
    pyautogui.press('tab')

for x in range(0,10): #Monday, 1st column
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Monday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Monday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Monday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')

for x in range(0,3):
    pyautogui.press('tab') #Tuesday, 1st column

for x in range(0,10):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Tuesday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Tuesday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Tuesday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')

for x in range(0,3):
    pyautogui.press('tab') #Wednesday, 1st column

for x in range(0,10):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Wednesday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Wednesday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Wednesday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')

for x in range(0,3):
    pyautogui.press('tab') #Thursday, 1st column

for x in range(0,10):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Thursday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Thursday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #Thursday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')

for x in range (0,21):
    pyautogui.press('tab')

for x in range(0,10): #2nd Monday, 1st column
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Monday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Monday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Monday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')

for x in range(0,3):
    pyautogui.press('tab') #2nd Tuesday, 1st column

for x in range(0,10):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Tuesday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Tuesday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Tuesday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')

for x in range(0,3):
    pyautogui.press('tab') #2nd Wednesday, 1st column

for x in range(0,10):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Wednesday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Wednesday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Wednesday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')

for x in range(0,3):
    pyautogui.press('tab') #2nd Thursday, 1st column

for x in range(0,10):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Thursday, 2nd column
for x in range(0,20):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Thursday, 3rd column
for x in range(0,22):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab') #2nd Thursday, 4th column
for x in range(0,37):
    pyautogui.press('down')
pyautogui.press('enter')
