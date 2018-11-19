import requests
from bs4 import BeautifulSoup
from datetime import date

classSuperList = list()


#url = 'http://catalog.csuchico.edu/viewer/search/courses.aspx?cycle=18&subject=all&keywords=&psize=00&pnum=1'
url = 'http://catalog.csuchico.edu/viewer/search/courses.aspx?cycle=18&subject=all&keywords=&psize=50'
response = requests.get(url)
html_response = BeautifulSoup(response.text, 'html.parser')
class_list = html_response.find_all('tr', class_='slide_link courseheading')
classSuperList.append(class_list)

for i in range(len(classSuperList[0])):
	singleClass = classSuperList[0][i]
	userID = 1;
	todaysDate = str(date.today())
	#Make term take solution
	className = singleClass.find('td', class_='courseTitle').text
	courseInfo = (singleClass.a.text).split(" ")
	courseNum = courseInfo[1].strip()
	courseSubject = courseInfo[0].strip()
	school = 'Chico State'
	#review solution
	#teacherName solution
	reviewerName = 'admin'