import pandas as pd
import plotly.graph_objects as go

data=pd.read_csv("Covid_time.csv",encoding="ISO-8859-1")

data.columns=("Date","Code","Country","WHO","New_cases","Cl_cases","New_deaths","Cl_deaths")
data["Date"]=pd.to_datetime(data["Date"])
#filtering data for India
india=data[data["Country"]=="India"]
india_date=india.groupby("Date").sum()

#India specific graph
#Cumulative cases in India
figure1=go.Figure()
figure1.add_trace(go.Scatter(x=india_date.index,y=india_date["Cl_cases"],fill="tonexty",line_color="cyan"))
figure1.update_layout(title="Cumulative cases in India")
figure1.write_html("Cl_India.html",auto_open=True)

#Cumulative deaths in India
figure2=go.Figure()
figure2.add_trace(go.Scatter(x=india_date.index,y=india_date["Cl_deaths"],fill="tonexty",line_color="green"))
figure2.update_layout(title="Cumulative deaths in India")
figure2.write_html("Cl_Deaths.html",auto_open=True)

#daily new cases line graph India
figure5=go.Figure()
figure5.add_trace(go.Scatter(x=india_date.index,y=india_date["New_cases"],fill="tonexty",line_color="blue"))
figure5.update_layout(title="New COVID-19 cases over time in India")
figure5.write_html("Covid_new_casesI.html",auto_open=True)

#daily new deaths line graph India
figure6=go.Figure()
figure6.add_trace(go.Scatter(x=india_date.index,y=india_date["New_deaths"],fill="tonexty",line_color="red"))
figure6.update_layout(title="New COVID-19 death cases over time in India")
figure6.write_html("Covid_new_deathsI.html",auto_open=True)

#filtering data for US
us=data[data["Country"]=="United States of America"]
us_date=us.groupby("Date").sum()

#US specific graph
#Cumulative cases in US
figure3=go.Figure()
figure3.add_trace(go.Scatter(x=us_date.index,y=us_date["Cl_cases"],fill="tonexty",line_color="magenta"))
figure3.update_layout(title="Cumulative cases in the USA")
figure3.write_html("Cl_US.html",auto_open=True)

#Cumulative deaths in US
figure4=go.Figure()
figure4.add_trace(go.Scatter(x=us_date.index,y=us_date["Cl_deaths"],fill="tonexty",line_color="blue"))
figure4.update_layout(title="Cumulative deaths in the USA")
figure4.write_html("Cl_DeathsUS.html",auto_open=True)

#daily new cases line graph US
figure7=go.Figure()
figure7.add_trace(go.Scatter(x=us_date.index,y=us_date["New_cases"],fill="tonexty",line_color="yellow"))
figure7.update_layout(title="New COVID-19 cases over time in the USA")
figure7.write_html("Covid_new_casesUS.html",auto_open=True)

#daily new deaths line graph US
figure8=go.Figure()
figure8.add_trace(go.Scatter(x=us_date.index,y=us_date["New_deaths"],fill="tonexty",line_color="black"))
figure8.update_layout(title="New COVID-19 death cases over time in the USA")
figure8.write_html("Covid_new_deathsUS.html",auto_open=True)
