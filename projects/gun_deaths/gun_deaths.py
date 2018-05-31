
# coding: utf-8

# # Gun Deaths in US
# 
# In this notebook I will explore demographic data on gun deaths in the US, and break them down by gender, race, date and intention (accidental vs homicide) looking for meaningful trends

# ### Explanation of variables in guns.csv (index is 1 less)
# 
# 1. Row number
# 1. Year
# 2. Month (1-12)
# 3. Intent (Suicide, Accidental, NA, Homicide, Undetermined)
# 4. Police
# 5. Sex (M/F)
# 6. Age (to one decimal)
# 7. Race (Asian/Pacific Islander, Native American/Native Alaskan, Black, Hispanic, or White)
# 8. Hispanic
# 9. Place (Home, Street, Other specified
# 10. Education (1: less than HS, 2: graduated HS, 3: some college, 4: graduated college, 5: not available)

# In[1]:


import csv
import datetime

with open("guns.csv","r") as input_file:
    data = list(csv.reader(input_file))


# In[39]:


headers = data[0]
data = data[1:]


# In[5]:


def count_deaths(index, dataset):
    death_count = {}
    for each in dataset:
        var = each[index]
        if var in death_count:
            death_count[var] += 1
        else:
            death_count[var] = 1
    return death_count 

years = [each[1] for each in data]
year_counts = count_deaths(1, data)

print (year_counts)


# In[43]:


dates = [datetime.datetime(year=int(each[1]),month=int(each[2]),day=1) for each in data]

date_counts = {}
for each in dates:
    if each in date_counts:
        date_counts[each] += 1
    else:
        date_counts[each] = 1

        
for date in date_counts:
    print(date.strftime("%b %Y") + ": %d" % (date_counts[date]))


# **Gun deaths occur randomly throughout the year**

# # Gun deaths by race
# 
# Below I will explore gun deaths by race.  Initially I will determine how many absolute gun deaths by race occurred, and then I will determine the death rate per 100k by race.  Finally I will stratify by intent, obtaining the homicide and accidental death rates per 100k

# In[17]:


sex_counts = count_deaths(5,data)
race_counts = count_deaths(7,data)
print(race_counts)
print(sex_counts)


# Males die much more frequently than women by gun.  We have total numbers of gun deaths by race, but unclear of significance without breaking it down into death rates / 100k people.  In the next cells we'll use demographic data from US census to convert death counts by race into rates

# In[44]:


with open("census.csv","r") as input_file:
    census = list(csv.reader(input_file))


# Census data is table with only **2 rows**, shown below
# 
# <table class="dataframe">
# <thead>
# <tr>
# <th>Id</th>
# <th>Year</th>
# <th>Id.1</th>
# <th>Sex</th>
# <th>Id.2</th>
# <th>Hispanic Origin</th>
# <th>Id.3</th>
# <th>Id2</th>
# <th>Geography</th>
# <th>Total</th>
# <th>Race Alone - White</th>
# <th>Race Alone - Hispanic</th>
# <th>Race Alone - Black or African American</th>
# <th>Race Alone - American Indian and Alaska Native</th>
# <th>Race Alone - Asian</th>
# <th>Race Alone - Native Hawaiian and Other Pacific Islander</th>
# <th>Two or More Races</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>cen42010</td>
# <td>April 1, 2010 Census</td>
# <td>totsex</td>
# <td>Both Sexes</td>
# <td>tothisp</td>
# <td>Total</td>
# <td>0100000US</td>
# <td>NaN</td>
# <td>United States</td>
# <td>308745538</td>
# <td>197318956</td>
# <td>44618105</td>
# <td>40250635</td>
# <td>3739506</td>
# <td>15159516</td>
# <td>674625</td>
# <td>6984195</td>
# </tr>
# </tbody>
# </table>

# In[45]:


num_white = int(census[1][10])
num_asian = int(census[1][14]) + int(census[1][15])
num_hispanic = int(census[1][11])
num_black = int(census[1][12])
num_indian = int(census[1][13])

mapping = {
    "Asian/Pacific Islander": num_asian,
    "Black": num_black,
    "Native American/Native Alaskan": num_indian,
    "Hispanic": num_hispanic,
    "White": num_white
}


# In[60]:


race_rates_per_hundredk = {}

for race in race_counts:
    rate = race_counts[race]/mapping[race] * 100000
    race_rates_per_hundredk[race] = rate

def display_rates(title, rates):
    print(title + ":")
    for each in rates:
        print(each + ": %.1f" % (rates[each]) + "/100,000")
        
display_rates("Rates of gun deaths by race",race_rates_per_hundredk)


# These represent rates of gun deaths per 100k people, but do not specifically focus on rates of gun *homicides*.  Will do this below by specifying intent

# # Homicide gun death rates by race
# 
# * Blacks have >10x of rate dying by gun homicide as whites
# * Hispanics have 3x rate as whites
# * Native America/Native Alaskan have 2x rate as whites

# In[61]:


intents = [each[3] for each in data]
races = [each[7] for each in data]

def get_death_counts(intent,demographic):
    homicide_counts = {}

    for i, value in enumerate(demographic):
        if intents[i] == intent:
            if value in homicide_counts:
                homicide_counts[value] += 1
            else:
                homicide_counts[value] = 1
    return homicide_counts

homicide_race_counts = get_death_counts("Homicide",races)
homicide_rates_by_race = {}

for each in homicide_race_counts:
    homicide_rates_by_race[each] = homicide_race_counts[each]/mapping[each]*100000

display_rates("Rates of gun death homicides by race",homicide_rates_by_race)


# # Accidental gun death rates by rates
# 
# * Interestingly, these do not vary much by race

# In[62]:


accident_race_counts = get_death_counts("Accidental",races)
accident_race_rates = {}

for each in accident_race_counts:
    accident_race_rates[each] = accident_race_counts[each]/mapping[each]* 100000
    
display_rates("Rates of gun death accidents by race",accident_race_rates)


# # Rates by gender

# In[72]:


# Obtain presumed number of people in each gender in US
total_people = int(census[1][9])
each_gender = total_people/2


# In[73]:


#sex_counts was already obtained above by calling count_deaths(5,data)

print("Total death counts by gender:")
for each in sex_counts:
    print(each + ": %d" % (sex_counts[each]))


# In[76]:


def get_rates_by_gender(intent):
    counts = {}
    gender = [each[5] for each in data]
    for i, value in enumerate(gender):
        if intents[i] == intent:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
    rates = {}
    for each in gender:
        rates[each] = counts[each] / each_gender * 100000
    return rates


# In[77]:


display_rates("Rates of gun death homicides by gender",get_rates_by_gender("Homicide"))


# In[78]:


display_rates("Rates of gun death accidents by gender",get_rates_by_gender("Accidental"))


# Men die approximately ***9 times*** more often by gun than women, both via homicide and accident

# # Gun deaths by month

# In[88]:


month_counts = {}

months = [int(each[2]) for each in data]
for each in months:
    month = int(each)
    if month in month_counts:
        month_counts[month] += 1
    else:
        month_counts[month] = 1


print("Total deaths by month")
for each in month_counts:
    print ("%d: %d" % (each,month_counts[each]))


# There doesn't appear to be a link between total gun deaths by month, although February had significatly fewer.  Let's look at homicides and accidents specifically

# In[94]:


accidents_by_month = get_death_counts("Accidental",months)

print("Total accidental deaths by month:")
for each in accidents_by_month:
    print("%d: %d" % (each, accidents_by_month[each]))


# Seems random

# In[95]:


homicides_by_month = get_death_counts("Homicide",months)

print("Total homicide deaths by month:")
for each in homicides_by_month:
    print("%d: %d" % (each, homicides_by_month[each]))


# Slight Summer spike?
