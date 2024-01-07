import altair as alt 
from vega_datasets import data

source = data.cars()

brush = alt.selection_interval()

points = alt.Chart(source).mark_point().encode(
    x = 'HP',
    y = 'miles per Gallon',
    color = alt.condition(brush,'Origin', alt.value('lightgray'))
).add_params(
        brush
    )


bars = alt.Chart(source).mark_bar().encode(
    y = 'Origin',
    color ='Origin',
    x='count(Origin)'
).transform_filter(
    brush
)

#points & bars

display.serve(chart, open_browser=True)  # Display in a web browser
