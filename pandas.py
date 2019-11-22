import pandas as pd
mlb_df = pd.read_csv('GL2018.TXT', header=None)
#mlb_df = mlb_df.iloc[:,[4,7,9,10]]
mlb_df = mlb_df.rename({4: 'v_league', 7: 'h_league', 9: 'v_score', 10: 'h_score'}, axis = 'columns')

## Add an extra column encoding whether a given game is AL vs AL, NL vs NL or mixed.
mlb_df['MatchType'] = 'mixed'
for i in range(len(mlb_df)):
    if mlb_df.loc[i,'v_league'] == mlb_df.loc[i,'h_league'] == "NL":
        mlb_df.loc[i,'MatchType'] = 'NL vs NL'
    elif mlb_df.loc[i,'v_league'] == mlb_df.loc[i,'h_league'] == "AL":
        mlb_df.loc[i,'MatchType'] = 'AL vs AL'
mlb_df.head()

import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(figsize=(16,8))
plt.suptitle('Game scores by league in MLB', fontsize=20, fontweight='bold')

plt.subplot(121)
plt.title('NL vs NL', fontsize = 18, fontweight='bold')
plt.xlabel('home scores', fontsize = 15)
plt.ylabel('visitor scores', fontsize = 15)
plt.xlim(-1,26); plt.ylim(-1,26)
plt.scatter(x = mlb_df[mlb_df['MatchType']=="NL vs NL"]['h_score'],
            y = mlb_df[mlb_df['MatchType']=="NL vs NL"]['v_score'], c = 'blue', alpha = .1)

plt.subplot(122)
plt.title('AL vs AL', fontsize = 18, fontweight='bold')
plt.xlabel('home scores', fontsize = 15)
plt.ylabel('visitor scores', fontsize = 15)

plt.xlim(-1,26); plt.ylim(-1,26)
plt.scatter(x = mlb_df[mlb_df['MatchType']=="AL vs AL"]['h_score'],
            y = mlb_df[mlb_df['MatchType']=="AL vs AL"]['v_score'], c = 'red', alpha = .1)

_ = plt.show()

mlb_df['score_diff'] = mlb_df['h_score'] - mlb_df['v_score']

plt.figure(figsize=(10,6))
mlb_df['score_diff'].hist(bins=(20), grid = False, color = 'green')
plt.title('Difference in score between home and visiting teams', fontsize = 15, fontweight='bold')

_ = plt.show()

from scipy import stats
import numpy as np

# Spearman correlation coefficient between h score and v score
a = mlb_df.loc[:,['h_score','v_score']]
a.corr(method = "spearman")

#mu1 = rho - sqrt()
data = mlb_df['score_diff']
h = mlb_df['h_score'].mean()
v = mlb_df['v_score'].mean()
mu1 = h - 0.01649*np.sqrt(h*v)
mu2 = v- 0.01649*np.sqrt(h*v)

plt.figure(figsize=(14,5))

plt.subplot(121)
plt.title('The distribution of home team scores')
plt.xlim(-1,26); plt.ylim(0,400)
mlb_df['h_score'].hist(bins=(25), grid = False)
plt.axvline(mu1, color='red')

plt.subplot(122)
plt.title('The distribution of visiting team scores')
plt.xlim(-1,26); plt.ylim(0,400)
mlb_df['v_score'].hist(bins=(25), grid = False)
plt.axvline(mu2, color='red')

_ = plt.show()

stats.kstest(data, lambda x : stats.skellam.cdf(x, mu1 = mu1 , mu2 = mu2, loc = 0))

# skellam distribution(red) and 'score_diff(green)' distribution
plt.figure(figsize=(10,6))

mlb_df['score_diff'].hist(bins=20, grid = False, color = 'green', density = True, label = 'score_diff')

x = np.arange(-20,20,1)
plt.plot(x, stats.skellam.pmf(x, mu1 = mu1, mu2 = mu2), label='skellam pmf', color = 'red')
plt.title('score_diff and skellam distribution', fontsize = 15, fontweight='bold')

_ = plt.legend(loc='best')

#negative binomial, skellam, h score and v score
import numpy as np

x = np.arange(0,25)
xh = mlb_df['h_score']
xv = mlb_df['v_score']

hrv_nb = stats.nbinom.rvs(mu1, 0.5 , size=2431)
hrv_p = stats.poisson.rvs(mu1, size=2431)

vrv_nb = stats.nbinom.rvs(mu2, 0.5 , size=2431)
vrv_p = stats.poisson.rvs(mu2, size=2431)


plt.figure(figsize=(14,5))

plt.subplot(121)
plt.title('Home scores', fontsize = 18, fontweight='bold')
xh.hist(bins=20, grid = False, color = 'green', density= True, label = 'h_score')
plt.plot(x, stats.poisson.pmf(x, mu1, loc=0), color = 'red', label='poisson pmf')
plt.plot(x, stats.nbinom.pmf(x, mu1, p =0.5, loc=0), color = 'blue', label='negative binomial pmf')

_ = plt.legend(loc='best')

plt.subplot(122)
plt.title('Visitor scores', fontsize = 18, fontweight='bold')
xv.hist(bins=20, grid = False, color = 'green', density= True, label = 'v_score')
plt.plot(x, stats.poisson.pmf(x, mu2, loc=0), color = 'red', label='poisson pmf')
plt.plot(x, stats.nbinom.pmf(x, mu2, p =0.5, loc=0), color = 'blue', label='negative binomial pmf')

_ = plt.legend(loc='best')

print(stats.ks_2samp(mlb_df['h_score'], hrv_nb)) # negative binomial
print(stats.ks_2samp(mlb_df['h_score'], hrv_p)) # poisson

print(stats.ks_2samp(mlb_df['v_score'], vrv_nb)) # negative binomial
print(stats.ks_2samp(mlb_df['v_score'], vrv_p)) # poisson
