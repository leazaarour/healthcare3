import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px 
from plotly.subplots import make_subplots
df= pd.read_csv('/Users/leazaarour/Desktop/insurance.csv')

with st.sidebar.header('1.Upload your CSV data'):
        uploaded_file= st.sidebar.file_uploader('Upload your input CSV file')
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title='2.Dive into the dataset',
        options=["Home", "Exploratory Data Analysis"],
    )
if selected=="Home":
        st.markdown("<h1 style='text-align: center; color: Navy;'>Insurance charges</h1>", unsafe_allow_html=True)
        st.image('https://asseco.com/files/public/_processed_/csm_insurance_952d181a9a.png',width=400)
        st.subheader("An insurance premium is the amount of money an individual or business pays for an insurance policy. Insurance premiums are paid for policies that cover healthcare, auto, home, and life insurance.")
        st.subheader("Furthermore, many factors affect the amount of the insurance charge, the factors that are discovered in this study are the gender, if the person smokes or not, the bmi and the number of children.")
if selected=="Exploratory Data Analysis":
    #loading the dataset
        df= pd.read_csv('/Users/leazaarour/Desktop/insurance.csv')
        #Exploratory Data Analysis
        st.title("Exploratory Data Analysis")
        st.subheader("1. Visualizing how charges are distributed according to given factors")
        sns.set(style='whitegrid')
        f, ax = plt.subplots(1,1, figsize= (12,8))
        ax = sns.displot(df['charges'], kde= True, color = 'c')
        plt.title ('Charges Distribution')
        st.pyplot()

        st.subheader('2. Visualizing the change of charges by region')
        charges = df['charges'].groupby(df.region).sum().sort_values(ascending = True)
        f, ax = plt.subplots (1,1, figsize = (8,6))
        ax = sns.barplot (charges.head(), charges.head().index, palette = 'Blues')      
        st.pyplot()
        st.subheader('3. Visualizing how the gender and region affect the insurance charges')
        f, ax = plt.subplots (1,1, figsize = (12,8))
        ax = sns.barplot (x='region', y='charges', hue='sex', data=df, palette='cool')
        st.pyplot()
        st.subheader('4. Visualizing how the smoking factor and region affect the insurance charges')
        f, ax = plt.subplots (1,1, figsize = (12,8))
        ax = sns.barplot (x='region', y='charges', hue='sex', data=df, palette='cool')
        f, ax = plt.subplots(1,1, figsize = (12,8))
        ax = sns.barplot (x='region', y= 'charges', hue='smoker', data=df, palette= 'Reds_r')
        st.pyplot()
        st.subheader('5. Visualizing how the number of children and region affect the insurance charges')
        f, ax = plt.subplots (1,1, figsize =(12,8))
        ax = sns.barplot (x='region', y= 'charges', hue='children', data= df, palette= "Blues")
        st.pyplot()
        st.subheader('6. Lets see the medical charges by age, bmi and children according to the smoking factor')
        ax = sns.lmplot( x= 'age' ,y='charges',data= df ,hue='smoker',palette='Set1' )
        st.pyplot()
        ax = sns.lmplot( x= 'bmi' ,y='charges',data= df ,hue='smoker',palette='Set2' )
        st.pyplot()
        ax = sns.lmplot( x= 'children' ,y='charges',data= df ,hue='smoker',palette='Set3' )
        st.pyplot()
