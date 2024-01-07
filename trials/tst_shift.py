import altair as alt
from altair import display

# Sample data
data = {'x': ['A', 'B', 'C', 'D'], 'y': [4, 6, 5, 8]}

# Create base chart with initial encodings
base = alt.Chart(data).encode(
    x='x:O',
    y='y:Q'
)

# Shift bars horizontally using a calculated offset
bars = base.mark_bar().encode(
    x='x:O',  # Use the original x-axis
    xOffset='shift:Q'  # Use xOffset for the calculated shift
)

# Calculate the shift values (adjust as needed)
shift = alt.Chart(data).transform_calculate(
    shift="0.4 * (datum.index + 1) - 1"
)

# Create the chart with shifted bars
chart = alt.layer(base, bars).transform_calculate(
    shift="datum.shift"  # Use the calculated field directly
)

# Display the chart in a web browser
display.serve(chart, open_browser=True)
