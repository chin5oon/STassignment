# Author: CS
# version: 1.0
# Nov 2022

import streamlit as st
# other libs
import pandas as pd

# -- Set page config
apptitle = 'ST Assignment'

st.set_page_config(page_title=apptitle, page_icon='random', layout= 'wide', initial_sidebar_state="expanded")
# random icons in the browser tab

st.title('ST assignment on the go..')
st.balloons()
# Let's add a sub-title
st.write("A **_cool_** ST assignment application")

df1 = pd.read_csv("PO.csv")
df2 = pd.read_csv("PO_GBW.csv")

complexST = st.radio(
 	'Complex?',
 	('COMPLEX', 'NON-COMPLEX'))

PPVC = st.radio(
 	'PPVC?',
 	('PPVC', 'NON-PPVC'))

storey = st.radio(
 	'How many storeys?',
 	('> 30 storeys', '< 30 storeys but > 10 storeys', '< 10 storeys'))


st.write(f'The project is {complexST}, {PPVC} and {storey}.')


if PPVC == 'PPVC':
    df = df1[df1['PPVClist'] == 1]
    df = df[df['Can Assign?'] == 1]
    df["ppvc_next"] = df["ppvc_next"].astype(float)
    df = df.sort_values(
        by="ppvc_next",
        ascending=False)
    st.write("Structural PO list:")
    st.write(df[["PO_name", "Department", "Yrs_of_Exp", "ppvc_lastdate", "ppvc_next"]])

else:
    if storey == "> 30 storeys":
        df = df1[df1['PPVClist'] == 0] #cannot be in the PPVC list
        df = df[df['Yrs_of_Exp'] >= 3]
        df = df[df['Can Assign?'] == 1]
        df["30storey_next"] = df["30storey_next"].astype(float)
        df = df.sort_values(
            by="30storey_next",
            ascending=False)
        st.write("Structural PO list:")
        st.write(df[["PO_name", "Department", "Yrs_of_Exp", "30storey_lastdate", "30storey_next"]])
        
        #GBW PO list
        df_gbw = df2[df2['Can Assign?'] == 1]
        df_gbw["30storey_next"] = df_gbw["30storey_next"].astype(float)
        df_gbw = df_gbw.sort_values(
            by="30storey_next",
            ascending=False)
        st.write("GBW PO list:")
        st.write(df_gbw[["PO_name", "Department", "Yrs_of_Exp", "30storey_lastdate", "30storey_next"]])
    
    else:
        if complexST == "COMPLEX":
            if storey == "< 10 storeys":
                df = df1[df1['PPVClist'] == 0] #cannot be in the PPVC list
                df = df1[df1['<10+complexlist'] == 1]
                df = df[df['Can Assign?'] == 1]
                df["10storey_next"] = df["10storey_next"].astype(float)
                df = df.sort_values(
                    by="10storey_next",
                    ascending=False)
                st.write("Structural PO list:")
                st.write(df[["PO_name", "Department", "Yrs_of_Exp", "10storey_lastdate", "10storey_next"]])

            else:
                df = df1[df1['PPVClist'] == 0] #cannot be in the PPVC list
                df = df[df['Yrs_of_Exp'] >= 3]
                df = df[df['Can Assign?'] == 1]
                df["30storey_next"] = df["30storey_next"].astype(float)
                df = df.sort_values(
                    by="30storey_next",
                    ascending=False)
                st.write("Note: For Complex STs, use the same PO list for > 30 storey.")
                st.write("Structural PO list:")
                st.write(df[["PO_name", "Department", "Yrs_of_Exp", "30storey_lastdate", "30storey_next"]])

        else:
            if storey == "< 10 storeys":
                st.write("There is no need for assignment.")
               
            else:
                df = df1[df1['Can Assign?'] == 1]
                df = df1[df1['PPVClist'] == 0] #cannot be in the PPVC list
                df["10storey_next"] = df["10storey_next"].astype(float)
                df = df.sort_values(
                    by="10storey_next",
                    ascending=False)
                st.write("Structural PO list:")
                st.write(df[["PO_name", "Department", "Yrs_of_Exp", "10storey_lastdate", "10storey_next"]])


