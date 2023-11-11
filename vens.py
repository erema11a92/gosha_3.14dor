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
        html.P('Этот дашборд предоставляет информацию о количестве солнечной радиации для различных временных интервалов.',
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
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        # Гистограмма
        dcc.Graph(id='histogram'),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        # Круговая диаграмма
        dcc.Graph(id='pie-chart'),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        # Ящик с усами
        dcc.Graph(id='box-plot'),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        # Точечный график
        dcc.Graph(id='scatter-plot'),
    ], style={'width': '48%', 'display': 'inline-block'}),

], style={'padding': '20px'})

# Определение логики дашборда
@app.callback(
    Output('line-chart', 'figure'),
    Output('histogram', 'figure'),
    Output('pie-chart', 'figure'),
    Output('box-plot', 'figure'),
    Output('scatter-plot', 'figure'),
    [Input('date-dropdown', 'value')]
)
def update_charts(selected_date):
    # Линейный график
    line_chart = go.Figure(go.Scatter(x=df['Дата'], y=df['Количество солнечной радиации (в Ваттах/квадратный метр)']))
    line_chart.update_layout(title='Линейный график',
                             xaxis_title='Дата',
                             yaxis_title='Количество солнечной радиации (в Ваттах/квадратный метр)',
                             plot_bgcolor='rgb(230, 230, 230)')

    # Гистограмма
    histogram = go.Figure(go.Histogram(x=df['Количество солнечной радиации (в Ваттах/квадратный метр)']))
    histogram.update_layout(title='Гистограмма',
                            xaxis_title='Количество солнечной радиации (в Ваттах/квадратный метр)',
                            yaxis_title='Количество наблюдений',
                            plot_bgcolor='rgb(230, 230, 230)')

    # Круговая диаграмма
    pie_chart = px.pie(df, names='Время изменения', values='Количество солнечной радиации (в Ваттах/квадратный метр)',
                       title='Круговая диаграмма')

    # Ящик с усами
    box_plot = px.box(df, x='Время изменения', y='Количество солнечной радиации (в Ваттах/квадратный метр)',
                      title='Ящик с усами')

    # Точечный график
    scatter_plot = px.scatter(df, x='Время изменения', y='Количество солнечной радиации (в Ваттах/квадратный метр)',
                             title='Точечный график')

    return line_chart, histogram, pie_chart, box_plot, scatter_plot

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)