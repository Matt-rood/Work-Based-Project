#!/usr/bin/env python
# coding: utf-8

# # Import Packages

# In[37]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


# # Create user defined funtions

# In[38]:


def Clean(df):
    for df in dataframes:
        for col in df.columns:
            vals = ['nan', 'NP', 'NEW', 'SUPP', 'NE', 'NSE', 'NA', 'NaT', 'NAT', '', ' ', 'DNS']
            df[col] = df[col][~df[col].isin(vals)]
            if col == 'URN':
                extras = ['PRI', 'SEC']
                df[col] = df[col][~df[col].isin(extras)]
                df[col] = df[col].astype(float)   
    
def Join(df, df1, df2, df3, df4):
    new_df = df.merge(df1, on='URN',suffixes=('', '_remove'))\
    .merge(df2, on='URN', suffixes=('', '_remove'))\
    .merge(df3, on='URN', suffixes=('', '_remove'))\
    .merge(df4, on='URN', suffixes=('', '_remove'))
    return new_df

filepath = 'D:\\Schools Data\\Data\\'
#filepath = 'C:\\Users\\matth\\OneDrive\\Documents\\University\\Schools Data\\Data\\'


# In[39]:


from collections import Counter

def cumulatively_categorise(column, threshold = 0.75, return_categories_list = True):
    threshold_value = int(threshold*len(column))
    categories_list = []
    s = 0
    counts = Counter(column)
    
    for i,j in counts.most_common():
        s += counts[i]
        categories_list.append(i)
        if s >= threshold_value:
            break
    categories_list.append('Other')
    
    new_column=column.apply(lambda x: x if x in categories_list else 'Other')
    
    if(return_categories_list):
        return new_column,categories_list
    else:
        return new_column


# # Import the data

# ## 2010-11

# In[89]:


# Import the KS4 information
ks4_2010_2011 = pd.read_csv(filepath + '2010-2011\\england_ks4final.csv', low_memory = False)

# Import the school information
spine_2010_2011 = pd.read_csv(filepath + '2010-2011\\england_spine.csv', low_memory = False)

# Import absence data
abs_2010_2011 = pd.read_csv(filepath + '2010-2011\\england_abs.csv', low_memory = False)

# Import school census data
census_2010_2011 = pd.read_csv(filepath + '2010-2011\\england_census.csv', low_memory = False)

# Import teacher info data
teacher_info_2010_2011 = pd.read_csv(filepath + '2010-2011\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2010_2011['ACADEMIC_YEAR'] = 2011

# List the dataframes
dataframes = [ks4_2010_2011, spine_2010_2011, abs_2010_2011, census_2010_2011, teacher_info_2010_2011]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2010_2011 = Join(ks4_2010_2011, spine_2010_2011, abs_2010_2011, census_2010_2011, teacher_info_2010_2011)

# Select the relevant columns
ks4_2010_2011 = ks4_2010_2011[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PTAC5EM',
                               'PTL2BASICS',
                               'TAVENT_E',
                               'PTANYQ',
                               'PERCTOT',
                               'SALARY',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSMCLA', 
                               'RATPUPTEA',
                               'MINORGROUP']]


# ## 2011-12

# In[90]:


# Import the KS4 information
ks4_2011_2012 = pd.read_csv(filepath + '2011-2012\\england_ks4final.csv', low_memory = False)

# Import the school information
spine_2011_2012 = pd.read_csv(filepath + '2011-2012\\england_spine.csv', low_memory = False)

# Import absence data
abs_2011_2012 = pd.read_csv(filepath + '2011-2012\\england_abs.csv', low_memory = False)

# Import school census data
census_2011_2012 = pd.read_csv(filepath + '2011-2012\\england_census.csv', low_memory = False)

# Import teacher info data
teacher_info_2011_2012 = pd.read_csv(filepath + '2011-2012\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2011_2012['ACADEMIC_YEAR'] = 2012

dataframes = [ks4_2011_2012, spine_2011_2012, abs_2011_2012, census_2011_2012, teacher_info_2011_2012]

# Use the function to clean the dataframes
Clean(dataframes)
                    
# Join all tables together
ks4_2011_2012 = Join(ks4_2011_2012, spine_2011_2012, abs_2011_2012, census_2011_2012, teacher_info_2011_2012)

# Select the relevant columns
ks4_2011_2012 = ks4_2011_2012[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PTAC5EM',
                               'PTL2BASICS',
                               'TAVENT_E',
                               'PTANYQ',
                               'PERCTOT',
                               'SALARY',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSMCLA', 
                               'RATPUPTEA',
                               'MINORGROUP']]


# ## 2012-13

# In[91]:


# Import the KS4 information
ks4_2012_2013 = pd.read_csv(filepath + '2012-2013\\england_ks4final.csv',  low_memory = False)

# Import the school information
spine_2012_2013 = pd.read_csv(filepath + '2012-2013\\england_spine.csv', low_memory = False)

# Import absence data
abs_2012_2013 = pd.read_csv(filepath + '2012-2013\\england_abs.csv', low_memory = False)

# Import school census data
census_2012_2013 = pd.read_csv(filepath + '2012-2013\\england_census.csv', low_memory = False)

# Import teacher info data
teacher_info_2012_2013 = pd.read_csv(filepath + '2012-2013\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2012_2013['ACADEMIC_YEAR'] = 2013

# List the dataframes
dataframes = [ks4_2012_2013, spine_2012_2013, abs_2012_2013, census_2012_2013, teacher_info_2012_2013]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2012_2013 = Join(ks4_2012_2013, spine_2012_2013, abs_2012_2013, census_2012_2013, teacher_info_2012_2013)
 
# Select the relevant columns
ks4_2012_2013 = ks4_2012_2013[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PTAC5EM',
                               'PTL2BASICS',
                               'TAVENT_E',
                               'PTANYQ',
                               'PERCTOT',
                               'SALARY',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSMCLA', 
                               'RATPUPTEA',
                               'MINORGROUP']]


# ## 2013-14

# In[92]:


# Import the KS4 information
ks4_2013_2014 = pd.read_csv(filepath + '2013-2014\\england_ks4final.csv', low_memory = False, encoding='latin-1')

# Import the school information
spine_2013_2014 = pd.read_csv(filepath + '2013-2014\\england_spine.csv', low_memory = False)

# Import absence data
abs_2013_2014 = pd.read_csv(filepath + '2013-2014\\england_abs.csv', low_memory = False)

# Import school census data
census_2013_2014 = pd.read_csv(filepath + '2013-2014\\england_census.csv', low_memory = False)

# Import school census data
teacher_info_2013_2014 = pd.read_csv(filepath + '2013-2014\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2013_2014['ACADEMIC_YEAR'] = 2014

# List the dataframes
dataframes = [ks4_2013_2014, spine_2013_2014, abs_2013_2014, census_2013_2014, teacher_info_2013_2014]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2013_2014 = Join(ks4_2013_2014, spine_2013_2014, abs_2013_2014, census_2013_2014, teacher_info_2013_2014)

# Select the relevant columns
ks4_2013_2014 = ks4_2013_2014[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PTAC5EM_PTQ',
                               'PTL2BASICS_PTQ',
                               'TAVENT_E_PTQ',
                               'PTANYQ_PTQ',
                               'PERCTOT',
                               'SALARY',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSMCLA', 
                               'RATPUPTEA',
                               'MINORGROUP']]


# ## 2014-15

# In[93]:


# Import the KS4 information
ks4_2014_2015 = pd.read_csv(filepath + '2014-2015\\england_ks4final.csv', low_memory = False)

# Import the school information
spine_2014_2015 = pd.read_csv(filepath + '2014-2015\\england_spine.csv', low_memory = False)

# Import absence data
abs_2014_2015 = pd.read_csv(filepath + '2014-2015\\england_abs.csv', low_memory = False)

# Import school census data
census_2014_2015 = pd.read_csv(filepath + '2014-2015\\england_census.csv', low_memory = False)

# Import teacher info data
teacher_info_2014_2015 = pd.read_csv(filepath + '2014-2015\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2014_2015['ACADEMIC_YEAR'] = 2015

# List the dataframes
dataframes = [ks4_2014_2015, spine_2014_2015, census_2014_2015, teacher_info_2014_2015, abs_2014_2015]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2014_2015 = Join(ks4_2014_2015, spine_2014_2015, census_2014_2015, teacher_info_2014_2015, abs_2014_2015)

# Select the relevant columns
ks4_2014_2015 = ks4_2014_2015[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PTAC5EM_PTQ_EE',
                               'PTL2BASICS_PTQ_EE',
                               'TAVENT_E_PTQ_EE',
                               'PTANYQ_PTQ_EE',
                               'PERCTOT',
                               'SALARY',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSM6CLA1A', 
                               'RATPUPTEA',
                               'MINORGROUP']]


# ## 2015-16

# In[94]:


# Import the KS4 information
ks4_2015_2016 = pd.read_csv(filepath + '2015-2016\\england_ks4final.csv', low_memory = False)

# Import the school information
spine_2015_2016 = pd.read_csv(filepath + '2015-2016\\england_spine.csv', low_memory = False)

# Import absence data
abs_2015_2016 = pd.read_csv(filepath + '2015-2016\\england_abs.csv', low_memory = False)

# Import school census data
census_2015_2016 = pd.read_csv(filepath + '2015-2016\\england_census.csv', low_memory = False)

# Import school census data
teacher_info_2015_2016 = pd.read_csv(filepath + '2015-2016\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2015_2016['ACADEMIC_YEAR'] = 2016

# List the dataframes
dataframes = [ks4_2015_2016, spine_2015_2016, abs_2015_2016, census_2015_2016, teacher_info_2015_2016]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2015_2016 = Join(ks4_2015_2016, spine_2015_2016, abs_2015_2016, census_2015_2016, teacher_info_2015_2016)

# Select the relevant columns
ks4_2015_2016 = ks4_2015_2016[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PTAC5EM_PTQ_EE',
                               'PTL2BASICS_LL_PTQ_EE',
                               'TAVENT_E_3NG_PTQ_EE',
                               'PTANYQ_PTQ_EE',
                               'PERCTOT',
                               'Mean Gross FTE Salary of All Teachers',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSM6CLA1A', 
                              'Pupil:     Teacher Ratio',
                               'MINORGROUP']]


# ## 2016-17

# In[95]:


# Import the KS4 information
ks4_2016_2017 = pd.read_csv(filepath + '2016-2017\\england_ks4final.csv', low_memory = False)

# Import the school information
spine_2016_2017 = pd.read_csv(filepath + '2016-2017\\england_spine.csv', low_memory = False)

# Import absence data
abs_2016_2017 = pd.read_csv(filepath + '2016-2017\\england_abs.csv', low_memory = False)

# Import school census data
census_2016_2017 = pd.read_csv(filepath + '2016-2017\\england_census.csv', low_memory = False)

# Import the provisionsal KS4 data
teacher_info_2016_2017 = pd.read_csv(filepath + '2016-2017\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2016_2017['ACADEMIC_YEAR'] = 2017

# List the dataframes
dataframes = [ks4_2016_2017, spine_2016_2017, census_2016_2017, teacher_info_2016_2017, abs_2016_2017]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2016_2017 = Join(ks4_2016_2017, spine_2016_2017, census_2016_2017, teacher_info_2016_2017, abs_2016_2017)

# Select the relevant columns
ks4_2016_2017 = ks4_2016_2017[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PT5EM_94',
                               'PTL2BASICS_94',
                               'TAVENT_E_3NG_PTQ_EE',
                               'PTANYQ_PTQ_EE',
                               'PERCTOT',
                               'Mean Gross FTE Salary of All Teachers',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSM6CLA1A', 
                               'Pupil:     Teacher Ratio',
                               'MINORGROUP']]


# ## 2017-18

# In[96]:


# Import the KS4 information
ks4_2017_2018 = pd.read_csv(filepath + '2017-2018\\england_ks4final.csv', low_memory = False)

# Import the school information
spine_2017_2018 = pd.read_csv(filepath + '2017-2018\\england_spine.csv', low_memory = False)

# Import absence data
abs_2017_2018 = pd.read_csv(filepath + '2017-2018\\england_abs.csv',low_memory = False)

# Import school census data
census_2017_2018 = pd.read_csv(filepath + '2017-2018\\england_census.csv', low_memory = False)

# Import school census data
teacher_info_2017_2018 = pd.read_csv(filepath + '2017-2018\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2017_2018['ACADEMIC_YEAR'] = 2018

# List the dataframes
dataframes = [ks4_2017_2018, spine_2017_2018, abs_2017_2018, census_2017_2018, teacher_info_2017_2018]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2017_2018 = Join(ks4_2017_2018, spine_2017_2018, abs_2017_2018, census_2017_2018, teacher_info_2017_2018) 

# Select the relevant columns
ks4_2017_2018 = ks4_2017_2018[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PT5EM_94',
                               'PTL2BASICS_94',
                               'TAVENT_E_3NG_PTQ_EE',
                               'PTANYQ_PTQ_EE',
                               'PERCTOT',
                               'Mean Gross FTE Salary of All Teachers (£s)',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSM6CLA1A', 
                               'Pupil:     Teacher Ratio',
                               'MINORGROUP']]


# ## 2018-19

# In[97]:


# Import the KS4 information
ks4_2018_2019 = pd.read_csv(filepath + '2018-2019\\england_ks4final.csv', low_memory = False)

# Import the school information
spine_2018_2019 = pd.read_csv(filepath + '2018-2019\\england_school_information.csv', low_memory = False)

# Import absence data
abs_2018_2019 = pd.read_csv(filepath + '2018-2019\\england_abs.csv', low_memory = False)

# Import school census data
census_2018_2019 = pd.read_csv(filepath + '2018-2019\\england_census.csv', low_memory = False)

# Import school census data
teacher_info_2018_2019 = pd.read_csv(filepath + '2018-2019\\england_swf.csv', low_memory = False)

# Add the academic year flag variable
ks4_2018_2019['ACADEMIC_YEAR'] = 2019

# List the dataframes
dataframes = [ks4_2018_2019, spine_2018_2019, abs_2018_2019, census_2018_2019, teacher_info_2018_2019]

# Use the function to clean the dataframes
Clean(dataframes)

# Join all tables together
ks4_2018_2019 = Join(ks4_2018_2019, spine_2018_2019, abs_2018_2019, census_2018_2019, teacher_info_2018_2019)

# Select the relevant columns
ks4_2018_2019 = ks4_2018_2019[['URN',
                               'POSTCODE',
                               'ACADEMIC_YEAR',
                               'KS2APS',
                               'PT5EM_94',
                               'PTL2BASICS_94',
                               'TAVENT_E_3NG_PTQ_EE',
                               'PTANYQ_PTQ_EE',
                               'PERCTOT',
                               'Mean Gross FTE Salary of All Teachers (£s)',
                               'ISPOST16',
                               'ISPRIMARY',
                               'ADMPOL',
                               'RELDENOM',
                               'NFTYPE',
                               'GENDER',
                               'PNUMEAL',
                               'PTFSM6CLA1A', 
                               'Pupil:     Teacher Ratio',
                               'MINORGROUP']]


# In[ ]:


# 2013/14
dict = {'PTAC5EM_PTQ' : 'PTAC5EM',
        'PTL2BASICS_PTQ': 'PTL2BASICS',
        'TAVENT_E_PTQ' : 'TAVENT_E',
        'PTANYQ_PTQ': 'PTANYQ'
        }
ks4_2013_2014.rename(columns=dict, inplace=True)

# 2014/15
dict = {'PTAC5EM_PTQ_EE' : 'PTAC5EM',
        'PTL2BASICS_PTQ_EE': 'PTL2BASICS',
        'TAVENT_E_PTQ_EE' : 'TAVENT_E',
        'PTANYQ_PTQ_EE' : 'PTANYQ',
        'PTFSM6CLA1A' : 'PTFSMCLA'
        }
ks4_2014_2015.rename(columns=dict, inplace=True)

# 2015/16
dict = {'PTAC5EM_PTQ_EE': 'PTAC5EM',
        'PTL2BASICS_LL_PTQ_EE': 'PTL2BASICS',
        'TAVENT_E_3NG_PTQ_EE' : 'TAVENT_E',
        'PTANYQ_PTQ_EE' : 'PTANYQ',        
        'PSENSE4' : 'PSENAPS4',
        'Mean Gross FTE Salary of All Teachers' : 'SALARY',
        'PTFSM6CLA1A' : 'PTFSMCLA',
        'Pupil:     Teacher Ratio' : 'RATPUPTEA'
        }
ks4_2015_2016.rename(columns=dict, inplace=True)

# 2016/17
dict = {'PT5EM_94': 'PTAC5EM',
        'PTL2BASICS_94': 'PTL2BASICS',
        'TAVENT_E_3NG_PTQ_EE' : 'TAVENT_E',
        'PTANYQ_PTQ_EE' : 'PTANYQ',        
        'PSENSE4' : 'PSENAPS4',
        'Mean Gross FTE Salary of All Teachers' : 'SALARY',
        'PTFSM6CLA1A' : 'PTFSMCLA',
        'Pupil:     Teacher Ratio' : 'RATPUPTEA'
       }
ks4_2016_2017.rename(columns=dict, inplace=True)

# 2017/18
dict = {'PT5EM_94': 'PTAC5EM',
        'PTL2BASICS_94': 'PTL2BASICS',
        'TAVENT_E_3NG_PTQ_EE' : 'TAVENT_E',
        'PTANYQ_PTQ_EE' : 'PTANYQ',        
        'PSENSE4' : 'PSENAPS4',
        'Mean Gross FTE Salary of All Teachers (£s)' : 'SALARY',
        'PTFSM6CLA1A' : 'PTFSMCLA',
        'Pupil:     Teacher Ratio' : 'RATPUPTEA'
       }
ks4_2017_2018.rename(columns=dict, inplace=True)

# 2018/19
dict = {'PT5EM_94': 'PTAC5EM',
        'PTL2BASICS_94': 'PTL2BASICS',
        'TAVENT_E_3NG_PTQ_EE' : 'TAVENT_E',
        'PTANYQ_PTQ_EE' : 'PTANYQ',    
        'FSM' : 'PNUMFSM',    
        'PSENSE4' : 'PSENAPS4',
        'Mean Gross FTE Salary of All Teachers (£s)' : 'SALARY',
        'PTFSM6CLA1A' : 'PTFSMCLA',
        'Pupil:     Teacher Ratio' : 'RATPUPTEA'
       }
ks4_2018_2019.rename(columns=dict, inplace=True)


# In[ ]:


stacked_data = pd.concat([ks4_2011_2012, 
                          ks4_2012_2013,
                          ks4_2013_2014,
                          ks4_2014_2015,
                          ks4_2015_2016,
                          ks4_2016_2017,
                          ks4_2017_2018,
                          ks4_2018_2019], 
                         ignore_index=True)

len(stacked_data)


# In[ ]:


nulls = stacked_data.isna().sum().to_frame()
nulls = nulls.rename(columns= {0: 'nulls'})

zeros = stacked_data.isin([0]).sum(axis=0).to_frame()
zeros = zeros.rename(columns= {0: 'zeros'})


# In[57]:


# Check missingness in categorical variables
categorical_variables = ['NFTYPE',
                         'ISPRIMARY',
                         'ISPOST16',
                         'GENDER',
                         'RELDENOM',
                         'ADMPOL']

all_categorical_variables = stacked_data[categorical_variables]

all_categorical_variables.isna().sum()


# In[58]:


# Impute categorical variables
stacked_data["RELDENOM"].fillna("Does not apply", inplace = True) 
stacked_data["ADMPOL"].fillna("Does not apply", inplace = True) 

# Drop NULL values
stacked_data_clean = stacked_data.dropna()


# # Read in and clean Ofsted Data 

# In[107]:


latest_ratings_2019 = pd.read_csv(filepath + 'Management_information_-_schools_Table1_-_31_August_2019.csv',
                                  encoding = 'cp1252',
                                  low_memory = False)

latest_ratings_2020 = pd.read_csv(filepath + 'Management_information_-_state-funded_schools_-_latest_inspections_at_31_December_2020.csv',
                                  encoding = 'cp1252',
                                  low_memory = False)

latest_ratings = pd.concat([latest_ratings_2019, 
                            latest_ratings_2020], 
                           ignore_index = False)


# In[108]:


# Replace spaces in column names with '_'
latest_ratings.columns = latest_ratings.columns.str.replace(' ', '_')

# Filter to specific inspection types
latest_ratings = latest_ratings[(latest_ratings['Event_type_grouping'] == 'Schools - S5') |
                                (latest_ratings['Event_type_grouping'] == 'Section 8 deemed section 5 (excluding short inspections)') |
                                (latest_ratings['Event_type_grouping'] == 'Short inspection converted')]

# Select only Secondary schools
latest_ratings = latest_ratings[(latest_ratings['Ofsted_phase'] == 'Secondary')]


# In[109]:


latest_ratings = latest_ratings[['URN',
                                 'Inspection_end_date',
                                 'Overall_effectiveness', # Target variable
                                 'Previous_inspection_end_date',
                                 'Previous_full_inspection_overall_effectiveness',
                                 'Previous_category_of_concern']]

latest_ratings["Previous_category_of_concern"].fillna("No concern", inplace = True)

latest_ratings = latest_ratings.dropna()


# In[110]:


# Split the year column into day, month and year
latest_ratings[["DAY", "MONTH", "YEAR"]] = latest_ratings["Inspection_end_date"].str.split("/", expand = True)

# Convert these values to integers
latest_ratings[['MONTH', 'YEAR']] = latest_ratings[['MONTH', 'YEAR']].astype(int)

# Derive the academic year
def flag_df(df):
    if (df['MONTH'] >= 9):
        return df['YEAR'] + 1
    elif (df['MONTH'] <= 8):
        return df['YEAR']
    
latest_ratings['ACADEMIC_YEAR'] = latest_ratings.apply(flag_df, axis = 1)

# Count number of days since the last inspection
latest_ratings['Inspection_end_date'] = pd.to_datetime(latest_ratings['Inspection_end_date'],
                                                           format = "%d/%m/%Y")
latest_ratings['Previous_inspection_end_date'] = pd.to_datetime(latest_ratings['Previous_inspection_end_date'],
                                                           format = "%d/%m/%Y")

latest_ratings['DAYS_SINCE_LAST'] = (latest_ratings['Inspection_end_date'] - latest_ratings['Previous_inspection_end_date']) / np.timedelta64(1, 'D')

# Do YEAR - 1
latest_ratings['LINKAGE_YEAR'] = latest_ratings['ACADEMIC_YEAR'] - 1


# In[111]:


final_table = pd.merge(stacked_data_clean, 
                       latest_ratings, 
                       how='left', 
                       left_on=['URN','ACADEMIC_YEAR'], 
                       right_on = ['URN','LINKAGE_YEAR'])

# Select columns needed
final_table = final_table.drop(['ACADEMIC_YEAR_x',
                                'ACADEMIC_YEAR_y',
                                'LINKAGE_YEAR',
                                'DAY', 
                                'MONTH', 
                                'YEAR', 
                                'Previous_inspection_end_date',
                                'Inspection_end_date'], 
                               axis=1)

# Drop any missing columns
final_table["RELDENOM"].fillna("Does not apply", inplace = True) 
final_table = final_table.dropna()
final_table = final_table.drop_duplicates()

len(final_table)


# In[112]:


# Import IDACI lookup 
idaci_quintiles = pd.read_csv('C:\\Users\\roodm\\OneDrive - Office for National Statistics\\University\\Year 3\\Work Based Project\\2019-deprivation-by-postcode.csv')

idaci_quintiles = idaci_quintiles[['Postcode', 'IDACI Decile']]

# Join IDACI lookup
final_table = pd.merge(final_table, 
                       idaci_quintiles, 
                       how='left', 
                       left_on='POSTCODE', 
                       right_on = 'Postcode')

final_table = final_table.drop_duplicates()

final_table = final_table.drop(['POSTCODE',
                                'Postcode'], 
                               axis=1)

len(final_table)


# # Identifying suitable categorical variables by looking at their distributions and importance

# #### Selecting all categorical variables in the data

# In[65]:


categorical_variables = ['MINORGROUP',
                         'NFTYPE',
                         'ISPRIMARY',
                         'ISPOST16',
                         'GENDER',
                         'RELDENOM',
                         'ADMPOL']

all_categorical_variables = final_table[categorical_variables]


# In[66]:


remapped_MINORGROUP = {'Maintained school': "Maintained School"}

all_categorical_variables = all_categorical_variables.replace({"MINORGROUP": remapped_MINORGROUP})


# In[67]:


remapped_RELDENOM = {'Roman Catholic/Church of England': "Christian",
                     'Roman Catholic' : "Christian",
                     'Church of England' : 'Christian',
                     'Church of England/Roman Catholic' : 'Christian',
                     'Church of England/Christian' : 'Christian',
                     'None' : 'Does not apply'
                    }

all_categorical_variables = all_categorical_variables.replace({"RELDENOM": remapped_RELDENOM})


# In[68]:


fig, axs = plt.subplots(4, 2, 
                        figsize = (20,20))

axs = axs.flatten()

for i, col in enumerate(all_categorical_variables.columns):
    value_counts = all_categorical_variables[col].value_counts()
    axs[i].bar(value_counts.index.astype(str), value_counts.values)
    axs[i].set_title(f'Value Counts of {col}')
    axs[i].set_xlabel('Unique values')
    axs[i].set_ylabel(f'Counts')
    
for j in range(i + 1, len(axs)):
    fig.delaxes(axs[j])
    
plt.tight_layout()

plt.show()


# In[69]:


categorical_variables = ['GENDER',
                         'RELDENOM']

selected_dfs = final_table[categorical_variables]


# In[70]:


remapped_gender = {'Boys': "Not mixed", 
                   'Girls': "Not mixed"}

selected_dfs = selected_dfs.replace({"GENDER": remapped_gender})


# In[71]:


remapped_reldenom = {'Does not apply': "Not religious", 
                     'Roman Catholic': "Religious",
                     'Christian' : "Religious",
                     'Church of England' : "Religious", 
                     'Roman Catholic/Church of England' : "Religious",
                     'Church of England/Roman Catholic' : "Religious",
                     'Church of England/Christian' : "Religious",
                     'Sikh' : 'Religious', 
                     'Muslim' : 'Religious', 
                     'Jewish' : 'Religious',
                     'None' : 'Not religious'}

selected_dfs = selected_dfs.replace({"RELDENOM": remapped_reldenom})


# In[72]:


fig, axs = plt.subplots(2,1 ,
                        figsize = (20,20))

axs = axs.flatten()

for i, col in enumerate(selected_dfs.columns):
    value_counts = selected_dfs[col].value_counts()
    axs[i].bar(value_counts.index.astype(str), value_counts.values)
    axs[i].set_title(f'Value Counts of {col}')
    axs[i].set_xlabel('Unique values')
    axs[i].set_ylabel(f'Counts')
    
plt.tight_layout()

plt.show()


# In[73]:


categorical_variables_ofsted = ['Overall_effectiveness',
                                'Previous_full_inspection_overall_effectiveness',
                                'Previous_category_of_concern',
                                'IDACI Decile']

selected_dfs_ofsted = final_table[categorical_variables_ofsted]


# In[74]:


fig, axs = plt.subplots(2, 2, 
                        figsize = (20,20))

axs = axs.flatten()

for i, col in enumerate(selected_dfs_ofsted.columns):
    value_counts = selected_dfs_ofsted[col].value_counts().sort_index()
    axs[i].bar(value_counts.index.astype(str), value_counts.values)
    axs[i].set_title(f'Value Counts of {col}')
    axs[i].set_xlabel('Unique values')
    axs[i].set_ylabel(f'Counts')
    
plt.tight_layout()

plt.show()


# In[75]:


remapped_reldenom = {'COMP': "Comprehensive", 
                     'SEL': "Selective",
                     'MOD' : "Comprehensive",
                     'UK' : "Unknown",
                     'Not applicable' : 'Unknown',
                     'Non-selective' : 'Comprehensive'}

selected_dfs = selected_dfs.replace({"ADMPOL": remapped_reldenom})


# In[76]:


remapped_reldenom = {'Roman Catholic': "Religious",
                     'Church of England' : "Religious", 
                     'Roman Catholic/Church of England' : "Religious",
                     'Church of England/Roman Catholic' : "Religious",
                     'Church of England/Christian' : "Religious",
                     'Unknown' : "Does not apply",
                     'Christian' : 'Religious',
                     'Muslim' : 'Religious',
                     'Sikh' : 'Religious',
                     'Jewish' : 'Religious',
                     None : 'Not religouse'} 

selected_dfs = selected_dfs.replace({"RELDENOM": remapped_reldenom})


# In[77]:


post_16 = {0.0 : "No",
           1.0 : 'Yes'} 

selected_dfs = selected_dfs.replace({"ISPOST16": post_16})


# In[78]:


school_types = {'Maintained school' : "Maintained School",
               'Academy (including Free Schools)' : 'All Academy Types',
               'Academy' : 'All Academy Types'} 

selected_dfs = selected_dfs.replace({"MINORGROUP": school_types})


# In[79]:


fig, axs = plt.subplots(2, 1, 
                        figsize = (20,20))

axs = axs.flatten()

for i, col in enumerate(selected_dfs.columns):
    value_counts = selected_dfs[col].value_counts()
    axs[i].bar(value_counts.index.astype(str), value_counts.values)
    axs[i].set_title(f'Value Counts of {col}')
    axs[i].set_xlabel('Unique values')
    axs[i].set_ylabel(f'Counts')
    
plt.tight_layout()

plt.show()


# In[80]:


previous_category_concern = {'SM' : "Previous Concerns", 
                            'SWK' : "Previous Concerns",
                            'Special Measures' : "Previous Concerns", 
                            'Serious Weaknesses' : "Previous Concerns",
                            'NTI' : 'Previous Concerns',} 

selected_dfs = selected_dfs.replace({"Previous_category_of_concern": previous_category_concern})


# # The 9-1 grading was implemented in 2017 for English and Maths GCSEs, the following section compares KS4 data for pre and post grading data

# ## Import data, selecting KS4 variables of inital interest

# In[164]:


# For 2010/11
ks4_2010_2011_compare = ks4_2010_2011[['PTAC5EM',
                                       'PTL2BASICS']]


# In[165]:


# For 2011/12
ks4_2011_2012_compare = ks4_2011_2012[['PTAC5EM',
                                       'PTL2BASICS']]


# In[166]:


# For 2012/13
ks4_2012_2013_compare = ks4_2012_2013[['PTAC5EM',
                                       'PTL2BASICS']]


# In[167]:


# For 2013/14
ks4_2013_2014_compare = ks4_2013_2014[['PTAC5EM_PTQ',
                                       'PTL2BASICS_PTQ']]


# In[168]:


# For 2014/15
ks4_2014_2015_compare = ks4_2014_2015[['PTAC5EM_PTQ_EE',
                                       'PTL2BASICS_PTQ_EE']]


# In[169]:


# For 2015/16
ks4_2015_2016_compare = ks4_2015_2016[['PTAC5EM_PTQ_EE',
                                       'PTL2BASICS_LL_PTQ_EE']]


# In[170]:


# For 2016/17
ks4_2016_2017_compare = ks4_2016_2017[['PT5EM_94',
                                       'PTL2BASICS_94']]


# In[171]:


# For 2017/18
ks4_2017_2018_compare = ks4_2017_2018[['PT5EM_94',
                                       'PTL2BASICS_94']]


# In[172]:


# For 2018/19
ks4_2018_2019_compare = ks4_2018_2019[['PT5EM_94',
                                       'PTL2BASICS_94']]


# ## Create Test Plots for KS4 variables (Maths and English inclusive)

# In[174]:


dfs = [ks4_2010_2011_compare, ks4_2011_2012_compare, ks4_2012_2013_compare, ks4_2013_2014_compare, 
       ks4_2014_2015_compare, ks4_2015_2016_compare, ks4_2016_2017_compare, ks4_2017_2018_compare, 
       ks4_2018_2019_compare]

for df in dfs:
        for col in df.columns:
            vals = ['nan', 'NP', 'NEW', 'SUPP', 'NE', 'NSE', 'NA', 'NaT', 'NAT', '', ' ', 'DNS']
            df[col] = df[col][~df[col].isin(vals)]
            
def remove_percentage(df):
    for column in df.columns:
        df[column] = df[column].str.replace('%', '').astype(float)
    return df

cleaned_dfs = [remove_percentage(df) for df in dfs]

for df in dfs:
    for col in df.columns:
        vals = [0]
        df[col] = df[col][~df[col].isin(vals)]


# In[175]:


dfs_and_columns = [(ks4_2010_2011_compare, 'PTAC5EM'), 
                   (ks4_2011_2012_compare, 'PTAC5EM'), 
                   (ks4_2012_2013_compare, 'PTAC5EM'), 
                   (ks4_2013_2014_compare, 'PTAC5EM_PTQ'), 
                   (ks4_2014_2015_compare, 'PTAC5EM_PTQ_EE'), 
                   (ks4_2015_2016_compare, 'PTAC5EM_PTQ_EE'), 
                   (ks4_2016_2017_compare, 'PT5EM_94'), 
                   (ks4_2017_2018_compare, 'PT5EM_94'), 
                   (ks4_2018_2019_compare, 'PT5EM_94')]

fig, axes = plt.subplots(3, 3, figsize = (20, 10))
axes = axes.flatten()

for i, (df, column) in enumerate(dfs_and_columns): 
    sns.distplot(df[column], 
                 kde = True, 
                 ax = axes[i])
    axes[i].set_title(f'Distribution of {column}')
                                                                  
plt.tight_layout()
plt.show()


# In[176]:


dfs_and_columns = [(ks4_2010_2011_compare, 'PTL2BASICS'), 
                   (ks4_2011_2012_compare, 'PTL2BASICS'), 
                   (ks4_2012_2013_compare, 'PTL2BASICS'), 
                   (ks4_2013_2014_compare, 'PTL2BASICS_PTQ'), 
                   (ks4_2014_2015_compare, 'PTL2BASICS_PTQ_EE'), 
                   (ks4_2015_2016_compare, 'PTL2BASICS_LL_PTQ_EE'), 
                   (ks4_2016_2017_compare, 'PTL2BASICS_94'), 
                   (ks4_2017_2018_compare, 'PTL2BASICS_94'), 
                   (ks4_2018_2019_compare, 'PTL2BASICS_94')]

fig, axes = plt.subplots(3, 3, figsize = (20, 10))
axes = axes.flatten()

for i, (df, column) in enumerate(dfs_and_columns): 
    sns.distplot(df[column], 
                 kde = True, 
                 ax = axes[i])
    axes[i].set_title(f'Distribution of {column}')
                                 
                                 
plt.tight_layout()
plt.show()


# In[ ]:




