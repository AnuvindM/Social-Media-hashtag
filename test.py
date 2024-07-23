import streamlit as st
import pandas as pd
df=pd.read_csv(r'C:\Users\anuvi\OneDrive\Desktop\census_2011 (1).csv')
df.head()
df.describe()
df.info()
st.title("Data Cleaning")

rename_columns = {
    'State name': 'State/UT',
    'District name': 'District',
    'Male_Literate': 'Literate_Male',
    'Female_Literate': 'Literate_Female',
    'Rural_Households': 'Households_Rural',
    'Urban_Households': 'Households_Urban',
    'Age_Group_0_29': 'Young_and_Adult',
    'Age_Group_30_49': 'Middle_Aged',
    'Age_Group_50': 'Senior_Citizen',
    'Age not stated': 'Age_Not_Stated'
}
df.rename(columns=rename_columns, inplace=True)
df.head()
#Replacing place names
df.replace(

    to_replace="ANDAMAN AND NICOBAR ISLANDS",
    value="Andaman and Nicobar Islands",inplace=True
)
df.replace(

    to_replace="JAMMU AND KASHMIR",
    value="Jammu and Kashmir",inplace=True
)
li=["Adilabad","Nizamabad","Karimnagar","Medak","Hyderabad","Rangareddy","Mahbubnagar","Nalgonda","Warangal","Khammam"]
a=df.isna().sum()
a

a.hist()
#fill missing values
def fillvalues(df):
    df['Population']=df['Population'].fillna(df['Male']+df['Female'])
    df['Literate']=df['Literate'].fillna(df['Literate_Male']+df['Literate_Female'])
    df['Households']=df['Households'].fillna(df['Households_Rural']+df['Households_Urban'])
    
    return df

data_filled=fillvalues(df)

#calculating percentage of missing values
intial_percentage=df.isnull().mean()*100
final_percentage=data_filled.isnull().mean()*100
print("Initial missing data percentage:")
print(intial_percentage)
print("\n")
print("Filled data missing percentage:")
data_filled
