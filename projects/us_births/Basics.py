
# coding: utf-8

# # Explanation
# 
# In this project I manipulate the cdc data for births per day from 1994 to 2003 (*"US_births_1994-2003_CDC_NCHS.csv"*) to calculate the total number of babies born in each year, each month, each day of the month, and each day of the week
# 
# ##### Headers
# * 'year' - Year (1994 to 2003)
# * 'month': Month (1 to 12).
# - 'date_of_month': Day number of the month (1 to 31).
# + 'day_of_week': Day of week (1 to 7).
# * 'births': Number of births that day.
# 

# In[1]:


def read_file(file_name):
    input_file = open(file_name,"r")
    return input_file.read()


# In[2]:


def read_csv(file_name):
    csv_text = read_file(file_name)
    row_list = csv_text.split("\n")
    #print(row_list[0:10])
    data_list = []
    
    first = True
    for row in row_list:
        if first:
            first = False
            continue
        string_list = row.split(",")
        int_list = []
        for string in string_list:
            int_list.append(int(string))
        data_list.append(int_list)
    return data_list


# In[3]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]


# In[4]:


def month_births(input_list):
    births_per_month = {}
    month_index = 1
    births_index = 4
    for row in input_list:
        month = row[month_index]
        births = row[births_index]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month


# In[5]:


cdc_month_births = month_births(cdc_list)
cdc_month_births


# In[6]:


def dow_births(input_list):
    births_per_day = {}
    dow_index = 3
    births_index = 4
    for row in input_list:
        dow = row[dow_index]
        births = row[births_index]
        if dow in births_per_day:
            births_per_day[dow] += births
        else:
            births_per_day[dow] = births
    return births_per_day


# In[7]:


cdc_dow_births = dow_births(cdc_list)
cdc_dow_births


# In[8]:


def calc_births(input_list, column_index):
    num_births = {}
    births_index = 4
    for row in input_list:
        field = row[column_index]
        births = row[births_index]
        if field in num_births:
            num_births[field] += births
        else:
            num_births[field] = births
    return num_births


# In[9]:


cdc_year_births = calc_births(cdc_list, 0)
cdc_month_births = calc_births(cdc_list, 1)
cdc_dom_births = calc_births(cdc_list, 2)
cdc_dow_births = calc_births(cdc_list, 3)


# In[10]:


cdc_year_births


# In[11]:


cdc_month_births


# In[12]:


cdc_dom_births


# In[13]:


cdc_dow_births

