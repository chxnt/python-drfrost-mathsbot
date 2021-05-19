import selenium
import keyboard
from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from keyboard import press
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driv = webdriver.Chrome(ChromeDriverManager().install())



driv.get("https://www.drfrostmaths.com/timestables-game.php")
time.sleep(1)
email = driv.find_element_by_name("login-email")
login = driv.find_element_by_name("login-password")
time.sleep(2)
email.send_keys("") # enter your email/username here
login.send_keys("") # enter your password here cba adding inputs so u have to enter it here (;
time.sleep(0.5)
press('enter')

limit = 20
answerele = driv.find_element_by_id("calculator-display")
questionele = driv.find_element_by_xpath('//*[@id="question"]')
questionele.click()
time.sleep(0.3)
questionelement = driv.find_element_by_xpath('//*[@id="question"]')
count = 0
while True:
	question = questionelement.text 
	questionspl = question.split(' ') # this section of code needs to turn the string into a list so we can go through each item we do this because dr frost maths uses '÷' and '×' instead of '/' '*' so if we find a ÷ or × we replace the index of 1 which it will always be at with the 
									  # correct operators then we need to put it back into a string so the eval function can work this is a very basic bot but fun to do

	for i in questionspl:
		if i == '÷':
			questionspl[1] = '/'
			ques = ' '.join(questionspl)
	

	for x in questionspl:
		if x == '×':
			questionspl[1] = '*'
			ques = ' '.join(questionspl)

	

	print(f'quession list is {questionspl}')
	print(f'list to sring is{ques}')
	ans = str(int(eval(ques)))
	count += 1
	answerele.clear()
	answerele.send_keys(ans)
	# may want to add time.sleep() here as it can be too fast for the website
	print(f'count is {str(count)}')


