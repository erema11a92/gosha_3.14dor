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

# Определение структуры дашборда
app.layout = html.Div([
    html.Div([
        html.H1('Дашборд анализа данных о количестве солнечной радиации', style={'textAlign': 'center'}),
        html.P(
            'Этот дашборд предоставляет информацию о количестве солнечной радиации для различных временных интервалов.',
            style={'textAlign': 'center'}),
        html.Div([
            html.Label('Выберите дату:', style={'fontSize': 18}),
            dcc.Dropdown(
                id='date-dropdown',
                options=[{'label': date, 'value': date} for date in df['Дата']],
                value=df['Дата'].iloc[0],
                clearable=False,
                style={'width': '50%', 'margin': '0 auto'}
            ),
        ], style={'textAlign': 'center', 'marginBottom': '30px'}),
    ], style={'marginBottom': '30px'}),

    html.Div([
        # Линейный график
        dcc.Graph(id='line-chart'),
    ], style={'width': '48%', 'display': 'inline-block'})
])


@app.callback(
    Output('line-chart', 'figure'),
    [Input('date-dropdown', 'value')]
)
def update_charts(selected_date):
    # Линейный график
    line_chart = go.Figure(go.Scatter(x=df['Дата'], y=df['Количество солнечной радиации (в Ваттах/квадратный метр)']))
    line_chart.update_layout(title='Линейный график',
                             xaxis_title='Дата',
                             yaxis_title='Количество солнечной радиации (в Ваттах/квадратный метр)',
                             plot_bgcolor='rgb(230, 230, 230)')
    return line_chart


# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
