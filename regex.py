import urllib.request as ulre
import re
from bs4 import BeautifulSoup

import urllib.request as ulre
import re
response = ulre.urlopen('http://www.greenteapress.com/thinkpython/code/words.txt')
data = response.read()
ASCII = data.decode('ASCII')
words = re.findall(r'\w+', ASCII)

four_consecutive_consonants = re.compile(r'(^.*[aeiouy][^aeiouy]{4}[aeiouy].*$)|(^[^aeiouy]{4}[aeiouy].*$)|(^.*[aeiouy][^aeiouy]{4}$)|(^[^aeiouy]{4}$)')
print(len([words[i] for i in range(len(words)) if len(four_consecutive_consonants.findall(words[i]))>0]))

gadsby = re.compile(r'^[^e]*$')
print(len([words[i] for i in range(len(words)) if len(gadsby.findall(words[i]))> 0]))

vowel_vowel = re.compile(r'^[aeiou][^aeiou]*[aeiou]$')
print(len([words[i] for i in range(len(words)) if len(vowel_vowel.findall(words[i]))> 0]))

#bookends : last two characters are the first two characters in reverse order (ex) repeater, stats
# be careful of the cases in which the word is length less or equal to 3
# greater than 3: abba abcba / equal to 3: aba / less than 3: aa or a(not inclusive)
bookends = re.compile(r'^(\w)(\w).*\2\1$|^(\w)(\w)\3$|^(\w)\5$')
print(len([words[i] for i in range(len(words)) if len(bookends.findall(words[i]))> 0]))

import urllib.request as ulre
import re
SkypeIRC_url = ulre.urlopen("http://www-personal.umich.edu/~klevin/teaching/Winter2018/STATS701/SkypeIRC.txt")
data = SkypeIRC_url.read().decode('utf-8').splitlines()
data[0:5]

n_packets = len(data)
n_packets

ip_regex = re.compile(r'\b((25[0-5]\.|2[0-4][0-9]\.|1[0-9][0-9]\.|[1-9]?[0-9]\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))\b')
ip_ads = [j[0] for i in data for j in ip_regex.findall(i)] 
set(ip_ads)

ip_addresses = len(set(ip_ads))
ip_addresses

def get_packets_by_regex(s):
    if isinstance(s, str) == False: 
        raise TypeError('Input must be a string.')
    regex = re.compile(s)
    return [i for i in data if regex.search(i) is not None]
    
len(get_packets_by_regex(r'comcast'))

import matplotlib.pyplot as plt
%matplotlib inline

times = [float(i.split()[1]) for i in data]

plt.hist(times, bins = range(325), label='Traffic Recording')
plt.ylabel('Number of Packets')
plt.xlabel('Time(seconds)')
plt.title('Packets appeared in each second of recording')
plt.show()

