# tejaswee testing plots and data preprocessing
import streamlit as st
import plotly.express as px # type: ignore
import pandas as pd
import numpy as np
import plotly.graph_objects as go

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")