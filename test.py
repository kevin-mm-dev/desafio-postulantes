from bs4 import BeautifulSoup
import requests
import json

page_url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html'
data_table_url='https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.csv?_=1651002576188'
html_text = requests.get(page_url).text
data_table_text = requests.get(data_table_url).text
soup = BeautifulSoup(html_text, 'html.parser')
mycontent= soup.find_all("div", {"class": "contenido"})

number_columns=11
lines=data_table_text.split('\r\n')
metas=soup.find_all('meta')
desc=soup.p

for x in metas:
    #print(x)
    #print(x.content)
    if x.name=='description':
        print('encontrado')
        print(x)
        
#print(soup.find_all('meta'))
#print(data_table_text)

class Header:
    def __init__(self, _column1, _column2, _column3, _column4, _column5, _column6, _column7,_column8,_column9,_column10,_column11):
        self.column1 = _column1
        self.column2 = _column2
        self.column3 = _column3
        self.column4 = _column4
        self.column5 = _column5
        self.column6 = _column6
        self.column7 = _column7
        self.column8 = _column8
        self.column9 = _column9
        self.column10 = _column10
        self.column11 = _column11

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
array_header=lines[0].split(';')
header_table=Header(array_header[0],array_header[1],array_header[2],array_header[3],array_header[4],array_header[5],array_header[6],array_header[7],array_header[8],array_header[9],array_header[10])
#print(header_table)
del lines[0]

#print(lines)
class NewLine:
    def __init__(self, _column1, _column2, _column3, _column4, _column5, _column6, _column7,_column8,_column9,_column10,_column11):
        self.column1 = _column1
        self.column2 = _column2
        self.column3 = _column3
        self.column4 = _column4
        self.column5 = _column5
        self.column6 = _column6
        self.column7 = _column7
        self.column8 = _column8
        self.column9 = _column9
        self.column10 = _column10
        self.column11 = _column11

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
my_lines = [] #Contains all the lines



for line in lines:
    try:
        arr_line=line.split(';')
        if len(arr_line)>1:
            li=NewLine(arr_line[0],arr_line[1],arr_line[2],arr_line[3],arr_line[4],arr_line[5],arr_line[6],arr_line[7],arr_line[8],arr_line[9],arr_line[10])
            li.column1=arr_line[0]
            my_lines.append(li)
    except:
        print("Error")
        

class Data:
    def __init__(self, _title, _desc, _table_header, _table_body,):
        self.title = _title
        self.desc = _desc
        self.table_header = _table_header
        self.table_body = _table_body
        
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


res=Data(metas[3]['content'],desc.contents[0],header_table,my_lines)

jsonStr = json.dumps(res.toJson(), indent=4)
resJson= json.loads(jsonStr)

print(resJson) #Resultado en JSON
#return resJson