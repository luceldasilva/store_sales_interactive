import plotly_express as px
import pandas as pd

def grafico_barras_producto(data):
    revenues_productos = (
        data.groupby("tipo_producto")["valor_total"].sum()
        .sort_values(ascending = True)
        .reset_index().tail(10)
    )
    
    # Creando el gráfico
    fig = px.bar(revenues_productos.head(10),
        x = 'valor_total',
        y = 'tipo_producto',
        text = 'valor_total',
        title = "Top ingresos por Producto ($)"
    )
    fig.update_layout(
        yaxis_title='Ingresos ($)',
        xaxis_title='Tipo de Producto',
        showlegend=False,
        title_x=0.4  # Centra el título
    )
    fig.update_xaxes(tickangle=45)
    fig.update_traces(
        texttemplate = '%{text:.3s}',
        hovertemplate = '<b>%{y}</b><br>Ingresos totales: $%{x:,.0f}<extra></extra>'
    )
    return fig