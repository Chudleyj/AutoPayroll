import pyautogui
import time 
import webbrowser 

webbrowser.open('https://mysecretlink)

for x in range (0,3):
	pyautogui.click(x=1087, y=165) #Employee Tab

for x in range(0,3):
	time.sleep(0.25)
	pyautogui.click(x=1271, y=409)#Part Time Employee Timesheet 

time.sleep(0.25)	
pyautogui.click(x=637,y=449)#Select Time Period

time.sleep(0.25)
pyautogui.click(x=636,y=463)#Choose Date Dropdown

for x in range(0,3):
	time.sleep(0.25)
	pyautogui.click(x=1063,y=500)#Adjust timesheet for this period
	
time.sleep(1)
for x in range(0,3):
	pyautogui.press('tab')

for x in range(0,11): #Jump to Monday
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


