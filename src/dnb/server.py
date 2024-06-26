from multiprocessing import Condition

import pandas as pd
import plotly.express as px
import setproctitle
from dash import Dash, html, dcc, callback, Output, Input

from dnb.domino import terminate_when_parent_process_dies


def start_dash(host: str, port: int, server_is_started: Condition):
    # Set the process title.
    setproctitle.setproctitle('dnb-dash')
    # When the parent dies, follow along.
    terminate_when_parent_process_dies()

    # The following is the minimal sample code from dash itself:
    # https://dash.plotly.com/minimal-app

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

    app = Dash()

    app.layout = [
        html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        dcc.Graph(id='graph-content')
    ]

    @callback(
        Output('graph-content', 'figure'),
        Input('dropdown-selection', 'value')
    )
    def update_graph(value):
        dff = df[df.country == value]
        return px.line(dff, x='year', y='pop')

    with server_is_started:
        server_is_started.notify()

    # debug cannot be True right now with nuitka: https://github.com/Nuitka/Nuitka/issues/2953
    app.run(debug=False, host=host, port=port)
