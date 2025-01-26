#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#reading the csv file
data=pd.read_csv("covid_data.csv")
#keeping specific columns
data=data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]
#rename
data.columns=("State","Country","LastUpdate","Lat","Long","Confirmed","Recovered","Deaths","Active")
#filling empty values
data["State"].fillna(value="",inplace=True)
#finding the top ten contries with confirmed cases
ttcon=pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
#creating a bubble chart
a=px.scatter(ttcon,x=ttcon.index,#country names
             y="Confirmed",#number of confirmed cases
             size="Confirmed",#bubble size
             color=ttcon.index,
             title="Number of confirmed cases per country")
a.write_html("Covid cases.html",auto_open=True)



