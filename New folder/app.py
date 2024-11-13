import streamlit as st
import pandas as pd
import helper



df = pd.read_csv('cleaned.csv')

st.set_page_config(layout = 'wide', page_title = 'StartUp Analysis')
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', df['Startup'].unique())
    st.title('Startup Analysis')
    btn1 = st.sidebar.button('Find Startup Details')
else:
    selected_investor = st.sidebar.selectbox('Select Investor',
     sorted(set(df['Investors'].str.split(',').sum())))
    st.title('Investor Analysis')  
    btn2 = st.sidebar.button('Find Investors Details')
    if btn2:
        helper.load_investor_details(selected_investor)      






