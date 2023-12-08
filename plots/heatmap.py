import panel as pn
import holoviews as hv
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColorBar, LinearColorMapper, HoverTool, ColumnDataSource
def create_heatmap(data):
    # Select only numeric columns for the correlation matrix
        data = data.drop(columns=['Unnamed: 0'])
        numeric_data = data.select_dtypes(include=['number'])

        # Calculate the correlation matrix
        corr_matrix = numeric_data.corr()

        # Create a Bokeh figure
        p = figure(
            width=800,
            height=800,
            x_range=list(corr_matrix.columns),
            y_range=list(corr_matrix.columns),
            #title="Spotify Dataset Heatmap",
            toolbar_location=None,
            tools="hover",
        )

        # Create a color mapper for the heatmap
        mapper = LinearColorMapper(
            palette="Viridis256", low=-1, high=1  # Adjust the range to your data
        )

        # Create a list of values from both the upper and lower triangles
        values = []
        x = []
        y = []
        text_values = []

        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                values.append(corr_matrix.iloc[i, j])
                x.append(corr_matrix.columns[i])
                y.append(corr_matrix.columns[j])
                text_values.append(f"{corr_matrix.iloc[i, j]:.2f}")

        # Create a ColumnDataSource
        source = ColumnDataSource(data={"x": x, "y": y, "values": values, "text_values": text_values})

        # Create the heatmap rectangles
        p.rect(
            x="x",
            y="y",
            width=1,
            height=1,
            source=source,
            line_color="white",
            fill_color={"field": "values", "transform": mapper},
        )

        # Add tooltips to display correlation values
        hover = HoverTool()
        hover.tooltips = [("Correlation", "@values{0.2f}")]
        p.add_tools(hover)

        # Add text labels to the heatmap cells
        p.text(
            x="x",
            y="y",
            text="text_values",
            source=source,
            text_color="white",
            text_align="center",
            text_baseline="middle",
        )

        # Add a color bar
        color_bar = ColorBar(
            color_mapper=mapper,
            location=(0, 0),
            title="Correlation",
            title_standoff=12,
            title_text_font_size="12pt",
            major_label_text_font_size="10pt",
        )

        p.add_layout(color_bar, "right")
        app = pn.Column(
            f"# Spotify Dataset Heatmap",
            p,
            )
        return app