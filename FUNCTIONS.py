# RICHARD CASTRO
# FOOD HOLIDAY APP
# DECEMBER 2022
from datetime import date
import pandas as pd
import dash
import dash_html_components as html
from datetime import datetime
date = datetime.now().strftime("%m/%d")
displayHoliday="assets/placeholder.png"

holidays=pd.read_csv('Holiday-db.csv', header=None, index_col=0, squeeze=True).to_dict()
for key,value in holidays.items():
    if (key == date):
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
    className="Content-Box",
    children=[
        html.Div(
            className="Bod",
            children=[
                html.Div(
                id='Holi-Content-Box',
                className="HoliBox",
                children=[
                    html.Img(
                    id='HoliImg',
                    className="HoliImg",
                    src=displayHoliday)]),
                    ]),
                ])
