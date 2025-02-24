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




