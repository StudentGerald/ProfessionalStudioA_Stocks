import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


df = pd.DataFrame(dict(
    r=[5, 5, 3, 0, 3],
    theta=['Past','Health','Future',
           'Dividend', 'Value']))
fig = px.line_polar(df, r='r', theta='theta', title="GOOGLE Snowflake Analysis", line_close=True)
fig.update_traces(fill='toself')
fig.update_layout(
    autosize=False,
    width=500,
    height=500)

fig.write_html("D:/Stuff/Work/Uni/2021/Professional Studio A/Code/testCompany1.html")
