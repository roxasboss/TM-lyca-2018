
# coding: utf-8

# In[35]:


from datetime import datetime, timedelta  
import time  
from collections import namedtuple  
import pandas as pd 
import requests  
import matplotlib.pyplot as plt  

pd.options.mode.chained_assignment = None
API_KEY = '40b453c139590191'  
BASE_URL = "http://api.wunderground.com/api/{}/history_{}/q/Switzerland/Collombey.json"
target_date = datetime(2016, 8, 16)  
features = ["date", "meantempm", "meandewptm", "meanpressurem", "maxhumidity", "minhumidity", "maxtempm",  
            "mintempm", "maxdewptm", "mindewptm", "maxpressurem", "minpressurem", "precipm"]
DailySummary = namedtuple("DailySummary", features)

def extract_weather_data(url, api_key, target_date, days):  
    records = []
    for _ in range(days):
        request = BASE_URL.format(API_KEY, target_date.strftime('%Y%m%d'))
        response = requests.get(request)
        if response.status_code == 200:
            data = response.json()['history']['dailysummary'][0]
            records.append(DailySummary(
                date=target_date,
                meantempm=data['meantempm'],
                meandewptm=data['meandewptm'],
                meanpressurem=data['meanpressurem'],
                maxhumidity=data['maxhumidity'],
                minhumidity=data['minhumidity'],
                maxtempm=data['maxtempm'],
                mintempm=data['mintempm'],
                maxdewptm=data['maxdewptm'],
                mindewptm=data['mindewptm'],
                maxpressurem=data['maxpressurem'],
                minpressurem=data['minpressurem'],
                precipm=data['precipm']))
        time.sleep(6)
        target_date += timedelta(days=1)
    return records
"""records = extract_weather_data(BASE_URL, API_KEY, target_date, 500)"""  
print("hi" + str(records))
records += extract_weather_data(BASE_URL, API_KEY, target_date, 500)


# In[4]:


import pickle 
with open("weather_records", "rb") as f:
    records = pickle.load(f)


# In[5]:


print("hi" + str(records))


# In[7]:


df = pd.DataFrame(records, columns=features).set_index("date")
print(df)


# In[9]:


tmp = df[["meantempm","meandewptm"]].head(10)
tmp


# In[12]:


N = 1
feature = "meantempm"
rows = tmp.shape[0]
nth_prior_measurements = [None]*N + [tmp[feature][i-N] for i in range (N, rows)]

col_name = "{}_{}".format(feature, N)
tmp[col_name] = nth_prior_measurements
tmp


# In[14]:


def derive_nth_day_feature(df, feature, N):
    rows = df.shape[0]
    nth_prior_measurements = [None]*N + [df[feature][i-N] for i in range(N, rows)]
    col_name = col_name = "{}_{}".format(feature, N)
    df[col_name] = nth_prior_measurements


# In[18]:


for feature in features:
    if feature != 'date':
        for N in range(1,4):
            derive_nth_day_feature(df, feature, N)


# In[19]:


df.columns


# In[20]:


#cleaning data, we remove the useless data
to_remove = [feature for feature in features if feature not in ["meantempm", "mintempm", "maxtempm"]]

to_keep = [col for col in df.columns if col not in to_remove]

df = df[to_keep]
df.columns


# In[21]:


df.info()


# In[36]:


df = df.apply(pd.to_numeric, errors="coerce")
df.info()


# In[28]:


spread = df.describe().T
IQR = spread["75%"] - spread["25%"]

spread['outliers'] = (spread['min']<(spread['25%']-(3*IQR)))|(spread['max'] > (spread['75%']+3*IQR))
#IQR = Interquartile range

spread.loc[spread.outliers,]


# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = [14, 8]  
df.maxhumidity_1.hist()  
plt.title('Distribution of maxhumidity_1')  
plt.xlabel('maxhumidity_1')  
plt.show()  


# In[33]:


for precip_col in ['precipm_1', 'precipm_2', 'precipm_3']:  
    # create a boolean array of values representing nans
    missing_vals = pd.isnull(df[precip_col])
    df[precip_col][missing_vals] = 0


# In[34]:


df = df.dropna()

