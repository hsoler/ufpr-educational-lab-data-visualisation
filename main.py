import numpy as np
import pandas as pd
import plotly

path = "./DataBases/fineduc/"

santa_quiteria = pd.read_csv(path + "santa-quiteria.csv", sep=";", decimal=",", thousands=".", index_col=0)
sao_luis = pd.read_csv(path + "sao-luis.csv", sep=";", decimal=",", thousands=".", index_col=0)

years = [i for i in range(2007, 2021)]

def my_plotter(df, city_name, yrange, ytick):
    fig = plotly.graph_objs.Figure()
    fig.layout.title.text = "Evolução do número de matrículas no município de " + city_name + " por dependência administrativa"
    fig.layout.xaxis.type = "linear"
    fig.layout.xaxis.title.text = "Tempo (em anos)"
    fig.layout.xaxis.range = (2007, 2020)
    fig.layout.xaxis.dtick = 1
    fig.layout.yaxis.type = "linear"
    fig.layout.yaxis.title.text
    fig.layout.yaxis.range = (0, yrange)
    fig.layout.yaxis.dtick = ytick
    for i, dep_adm in enumerate(df.index):
        trace = plotly.graph_objs.Scatter()
        trace.name = dep_adm
        trace.mode = "lines"
        trace.x = years
        trace.y = df.loc[dep_adm]
        trace.line.dash = "dashdot"
        trace.line.color = plotly.colors.qualitative.D3[i]
        trace.line.shape = "linear"
        fig.add_trace(trace)
    return fig

def run():
    fig_sq = my_plotter(santa_quiteria, "Santa Quitéria", 15000, 1000)
    fig_sl = my_plotter(sao_luis, "São Luís", 400000, 40000)
    return fig_sq, fig_sl

