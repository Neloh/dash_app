from dash import Dash, html, dcc, callback, Input, Output
from flask import Flask

server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    external_stylesheets=[
        'https://codepen.io/amyoshino/pen/jzXypZ.css'
    ]
)

# For Bootstrap CSS
#app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Hello World',
                        className='nine columns'),
                html.Img(
                    src="http://test.fulcrumanalytics.com/wp-content/uploads/2015/10/Fulcrum-logo_840X144.png",
                    className='three columns',
                    style={
                        'height': '9%',
                        'width': '9%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                    },
                ),
                html.Div(children='''
                        Dash: A web application framework for Python.
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose City:'),
                        dcc.Checklist(
                                id='Cities',
                                options=[
                                    {'label': 'San Francisco', 'value': 'SF'},
                                    {'label': 'Montreal', 'value': 'MT'}
                                ],
                                value=['SF', 'MT'],
                                inline=True  # replaces labelStyle
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph'
                )
                ], className='six columns'
                ),

                html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 9, 8], 'type': 'line', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Graph 2'
                        }
                    }
                )
                ], className='six columns'
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one')
)

@callback(
    Output('example-graph', 'figure'),
    [Input('Cities', 'value')])
def update_graph_1(selector):
    data = []
    if 'SF' in selector:
        data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'})
    if 'MT' in selector:
        data.append({'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 1',
            'xaxis': dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis': dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@callback(
    Output('example-graph-2', 'figure'),
    [Input('Cities', 'value')])
def update_graph_2(selector):
    data = []
    if 'SF' in selector:
        data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'})
    if 'MT' in selector:
        data.append({'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 2',
            'xaxis': dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis': dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=False)
