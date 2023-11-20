import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from datetime import timedelta


def plot_barchart_weight_graph(data):
    """
    Plot a bar chart showing the body weight dynamics over different exam dates for each individual.

    Parameters:
    - data: DataFrame containing the necessary columns (ExamDate, Name, Weight).

    Returns:
    None
    """
    # Use the "ExamDate" as the x-axis and group by "ExamDate" and "Name" to display bars side by side
    fig = px.bar(
        data,
        x="ExamDate",
        y="Weight",
        color="Name",
        template="seaborn",
        title="Barchart Weight - Exam Date",
        range_y=[
            data["Weight"].min() // 1.01,  # devide by 1.01 to show the last bar's value
            data["Weight"].max(),
        ],
    )

    fig.update_layout(barmode="group")  # Display bars side by side
    st.plotly_chart(fig, use_container_width=True, height=400)


def plot_linechart_weight_graph(data):
    """
    Plot a line chart illustrating the body weight trends over time for each individual.

    Parameters:
    - data: DataFrame containing the necessary columns (ExamDate, Name, Weight).

    Returns:
    None
    """
    line_fig = px.line(
        data,
        x="ExamDate",
        y="Weight",
        color="Name",
        template="seaborn",
        text="Weight",
        title="Body weight per Examdate Dynamics",
        range_y=[
            data["Weight"].min() // 1.02,  # devide by 1.01 to show the last bar's value
            data["Weight"].max()
            // 0.98,  # devide by 0.98 to show the first bar's value
        ],
    )
    line_fig.update_layout(legend=dict(orientation="h"))  # Show the legend horizontally
    line_fig.update_traces(
        line=dict(dash="dot"), textposition="top right"
    )  # Set the line style to dashed

    st.plotly_chart(line_fig, use_container_width=True, height=400)


def plot_piechart_fm_ffm_graph(most_recent_record):
    """
    Plot a pie chart representing the ratio of Fat Mass (FM%) and Fat-Free Mass (FFM%) for the most recent BIA exam.

    Parameters:
    - most_recent_record: DataFrame row containing the data for the most recent BIA exam.

    Returns:
    None
    """
    # Format the date as "DD-MM-YYYY"
    registration_date = most_recent_record["ExamDate"].strftime("%d-%m-%Y")

    # Create a DataFrame for the pie chart
    pie_df = pd.DataFrame(
        {
            "Category": ["Fat Mass (FM%)", "Fat-Free Mass (FFM%)"],
            "Percentage": [
                most_recent_record["FM%"],
                most_recent_record["FFM%"],
            ],
            "Exam Date": [registration_date] * 2,
        }
    )

    fig = px.pie(
        data_frame=pie_df,
        names="Category",
        values="Percentage",
        hole=0.5,
        title=f"Fat Mass % and Fat Free Mass % ratio (Most Recent)",
        hover_data=["Exam Date"],
    )

    st.plotly_chart(fig, use_container_width=True)
    values_df = pd.DataFrame(
        {
            "Mass Type": ["Fat Mass (FM)", "Fat-Free Mass (FFM)"],
            "Value (kg/lb)": [
                most_recent_record["FM"],
                most_recent_record["FFM"],
            ],
        }
    )
    st.table(values_df)


def plot_linechart_icw_ecw_graph(data):
    """
    Plot a line chart depicting the changes in Intra-Cellular-Weight (ICW%) and Extra-Cellular-Weight (ECW%) over time.

    Parameters:
    - data: DataFrame containing the necessary columns (ExamDate, ICW%, ECW%).

    Returns:
    None
    """
    # Create a long-format DataFrame for ICW and ECW data
    icw_ecw_data = pd.melt(
        data,
        id_vars=["ExamDate"],
        value_vars=["ICW%", "ECW%"],
        var_name="CellularWeight",
        value_name="Value",
    )

    # Create a line chart for ICW and ECW
    line_chart = px.line(
        icw_ecw_data,
        x="ExamDate",
        y="Value",
        color="CellularWeight",
        template="seaborn",
        title="Intra-Cellular-Weight (ICW) and Extra-Cellular-Weight (ECW) Over Time",
        markers=True,
    )

    # Set the x-axis range to cover the entire date range
    line_chart.update_xaxes(
        range=[
            min(data["ExamDate"]) - timedelta(days=14),
            max(data["ExamDate"]) + timedelta(days=14),
        ]
    )  # timedelta used to completly show the linegraph

    st.plotly_chart(line_chart, use_container_width=True, height=400)


def plot_gauge_BMR_graph(most_recent_record, previous_record):
    """
    Plot a gauge chart displaying the Body Mass Index (BMR) for the most recent BIA exam, including a delta
    indicating the change from the previous BMR value.

    Parameters:
    - most_recent_record: DataFrame row containing the data for the most recent BIA exam.
    - previous_record: DataFrame row containing the data for the previous BIA exam.

    Returns:
    None
    """
    fig = go.Figure(
        go.Indicator(
            domain={"x": [0, 1], "y": [0, 1]},
            value=most_recent_record["BMR"],
            mode="gauge+number+delta",
            title={
                "text": f"Current BMR for {most_recent_record['Name']} {most_recent_record['Surname']}"
            },
            delta={"reference": previous_record["BMR"]},
            gauge={
                "axis": {"range": [None, 3000]},
                "steps": [{"range": [0, 3000], "color": "lightgray"}],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": previous_record["BMR"],
                },
            },
        )
    )
    st.markdown(
        """ <span style="font-size: 18px;"> \U0001F7E9 _Most recent BMR value_ <br> \U0001F7E5 _Previous BMR value, if existing_ <br> \u25B2 _BMR has increased from previous exam_ <br> \u25BC _BMR has decreased from previous exam_""",
        unsafe_allow_html=True,
    )
    st.plotly_chart(fig)
