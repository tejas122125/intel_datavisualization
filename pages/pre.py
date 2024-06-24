import streamlit as st
import graphviz as gv
import pandas as pd
import streamlit as st
import plotly.express as px # type: ignore
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import scipy.optimize
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from p import info,getallcatfig,describe_column,getallconfigs

# initial config

kdf = pd.read_csv('kidney.csv')
kdf.drop(columns = ['PatientID', 'DoctorInCharge'], inplace = True)
cat_cols = [col for col in kdf.columns if kdf[col].nunique() < 6]
num_cols = [col for col in kdf.columns if col not in cat_cols]
cat_cols.remove("Diagnosis")
totalcols = kdf.columns.tolist()


st.title("pre processing page")
quote = "Without data you are another person with an opnion"
author = "W.Edward's Duming"

# Display the quote using Markdown
st.markdown(f"""
    <div style="background-color:#0E1117;padding:20px;border-radius:10px;">
        <p style="font-size:24px;font-style:italic;text-align:center;">"{quote}"</p>
        <p style="font-size:20px;text-align:right;margin-right:20px;">- {author}</p>
    </div>
""", unsafe_allow_html=True)

with st.container(border=True):
    st.write(f"1st basic step involves understanding the features of data and to remove any NULL values. Here in the Kidney dataset there in no NULL values in any column. With df.info() we get to know about data types and null values count ")

    st.write(np.round(kdf.describe(),1),height=400)
st.write("2nd Step : visualizing each column and its mathematical summary")   

catfigures = getallcatfig(kdf,cat_cols=cat_cols)

for i,fig in enumerate(catfigures) :
    with st.container(border=True):
        col1,col2 = st.columns([4,3])
        
        with col1:
            st.plotly_chart(catfigures[i])
        with col2:
            st.write(f"Description of {cat_cols[i]}")
            des = describe_column(df=kdf,column_name=cat_cols[i])
            st.dataframe(des)    


configs = getallconfigs(df=kdf,num_cols=num_cols)


for i,fig in enumerate(configs) :
    with st.container(border=True):
        col1,col2 = st.columns([4,3])
        
        with col1:
            st.plotly_chart(fig)
        with col2:
            st.write(f"Description of {num_cols[i]}")
            des = describe_column(df=kdf,column_name=num_cols[i])
            st.dataframe(des)        