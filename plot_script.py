import plotly.graph_objs as go
import plotly.io as pio

# Create a simple line plot
data = [go.Scatter(x=[1, 2, 3, 4, 5], y=[10, 11, 12, 13, 14])]

# Define the layout
layout = go.Layout(title='Simple Line Plot')

# Create the figure
fig = go.Figure(data=data, layout=layout)

# Save the plot as an HTML file
pio.write_html(fig, file='simple_line_plot.html', auto_open=True)
