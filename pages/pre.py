import streamlit as st
import graphviz as gv
from io import StringIO
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
from p import info,getallcatfig,describe_column,getallconfigs,gettopnfeatures,violin_plot,oversampling,getClassificationReport

# initial config

kdf = pd.read_csv('kidney.csv')
kdf.drop(columns = ['PatientID', 'DoctorInCharge'], inplace = True)
cat_cols = [col for col in kdf.columns if kdf[col].nunique() < 6]
num_cols = [col for col in kdf.columns if col not in cat_cols]
cat_cols.remove("Diagnosis")
totalcols = kdf.columns.tolist()


st.title("pre processing page",anchor=False)
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

with st.expander(" Click to show plots"):
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

with st.expander(" Click to show plots"):
    for i,fig in enumerate(configs) :
        with st.container(border=True):
            col1,col2 = st.columns([4,3])
            with col1:
                st.plotly_chart(fig)
            with col2:
                st.write(f"Description of {num_cols[i]}")
                des = describe_column(df=kdf,column_name=num_cols[i])
                st.dataframe(des)        
                
            
            
with  st.container(border=True):
    st.subheader("Get Top 20 features from the dataframe",anchor=False)
    
    st.write("") 
    rdf = gettopnfeatures(n=20,df= kdf) 
    rdf.drop([0],inplace=True)
    rdf = rdf.head( 20)
    st.dataframe(data=rdf,height=500)
    st.text(' ')
    st.subheader("Visualizing Top 2 feature Vs Diagnosis in a Violoin Plot")
    fig1 = violin_plot(kdf,"SerumCreatinine","Diagnosis")
    st.plotly_chart(fig1)
    fig2 = violin_plot(kdf,"GFR","Diagnosis")
    st.plotly_chart(fig2)

st.subheader("3rd Step : To remove both single variate and multi-variate outliers from the data-frame")

with st.container(border=True):
    st.subheader("Outlier Detection",anchor=False)
    
    st.write("Using IQR  method to remove single variate outlier")
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*ZrRgmtVHMVLknr7BmezXlg.jpeg")
    st.write(' ')
    st.write("*********Using Mahalanobis  distance to remove multivariate outliers**********")
    st.write("Mahalanobis distance is a statistical technique used to identify and remove outliers in multivariate data (data with multiple variables)")
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*Zj_jFn6SfDPwmasUBCAR1A.png")
        
with st.container(border=True):
    st.subheader("Data Binning",anchor=False)
    
    st.write("*Data binning, also known as data discretization, is a technique used in data preprocessing that groups continuous values into discrete intervals or bins. This process helps in reducing the effects of minor observation errors and enhances the performance of models by simplifying the data.*")    
    
    st.write("__Here Age column has been binned into three bins Teenage , Adult and Senior__ ")
    
    
with st.container(border=True):
    st.subheader("SMOTE",anchor=False)
    
    info = kdf["Diagnosis"].value_counts()
    st.write("*SMOTE is an oversampling technique that creates synthetic samples of the minority class by interpolating between existing minority class instances.The goal of SMOTE is to balance the class distribution by generating synthetic examples rather than by duplicating existing ones, which helps prevent overfitting.*")     
    st.write("__Before oversampling__")
       
    st.dataframe(info) 
    oversampldf = oversampling(df=kdf,target='Diagnosis')
    st.write("__After Oversampling__")
    newinfo = oversampldf['Diagnosis'].value_counts()
    st.dataframe(newinfo) 
    
with st.container(border=True):
    st.subheader("Min-max scaling",anchor=False)
    st.write("*Min-max scaling, also known as min-max normalization, transforms numerical features to a common scale, typically [0, 1]. It rescales features by shifting and scaling values to a specified range, where the minimum value of the feature becomes 0 and the maximum value becomes . Min-max scaling preserves the original distribution and relationships between data points.*") 
    st.text(" ")
    st.write("__Classification Report after Training a Random Forest Model__")   
    report = getClassificationReport(df=kdf)
    csv_file = StringIO(report)
    # Convert the string to a DataFrame
    reportdf = pd.read_csv(csv_file)
    st.dataframe(reportdf)
 
   
    
    
    