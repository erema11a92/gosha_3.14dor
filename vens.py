import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
# Загрузка данных
df = pd.read_csv(r"C:\Users\Admin\PycharmProjects\pythonProject\venv\ху_ня.csv")
# Создание экземпляра приложения
app = dash.Dash(__name__)
# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)