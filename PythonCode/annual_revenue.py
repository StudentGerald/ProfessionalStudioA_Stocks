import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("D:/Stuff/Work/Uni/2021/Professional Studio A/Code/Python functions/annual_revenue.csv")

barchart = px.bar(
	data_frame = df,
	x = "Date",
	y = "Annual Revenue",
	orientation = "v",
	title = "Google Annual Revenue"
)

barchart.update_layout(
    autosize=False,
    width=1000,
    height=500)

barchart.write_html("D:/Stuff/Work/Uni/2021/Professional Studio A/Code/Stock HTML/annualRevenue1.html")
