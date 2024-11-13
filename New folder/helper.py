import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned.csv')

def load_investor_details(investor):
    st.title(investor)
    last_df = (df[df.Investors.str.contains(investor)][['Date', 'Startup', 'Vertical', 
    'Subvertical', 'City', 'Round', 'Amount']])
    st.subheader('Recent Investments')
    st.dataframe(last_df)

    big_series = df[df.Investors.str.contains(investor)].groupby('Startup').Amount.sum().sort_values(ascending = False).head(10)
    
    col1, col2 = st.columns(2)
    with col1:
    
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

    with col2:
        st.write("Generally Invests in ")   
        st.subheader(df[df.Investors.str.contains(investor)].groupby('Vertical').Amount.sum().sort_values(ascending = False).head(1).index[0])
        fig, ax = plt.subplots()
        df[df.Investors.str.contains(investor)].groupby('Vertical').Amount.sum().plot(kind='pie', 
                                                ax=ax, 
                                                labeldistance=1.2,   # Increase label distance for radial effect
                                                autopct='%1.1f%%',   # Show percentages
                                                startangle=90,       # Rotate the pie chart for better alignment
                                                colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0', '#ffb3e6'])  # Optional: Color palette

        # Set title and remove y-label
        ax.set_title('Vertical Distribution of IDG Ventures')
        st.pyplot(fig)
    
    col3, col4 = st.columns(2)
    with col3:
    
        st.subheader('Rounds of Investments')
        fig, ax = plt.subplots()
        df[df.Investors.str.contains(investor)].groupby('Round').Amount.sum().plot(kind='barh')
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

    with col4:
        st.subheader("Cities Invested in ")   
        fig, ax = plt.subplots()
        df[df.Investors.str.contains(investor)].groupby('City').Amount.sum().plot(kind='pie', 
                                                                                 labeldistance=1.2,   # Increase label distance for radial effect
                                                                                 autopct='%1.1f%%',   # Show percentages on the pie slices
                                                                                 startangle=90,       # Rotate the pie chart for better alignment
                                                                                 figsize=(6, 6))


        # Set title and remove y-label
        ax.set_title('City Distribution')
        st.pyplot(fig)