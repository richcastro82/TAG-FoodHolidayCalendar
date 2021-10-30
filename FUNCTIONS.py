#Richard Castro
#Functions for holiday Topbar
from LIBRARIES import *
from datetime import datetime
df=pd.read_csv('Holiday-List.csv')
holidays=[]

for i in df.Holiday:
    holidays.append('{}'.format(i))
date = datetime.now()

app = dash.Dash(
        __name__,
        meta_tags=[
            {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
            }],)

server = app.server
app.config["suppress_callback_exceptions"] = True


app.layout = html.Div(
    className="container scalable",
    children=[
            html.Div(
            id='',children=[
                date.strftime("%m/%d")])
            ])
