from bs4 import BeautifulSoup
import requests, openpyxl

excel1 = openpyxl.Workbook()
sheet1 = excel1.active
sheet1.title = 'Images Links'
sheet1.append(['Images Link'])

excel2 = openpyxl.Workbook()
sheet2 = excel2.active
sheet2.title = 'Anchors Links'
sheet2.append(['Anchors Link'])

url = "https://plain-train-pike.cyclic.app/"

req = requests.get(url)
hcont = req.content

be_so = BeautifulSoup(hcont, 'html.parser')

# All Images links

im_li = be_so.find_all('img')


for ili in im_li:
    if ili.get('src') is not None:
        ili_text = "https://plain-train-pike.cyclic.app/"+ili.get('src')
        print(ili_text)
        sheet1.append([ili_text])


# All a tags links

atag = be_so.find_all('a')

for li in atag:
    if(li.get('href') != '#'):
        if li.get('href') is not None:
            li_text = "https://plain-train-pike.cyclic.app"+li.get('href')
            print(li_text)
            sheet2.append([li_text])


# All the text from page

#print(be_so.get_text())

# All the elements with class box

#print(be_so.find_all("div", class_="box"))

# Classes of any element

#print(be_so.find('div')['class'])

# All p tags text

gt = be_so.find_all('p')
for pa in gt:
    print(pa.get_text(strip=True))
    

excel1.save('Images links.xlsx')
excel2.save('Anchors links.xlsx')
