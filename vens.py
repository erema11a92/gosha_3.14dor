import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Загрузка данных
file_path = "D:\gitititi\gosha_3.14dor\ху_ня.csv"
df = pd.read_csv(file_path)

# Создание экземпляра приложения
app = dash.Dash(__name__)

# Определение структуры дашборда
app.layout = html.Div([
    html.Div([
        html.H1('Дашборд анализа солнечной радиации', style={'textAlign': 'center'}),
        html.P('Этот дашборд предоставляет информацию о солнечной радиации для различных временных интервалов.',
               style={'textAlign': 'center'}),
        html.Div([
            html.Label('Выберите дату:', style={'fontSize': 18}),
            dcc.Dropdown(
                id='date-dropdown',
                options=[{'label': date, 'value': date} for date in df['date']],
                value=df['ghi'].iloc[0],
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
    line_chart = go.Figure()
    line_chart.add_trace(go.Scatter(x=df['date'], y=df['ghi'], mode='lines', name='GHI'))
    line_chart.add_trace(go.Scatter(x=df['date'], y=df['dni'], mode='lines', name='DNI'))
    line_chart.add_trace(go.Scatter(x=df['date'], y=df['dhi'], mode='lines', name='DHI'))
    line_chart.update_layout(title='График солнечной радиации',
                             xaxis_title='Дата',
                             yaxis_title='Солнечная радиация (в Ваттах/квадратный метр)',
                             plot_bgcolor='rgb(230, 230, 230)')

    # Гистограмма
    histogram = go.Figure(go.Histogram(x=df['ghi']))
    histogram.update_layout(title='Гистограмма солнечной радиации',
                            xaxis_title='Солнечная радиация (в Ваттах/квадратный метр)',
                            yaxis_title='Частота',
                            plot_bgcolor='rgb(230, 230, 230)')

    # Круговая диаграмма
    pie_chart = px.pie(df, names='date', values='ghi', title='Круговая диаграмма солнечной радиации')

    # Ящик с усами
    box_plot = px.box(df, x='date', y='ghi', title='Ящик с усами солнечной радиации')

    # Точечный график
    scatter_plot = px.scatter(df, x='date', y='ghi', title='Точечный график солнечной радиации')

    return line_chart, histogram, pie_chart, box_plot, scatter_plot

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
