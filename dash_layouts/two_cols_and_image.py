import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    html.Div(
        className="row",
        children=[
            html.Div(
                className="six columns",
                children=[
                    html.Div(
                        children=dcc.Graph(
                            id='left-graph',
                            figure={
                                'data': [{
                                    'x': [1, 2, 3],
                                    'y': [3, 1, 2],
                                    'type': 'bar',
                                    'marker': {'color': 'green'},
                                }],
                                'layout': {
                                    'height': 800,
                                    'margin': {
                                        'l': 10, 'b': 20, 't': 0, 'r': 0
                                    }
                                }
                            }
                        )
                    )
                ]
            ),
            html.Div(
                className="six columns",
                children=html.Div([
                    dcc.Graph(
                        id='right-top-graph',
                        figure={
                            'data': [{
                                'x': [1, 2, 3],
                                'y': [3, 1, 2],
                                'type': 'bar'
                            }],
                            'layout': {
                                'height': 400,
                                'margin': {'l': 10, 'b': 20, 't': 0, 'r': 0}
                            }
                        }
                    ),
                    html.Img(
                        id='right-bottom-image',
                        src='assets/classroom.jpg',
                        style={'max-width': '100%', 'height': '400px'},
                    ),

                ]),
                style={'text-align': 'center'},
            )
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
