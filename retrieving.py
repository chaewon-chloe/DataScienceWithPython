import urllib.request as ulre
import re
from bs4 import BeautifulSoup
url = ulre.urlopen('https://en.wikipedia.org/wiki/Ann_Arbor,_Michigan')
html_parsed = BeautifulSoup(url, 'html.parser')

regex = re.compile(r'Climate data for ')
for i in html_parsed.find_all('table'):
    if i.th is not None:
        if regex.match(i.th.get_text()) is not None:
            climate = i
            break
            
print(climate.prettify())

def retrieve_climate_table(url):
    import urllib.request
    from bs4 import BeautifulSoup
    
    try:
        city = urllib.request.urlopen(url)
    except:
        raise ValueError("The input URL cannot be opened.")
    if city.getcode()!=200:
        raise ValueError("The input URL is not available. Code: %d" % city.getcode())
    else:
        parsed = BeautifulSoup(city, 'html.parser')

        regex = re.compile(r'Climate data for ')
        for i in parsed.find_all('table'):
            if i.th is not None:
                if regex.match(i.th.get_text()) is not None:
                    return i
            if i.caption is not None:
                if regex.match(i.caption.get_text()) is not None:
                    return i
        return None 

retrieve_climate_table('https://en.wikipedia.org/wiki/Hyderabad') 

def list_climate_table_row_names(url):
    table = retrieve_climate_table(url)
    if table == None:
        return None
    else:
        rows = table.find_all('th',attrs={'scope':'row'})
        return [i.get_text() for i in rows]

list_climate_table_row_names('https://en.wikipedia.org/wiki/Hyderabad')

def get_climate_information(url,row):
    table = retrieve_climate_table(url)
    row_names = list_climate_table_row_names(url)
    
    if row not in row_names:
        raise ValueError("There is not the row '{%s}' in the table!", row.strip('\n'))
    elif table == None:
        raise ValueError("There is not a climate data table in this URL!")
    else:
        def has_attr(tag):
            return tag.has_attr('scope') and row in tag.text
        nodes = table.find_all(has_attr)[0].find_parents('tr')[0] 
        value_dic = dict()
        dic_i = ['01Jan','02Feb','03Mar','04Apr','05May','06Jun','07Jul','08Aug','09Sep','10Oct','11Nov','12Dec','Year']
        for i,j in zip(dic_i,nodes.find_all('td')):
            value_dic[i] = j.get_text().strip('\n')
       return value_dic

get_climate_information('https://en.wikipedia.org/wiki/Hyderabad','Average low °C (°F)\n')
