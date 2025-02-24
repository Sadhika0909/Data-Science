import pandas as pd
import plotly.graph_objects as go

data=pd.read_csv("Covid_time.csv",encoding="ISO-8859-1")

data.columns=("Date","Code","Country","WHO","New_cases","Cl_cases","New_deaths","Cl_deaths")
data["Date"]=pd.to_datetime(data["Date"])
