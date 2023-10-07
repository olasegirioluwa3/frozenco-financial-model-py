from learndash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World'),
    html.H1(children='hi')
])

if __name__ == '__main__':
    app.run_server(debug=True)