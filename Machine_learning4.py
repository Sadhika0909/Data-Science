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
#Top ten most affected countries
a=px.scatter(ttcon,x=ttcon.index,#country names
             y="Confirmed",#number of confirmed cases
             size="Confirmed",#bubble size
             color=ttcon.index,
             title="Number of confirmed cases per country")
a.write_html("Covid cases.html",auto_open=True)

#data analysis
#Top ten recovered countries bar plot
r=pd.DataFrame(data.groupby("Country")["Recovered"].sum().nlargest(10).sort_values(ascending=False))
b=px.bar(r,x=r.index,y="Recovered",height=600,color="Recovered",title="Top Ten Recovered Cases",color_continuous_scale=px.colors.sequential.Viridis)
b.write_html("Covid cases Recovered.html",auto_open=True)

#Top ten countries with the highest death cases
#bubble plot
ttdea=pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False))
d=px.scatter(ttdea,x="Deaths",y=ttdea.index,color="Deaths",orientation="h",title="Top Ten countries with the highest death cases",color_continuous_scale=["deepskyblue","red"])
d.write_html("Covid cases deaths.html",auto_open=True)

#USA
#Finding most affected states in big countries
tops=data["Country"]=="US"
tops=data[tops].nlargest(5,"Confirmed")
#Brazil
t=data["Country"]=="Brazil"
t=data[t].nlargest(4,"Confirmed")
#India
top=data["Country"]=="India"
top=data[top].nlargest(5,"Confirmed")
#Russia
tt=data["Country"]=="Russia"
tt=data[tt].nlargest(5,"Confirmed")

#Bar chart for US
bus=go.Figure(data=[go.Bar(name="Confirmed cases",x=tops["Confirmed"],y=tops["Confirmed"],orientation="h"),go.Bar(name="Death cases",x=tops["Deaths"],y=tops["Deaths"],orientation="h")])
bus.update_layout(title="Most affected states in USA",height=600)
bus.write_html("Most affected states in USA.html",auto_open=True)

#Stacked bar for Brazil
sb=go.Figure(data=[go.Bar(name="Confirmed cases",x=t["State"],y=t["Confirmed"]),
                    go.Bar(name="Recovered cases",x=t["State"],y=t["Recovered"]),
                    go.Bar(name="Death cases",x=t["State"],y=t["Deaths"])])
sb.update_layout(title="Most affected states in Brazil",barmode="stack",height=600)
sb.write_html("Most affected states in Brazil.html",auto_open=True)



