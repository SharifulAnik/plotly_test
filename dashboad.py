import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pickle

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

figure = go.Figure(data=data)
app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Graph(
        figure=figure,
        style={'width': '1100px', 'height': '700px'}
    )
])

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
