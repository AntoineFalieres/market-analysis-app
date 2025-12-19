import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_candlestick_chart(df, indicators_to_show):
    # Create subplots: Row 1 for Price, Row 2 for Volume/RSI
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'), 
                        row_width=[0.2, 0.7])

    # 1. Main Candlestick
    fig.add_trace(go.Candlestick(
        x=df['timestamp'],
        open=df['open'], high=df['high'],
        low=df['low'], close=df['close'],
        name="Price"
    ), row=1, col=1)

    # 2. Add VWMA if it exists in the dataframe
    vwma_cols = [c for c in df.columns if 'vwma' in c.lower()]
    for col in vwma_cols:
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df[col], name=col.upper()), row=1, col=1)

    # 3. Volume bars in the second row
    fig.add_trace(go.Bar(x=df['timestamp'], y=df['volume'], name="Volume", marker_color='gray'), row=2, col=1)

    fig.update_layout(xaxis_rangeslider_visible=False, height=800, template="plotly_dark")
    return fig