import pandas as pd
import plotly.graph_objects as go

#reading the csv file
data=pd.read_csv("Covid_time.csv",encoding="ISO-8859-1")

data.columns=("Date","Code","Country","WHO","New_cases","Cl_cases","New_deaths","Cl_deaths")
data["Date"]=pd.to_datetime(data["Date"])

a=data.groupby("Date").sum()
#line graph for cumulative COVID cases over time
figure1=go.Figure()
figure1.add_trace(go.Scatter(x=a.index,y=a["Cl_cases"],fill="tonexty",line_color="blue"))
figure1.update_layout(title="Cumulative COVID-19 cases over time")
figure1.write_html("Covid_time.html",auto_open=True)

#line graph for cumulative death cases over time
figure2=go.Figure()
figure2.add_trace(go.Scatter(x=a.index,y=a["Cl_deaths"],fill="tonexty",line_color="green"))
figure2.update_layout(title="Cumulative COVID-19 death cases over time")
figure2.write_html("Covid_death.html",auto_open=True)

#daily new cases line graph
figure3=go.Figure()
figure3.add_trace(go.Scatter(x=a.index,y=a["New_cases"],fill="tonexty",line_color="magenta"))
figure3.update_layout(title="New COVID-19 cases over time")
figure3.write_html("Covid_new_cases.html",auto_open=True)

#daily new deaths line graph
figure4=go.Figure()
figure4.add_trace(go.Scatter(x=a.index,y=a["New_deaths"],fill="tonexty",line_color="red"))
figure4.update_layout(title="New COVID-19 death cases over time")
figure4.write_html("Covid_new_deaths.html",auto_open=True)