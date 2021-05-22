import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("D:/Stuff/Work/Uni/2021/Professional Studio A/Code/PE_Ratio_Compare.csv")

barchart = px.bar(
	data_frame = df,
	x = "PE Ratio",
	y = " ",
	orientation = "h",
	title = "Price to Earnings Ratio"
)

barchart.update_layout(
    autosize=False,
    width=500,
    height=500)

barchart.write_html("D:/Stuff/Work/Uni/2021/Professional Studio A/Code/barChart.html")
