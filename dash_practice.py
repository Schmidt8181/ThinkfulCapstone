import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

'''
    dcc.Graph(id='predicted',
        figure={
            'data': [
                {'x': , 'y': ,
                'type': 'line', 'name': 'Predicted Prices'}
                ],
            'layout': {'title': 'Price Forecast'}
                },
        style={'width': '600', 'display': 'inline-block'}),
    ], style={'display': 'inline-block'}
'''


df = pd.read_csv('Food_price_indices_data_jul.csv')

After2005 = df[192:]
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Thinkful DataScience Final Capstone',
        style={'text-align': 'center'}),
    html.Div(
    children='''
        In this capstone, I would like to build a dashboard as a proof of concept
        that allows a user to choose a food item from a limited drop down menu
        that will then show them the recent local prices of said food item and forecast
        if that item will be going up or down in price.
    '''),
    html.Div(children=[
        dcc.Dropdown(id='drop_down',
        options=[
            {'label': 'Food Price Index', 'value': 'Food Price Index'},
            {'label': 'Oils Price Index', 'value': 'Oils Price Index'},
            {'label': 'Cereals Price Index', 'value': 'Cereals Price Index'},
            {'label': 'Sugar Price Index', 'value': 'Sugar Price Index'},
            {'label': 'Dairy Prince Index', 'value': 'Dairy Price Index'},
            {'label': 'Meat Price Index', 'value': 'Meat Price Index'},
            ],
            value='Food Price Index'),
         dcc.Graph(id='graphs',
            style={'width': '600', 'display': 'inline-block'})
])
])

@app.callback(
    Output(component_id='graphs', component_property='figure'),
    [Input(component_id='drop_down', component_property='value')]
)
def update_output_div(drop_down):
    return {'data':[
                    {'x': After2005.Date, 'y': After2005[drop_down], 'type': 'line', 'name': drop_down},
                    ],
            'layout': go.Layout(
                xaxis={'title': "Month"},
                yaxis={'title': drop_down}
            )
            }


if __name__ == '__main__':
    app.run_server(debug=True)
