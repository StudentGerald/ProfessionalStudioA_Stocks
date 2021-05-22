import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("D:/Stuff/Work/Uni/2021/Professional Studio A/Code/Python functions/total_Assets.csv")

barchart = px.bar(
	data_frame = df,
	x = "Date",
	y = "Total Assets",
	orientation = "v",
	title = "Google Annual Total Assets"
)

barchart.update_layout(
    autosize=False,
    width=1000,
    height=500)

barchart.write_html("D:/Stuff/Work/Uni/2021/Professional Studio A/Code/Stock HTML/total_Assets1.html")
