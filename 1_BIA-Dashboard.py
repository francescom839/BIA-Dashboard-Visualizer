import streamlit as st
import pandas as pd
import warnings
from io import StringIO
import os
import subprocess

# Custom modules
from features import show_info_data_formatting as show_info
from features import manipulate_dataframe as man_df
from features import bia_graphics as bia_g

st.label_visibility = "collapse"
warnings.filterwarnings("ignore")

st.set_page_config(page_title="BIA Dashboard", page_icon=":bar_chart", layout="wide")

st.title(" :bar_chart: BIA Visualizer Dashboard")
st.markdown(
    "<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True
)  # Using CSS to style the title

file = st.file_uploader(
    "", type=(["csv"])
)  # The user can upload their file with a widget


dashboard_info = st.info("To see the Dashboard, you need to upload a file", icon="ℹ️")
wrong_format, correct_format, info_format = show_info.display_data_formatting_info()


if file is not None:  # if you choose and upload a file, then run the script
    filename = file.name

    # Use StringIO to read the uploaded file from any directory
    content = file.getvalue().decode("utf-8")
    dataframe = pd.read_csv(StringIO(content), encoding="ISO-8859-1", sep=";")
    dashboard_info.empty()
    wrong_format.empty()
    correct_format.empty()
    info_format.empty()

    dataframe["ExamDate"] = pd.to_datetime(dataframe["ExamDate"], format="%d/%m/%Y")

    column1, column2 = st.columns((2))  # creating two columns

    startDate = pd.to_datetime(dataframe["ExamDate"]).min()  # getting the min exam Date
    endDate = pd.to_datetime(dataframe["ExamDate"]).max()  # getting the max exam Date

    with column1:
        date1 = pd.to_datetime(
            st.date_input("Start Date", startDate, format="DD/MM/YYYY")
        )

    with column2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate, format="DD/MM/YYYY"))

    dataframe = dataframe[
        (dataframe["ExamDate"] >= date1) & (dataframe["ExamDate"] <= date2)
    ].copy()  # Updating/Filtering the data depending on the beginning and ending data

    with st.sidebar:
        # Creating a filter option
        st.sidebar.header("Choose your filter: ")

        # Filter for surname
        surname = st.sidebar.multiselect(
            "Pick your surname", dataframe["Surname"].unique()
        )
        if not surname:  # what happens if there are no filters?
            dataframe2 = dataframe.copy()
        else:
            dataframe2 = dataframe[
                dataframe["Surname"].isin(surname)
            ]  # Creating a filtered version of the data

        # Filter for name
        name = st.sidebar.multiselect("Pick your name", dataframe2["Name"].unique())
        if not name:  # what happens if there are no filters?
            dataframe3 = dataframe.copy()
        else:
            dataframe3 = dataframe2[
                dataframe2["Name"].isin(name)
            ]  # Creating a filtered version of the data
        age = st.sidebar.multiselect("Pick your age", dataframe3["Age"].unique())

    (
        previous_record,
        most_recent_record,
        filtered_dataframe,
    ) = man_df.filter_and_format_dataframe(dataframe, dataframe3, name, surname, age)

    with column1:
        st.subheader("Body dynamics per Examdate")

        if name and surname:  # Check if both Name and Surname are selected
            if not filtered_dataframe.empty:
                # Create a bar chart
                bia_g.plot_barchart_weight_graph(filtered_dataframe)
                # Create a line graph
                bia_g.plot_linechart_weight_graph(filtered_dataframe)
            else:
                st.warning("No data available for the selected person.")
        else:
            st.warning("Please select both Name and Surname to display the bar-chart.")

    with column2:
        st.subheader(
            f"Body Composition for {most_recent_record['Name']} {most_recent_record['Surname']}"
        )

        if name and surname:
            if not filtered_dataframe.empty:
                # Create a pie chart
                bia_g.plot_piechart_fm_ffm_graph(most_recent_record)
                # Create a linechart
                bia_g.plot_linechart_icw_ecw_graph(filtered_dataframe)
            else:
                st.warning("No data available for the selected person.")

        else:
            st.warning("Please select both Name and Surname to display the pie-chart.")

    with st.expander(
        "\u26A1 Body Metabolism Rate (BMR)", expanded=True
    ):  # Show Gauge for BMR
        if name and surname:
            if not filtered_dataframe.empty:
                bia_g.plot_gauge_BMR_graph(most_recent_record, previous_record)
            else:
                st.warning("No data available for the selected person.")
        else:
            st.warning("Please select both Name and Surname to display the BMR gauge.")
else:
    st.stop()  # Stop the script if there is no file uploaded

if __name__ == "__main__":
    # Get the absolute path to the current script
    script_path = os.path.abspath(__file__)

    # Build the Streamlit run command to access the DashBoard
    streamlit_command = f"streamlit run {script_path} --server.port 8888"

    # Run the dashboard
    subprocess.run(streamlit_command, shell=True)