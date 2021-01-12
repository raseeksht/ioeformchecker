import  json
import requests
from bs4 import BeautifulSoup

url = "https://entrance.ioe.edu.np/Students/Review"
jsonFile = 'mydata.json'
f = open(jsonFile)

a = json.load(f)

headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
}


if a["fileinput"] == True:
	data =  {
	"LastName":a["lastname"],
	"BirthDateBS":a['BirthDateBS'],
	"BirthDateAD":a["BirthDateAD"],
	"BirtDate":"on",
	"IdentificationNo":a['idNo'],
	"IsPrint":""
	}

else:
	data =  {
	"LastName":input("lastname: "),
	"BirthDateBS":input("BirthDateBS: "),
	"BirtDate":"on",
	"IdentificationNo":input("id no. "),
	"BirthDateAD":input("BirthDateAD: "),
	"IsPrint":""
	}


r = requests.post(url,data=data,headers=headers)
soup  = BeautifulSoup(r.content,'html.parser')
try:
	alld = soup.find("div",class_="status_info")
	res = alld.div.div.p.get_text()
	print(" ".join(res.split()))
except Exception as e:
	print(soup)
	print("ok vako xaina")
