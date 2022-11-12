# Author: Prakash Sukhwal
# version: 2.0
# Aug 2021

import streamlit as st
# other libs
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

# -- Set page config
apptitle = 'ST Assignment'

st.set_page_config(page_title=apptitle, page_icon='random', layout= 'wide', initial_sidebar_state="expanded")
# random icons in the browser tab

st.title('ST assignment on the go..')
st.balloons()

 ######################## section-1 ##################
 # Let's add a sub-title
st.write("A **_cool_** ST assignment application")

filename = 'Assignment1.xlsx' #INSERT FILENAME FOR ISPS EXTRACTED EXCEL 
filename_PO = 'PO List' #INSERT SHEET NAME FOR PO List
filename_POGBW = 'PO GBW List' #INSERT SHEET NAME FOR PO GBW List

xls = pd.ExcelFile(filename)
df1 = pd.read_excel(xls, filename_PO, header = 1)
df2 = pd.read_excel(xls, filename_POGBW, header = 1)

complexST = st.radio(
 	'Complex?',
 	('COMPLEX', 'NON-COMPLEX'))

PPVC = st.radio(
 	'PPVC?',
 	('PPVC', 'NON-PPVC'))

storey = st.radio(
 	'More than 30 storeys?',
 	('> 30 storeys', '< 30 storeys'))


st.write(f'The project is {complexST}, {PPVC} and {storey}.')


if PPVC == 'PPVC':
    df = df1[df1['PPVClist'] == 1]
    df = df[df['Can Assign?'] == 1]
    df = df.sort_values(
        by="ppvc_next",
        ascending=False)
    st.write("Structural PO list:")
    st.write(df[["PO_name", "Department", "ppvc_lastdate", "ppvc_next"]])

else:
    if storey == "> 30 storeys":
        df = df1[df1['PPVClist'] == 0] #cannot be in the PPVC list
        df = df[df['Yrs_of_Exp'] >= 3]
        df = df[df['Can Assign?'] == 1]
        df = df.sort_values(
            by="30storey_next",
            ascending=False)
        st.write("Structural PO list:")
        st.write(df[["PO_name", "Department", "30storey_lastdate", "30storey_next"]])
        
        #GBW PO list
        df_gbw = df2[df2['Can Assign?'] == 1]
        df_gbw = df_gbw.sort_values(
            by="30storey_next",
            ascending=False)
        st.write("GBW PO list:")
        st.write(df_gbw[["PO_name", "Department", "30storey_lastdate", "30storey_next"]])
    
    else:
        if complexST == "COMPLEX":
            df = df1[df1['PPVClist'] == 0] #cannot be in the PPVC list
            df = df[df['Yrs_of_Exp'] >= 3]
            df = df[df['Can Assign?'] == 1]
            df = df.sort_values(
                by="30storey_next",
                ascending=False)
            st.write("Structural PO list:")
            st.write(df[["PO_name", "Department", "30storey_lastdate", "30storey_next"]])
        
        else:
            df = df1[df1['Can Assign?'] == 1]
            df = df.sort_values(
                by="10storey_next",
                ascending=False)
            st.write("Structural PO list:")
            st.write(df[["PO_name", "Department", "10storey_lastdate", "10storey_next"]])