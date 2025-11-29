# INST414 Final Project Sprint 2

## Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# select columns to read and keep
cols_to_keep = ['Data_Value', 'Race/Ethnicity', 'Age(months)', 'Sex', 'LocationDesc', 'LocationAbbr', 'YearStart', 'YearEnd', 'Low_Confidence_Limit', 'High_Confidence_Limit', 'Sample_Size']
df = pd.read_csv("/Users/virginialee/Downloads/WIC_data.csv", usecols=cols_to_keep)

df.head()
df.shape

# rename columns to be more intuitive
df.rename(columns={
    'Data_Value': 'pct_overweight',
    'Race/Ethnicity': 'race',
    'Age(months)': 'age_months'
}, inplace=True)
df.head()

missing_value = df.isna().sum()
print(missing_value)

379/12852 # % missing for data_value
7182/12852 # % missing for race/ethnicity
9072/12852 # % missing for age
10584/12852 # % missing for sex

# dropping rows with missing Data_Value
df_drop_na = df.dropna(subset=['Data_Value'])
df_drop_na.head()

# dropping sex column due to high missingness
df_drop_sex = df_drop_na.drop(columns='Sex')

df_race = df_drop_sex[df_drop_sex['Race/Ethnicity'].isin(['American Indian/Alaska Native', 'Non-Hispanic White'])]
df_race.shape

# examining missingness patterns
missingness_df = df.copy()
missingness_df['age_missing'] = missingness_df['Age(months)'].isna().astype(int)
missingness_df.head()

missingness_df.groupby("Race/Ethnicity")['age_missing'].mean()
missingness_df.groupby('Sex')['age_missing'].mean()
missingness_df.groupby('LocationDesc')['age_missing'].mean()

# outliers
df.boxplot(column='Data_Value')
plt.title("Boxplot of % Overweight")
plt.show()

# duplicates in data set
duplicates = df.duplicated()
print(duplicates.value_counts())
duplicates.drop_duplicates()

# duplicates in df_race
df_race.drop_duplicates()
df_race.shape

# inconsistencies
print(df['Race/Ethnicity'].value_counts())
print(df['Sex'].value_counts())
print(df['LocationDesc'].value_counts().sort_values())


plt.figure()
overweight_race = df_race.groupby('Race/Ethnicity')['Data_Value'].mean().reset_index()
sns.barplot(x='Race/Ethnicity', y='Data_Value', data=overweight_race)
plt.ylabel('% of WIC toddlers overweight')
plt.xlabel('Proportion of Overweight Toddlers by Race')
plt.show()

plt.figure()
overweight_age = df_race.groupby('Age(months)')['Data_Value'].mean().reset_index()
sns.barplot(x='Age(months)', y= 'Data_Value', data=overweight_age)
plt.ylabel('% of WIC toddlers overweight')
plt.xlabel('Proportion of Overweight Toddlers by Age (months)')
plt.show()

plt.figure()
sns.boxplot(x='Race/Ethnicity', y='Data_Value', data=df_race)
plt.title("Boxplot of Race/Ethnicity and % Overweight")
plt.ylabel('% of WIC toddlers overweight')
plt.show()

state_df = df.groupby('LocationDesc')['Data_Value'].mean().reset_index()
plt.figure()
sns.scatterplot(data=df_race, x='LocationDesc', y='Data_Value', hue='Race/Ethnicity')
plt.xticks(rotation=90)
plt.ylabel('% of Overweight WIC Toddlers')
plt.title("% Overweight by US State/Territory")
plt.show()