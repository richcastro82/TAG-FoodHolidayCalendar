#Richard Castro
#Functions for holiday Topbar
from LIBRARIES import *
from datetime import datetime
date = datetime.now()
dat=date.strftime("%m/%d")
displayHoliday='No Holiday'

holidays=pd.read_csv('Holiday-List.csv', header=None, index_col=0, squeeze=True).to_dict()
for key,value in holidays.items():
    if (key == dat):
        displayHoliday=value

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
    className="box",
    children=[
            html.Div(
            id='', className="contentBox",children=[
            html.A(
            id='', className="content",children=[dat,' - ',displayHoliday])
            ])
            ])
