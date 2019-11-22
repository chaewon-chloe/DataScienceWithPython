from mrjob.job import MRJob
import re

regex = re.compile(r'[A-Za-z]+')

class MRWordCount(MRJob):
    def mapper(self, _, line):
        for word in regex.findall(line):
            yield word.lower(), 1
            
    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__=='__main__':
    MRWordCount.run()

from mrjob.job import MRJob
from functools import reduce

class MRSummaryStats(MRJob):
    
    def mapper(self, _,line):
        yield int(line.split("\t")[0]), float(line.split("\t")[1])
  
    def reducer(self, key, values):
        COUNT, SUM, SQR = 0, 0.0, 0.0
        for i in values:
            COUNT += 1
            SQR += i**2
            SUM += i
        yield key,(COUNT, SUM/COUNT, SQR/COUNT-(SUM/COUNT)**2)

if __name__ == '__main__':
    MRSummaryStats.run()
    
    

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("darwin_word_counts.txt", delimiter="\t", names = ['word','count'])
data = data.sort_values('count', ascending = False).reset_index()
data['log rank']=np.log(list(data.index+1))
data['rank']=list(data.index+1)
data['log count']=np.log(data['count'])

%matplotlib inline
f = plt.figure(figsize=(8,8))

plt.plot(data['rank'],data['count'],'-r')
plt.xscale('log')
plt.yscale('log')

plt.title("Plot of word counts vs. word rank on a log-log scale", fontsize=14)
plt.xlabel("Log rank (Axis label: non-logarithm rank)",fontsize=13)
plt.ylabel("Log counts (Axis label: non-logarithm count)",fontsize=13)
plt.show()

f.savefig("zipf.pdf")

import scipy.stats as st
import matplotlib.pyplot as plt

pops = pd.read_csv("summary_large.txt", delimiter = "\t\[|,|\]",
                  names = ['label','n','sample mean', 'sample variance','NaN']).drop(columns = ['NaN'])
pops = pops.sort_values('label')

%matplotlib inline
f = plt.figure(figsize=(12,8))                     
plt.errorbar(pops.label, pops['sample mean'], yerr=st.norm.ppf(1-0.05/2)*(pops['sample variance']**0.5)/(pops['n']**0.5), fmt='o')
plt.title("95% CI for sample means of the population", fontsize=15)
plt.xlabel("Label",fontsize=15)
plt.ylabel("Sample mean",fontsize=15)
plt.show()
f.savefig("populations.pdf")
