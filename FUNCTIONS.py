#Richard Castro
#Functions for holiday Topbar
from LIBRARIES import *
df=pd.read_csv('Holiday-List.csv')
holidays=[]

for i in df.Holiday:
    holidays.append('{}'.format(i))

app = dash.Dash(
        __name__,
        meta_tags=[
            {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
            }],)

server = app.server
app.config["suppress_callback_exceptions"] = True


def build_branding():
    return html.Div()


app.layout = html.Div(
    className="container scalable",
    children=[
            # CLIENT BRANDING ON THE HTML
            html.Div(
            id='build-branding',children=[
            dcc.Dropdown(
                id="", multi=True, searchable=True,
                options=[{"label": i, "value": i} for i in holidays],
                value=""
            )
            ]),
],)
