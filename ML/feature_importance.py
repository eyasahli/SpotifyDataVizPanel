import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Viridis256


def plot_feature_importance(feature_importances):
    # Sort the feature importances for better visualization
    feature_importances = feature_importances.sort_values(ascending=True)

    # Create a Bokeh figure
    p = figure(
        y_range=list(feature_importances.index),
        height=600, width=1000,
        title="Catboost Feature Importance",
        toolbar_location=None, tools="",
        x_axis_label="Importance", y_axis_label="Features",
    )

    # Create a ColumnDataSource
    source = ColumnDataSource(data=dict(features=feature_importances.index, importance=feature_importances.values))

    # Add horizontal bars to the plot
    p.hbar(
        y='features', right='importance', height=0.8,
        source=source, line_color="white", fill_color=Viridis256[len(feature_importances)]
    )

    # Set visual properties
    p.title.text_font_size = '20pt'
    p.ygrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None

    # Customize tick labels
    p.yaxis.major_label_text_font_size = '12pt'
    p.xaxis.major_label_text_font_size = '12pt'

    # Remove axis spines
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.minor_tick_line_color = None

    # Add hover tool for additional information
    p.add_tools(
        HoverTool(
            tooltips=[("Feature", "@features"), ("Importance", "@importance")],
            mode='vline'
        )
    )

    # Return the Bokeh figure
    return p


