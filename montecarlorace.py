# -*- coding: utf-8 -*-
"""MonteCarloRace.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jT3ahrxNnynPd5A33w9goEl7eIFM88bv

Assume that our data frame has the NAME of the runner and the TIME they took in their previous races, ordered by DATE. Our logic is to get the rolling EWM and then to keep the last for each runner
"""

## generate random date
import datetime
import random
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2021, 2, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)
print(random_date)



import pandas as pd
import numpy as np
## convert it to data
#df['DATE'] = pd.to_datetime(df.DATE)
## sort by date
#df.sort_values('DATE', inplace=True)
#df['mean_tmp']=df.groupby('NAME')['TIME'].transform(lambda x: x.ewm(alpha=0.30).mean())
#df['std_tmp']=df.groupby('NAME')['TIME'].transform(lambda x: x.ewm(alpha=0.30).std())
## remove the NAN in Std
#df.dropna(subset=['std_tmp'], inplace=True)
## get the most recent observation of the EWM
#runner= df.groupby('NAME')[['mean_tmp', 'std_tmp']].last()
#runner.reset_index(inplace=True)
#runner.columns = ['NAME', 'mean', 'std']
#runner


## A, 13.1, 12-01-2020
## A, 13.2, 12-10-2020
##

"""Assume that we come up with the following mean and standard deviation for the 8 runners."""

runner = pd.DataFrame({'NAME':["A","B","C","D","E","F","G","H"],
                       'mean': [13.11, 13.17, 12.99, 12.96, 13.25, 13.00, 13.40, 13.29],
                       'std': [0.15, 0.15, 0.17, 0.20, 0.14, 0.16, 0.17, 0.2]})
runner

# number of simulations
np.random.seed(5)
# number of simulations
sims = 1000
runner['monte_carlo'] = runner.apply(lambda x:np.random.normal(x['mean'], x['std'], sims), axis=1)
runner

"""Once we simulated the data, we can get the probability of each runner to win."""

# Probability to finish in top x positions
top_x = 1
tmp_probs = pd.DataFrame((pd.DataFrame(list(runner['monte_carlo']),index=runner.NAME).rank()<=top_x).sum(axis=1)/sims)
tmp_probs.reset_index(inplace=True)
tmp_probs.columns=['NAME', 'Probability']
tmp_probs

"""Similarly, we can estimate the probability of each runner to be on the podium, i.e. in the top 3 positions."""

# Probability to finish in top x positions 
top_x = 3 # in top three positions
tmp_probs = pd.DataFrame((pd.DataFrame(list(runner['monte_carlo']),index=runner.NAME).rank()<=top_x).sum(axis=1)/sims)
tmp_probs.reset_index(inplace=True)
tmp_probs.columns=['NAME', 'Probability']
tmp_probs

