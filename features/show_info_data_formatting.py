import streamlit as st
import pandas as pd
from features import dataset_sample as ds

def display_data_formatting_info():
    ''' Displays information related to data formatting.
    This function creates and displays informational messages, sample tables for correct
    and wrong data formats as guidelines on how to format data properly.

    Returns:
        tuple: A tuple containing wrong_format, correct_format, and info_format. '''
    
    info_format = st.empty()
    with info_format.container():
        st.header("How to format your Data", divider="grey")
        if st.button("\u23EC **Download: Correctly formatted Dataset**"):
            # Download the sample dataset when the button is clicked
            csv_buffer = ds.download_sample_data()
            st.download_button(
                label="**Click to download**",
                data=csv_buffer,
                file_name="correct_sample_dataset.csv",
            )
        st.markdown(
            """ <span style="font-size: 20px;"> \u2757 _Your table headers need to be written the same way as shown in this example_ """,
            unsafe_allow_html=True,
        )

    correct_sample_df = pd.DataFrame(
        {
            "Name": ["Mario", "Giulia"],
            "Surname": ["Rossi", "Bianchi"],
            "Age": ["35", "28"],
            "ExamDate": ["15/11/2023", "03/09/2023"],
            "Weight": ["75.5", "62,0"],
            "FFM%": ["70.2", "65,5"],
            "FM%": ["29.8", "34,5"],
            "FM": ["22.3", "21.4"],
            "FFM": ["53.2", "40.6"],
            "ICW%": ["60.5", "58,0"],
            "ECW%": ["39.5", "42,0"],
            "BMR": ["1.700,22", "1400,32"],
        }
    )
    wrong_sample_df = pd.DataFrame(
        {
            "Name": ["Mario", "Giulia"],
            "Surname": ["Rossi", "Bianchi"],
            "Age": ["35y", "28y.o."],
            "ExamDate": ["15-11-2023", "2023/09/03"],
            "Weight": ["75.5lb", "62,0kg"],
            "FFM%": ["70.2%", "65,5%"],
            "FM%": ["29.8%", "34,5%"],
            "FM": ["22.3lb", "21.4kg"],
            "FFM": ["53.2lb", "40.6kg"],
            "ICW%": ["60.5%", "58,0%"],
            "ECW%": ["39.5%", "42,0%"],
            "BMR": ["1,700,22", "1,400.32"],
        }
    )

    # Display correct format information
    correct_format = st.empty()
    wrong_format = st.empty()

    with correct_format.container():
        st.subheader("Correct format", divider="green")
        st.table(
            correct_sample_df.style.set_table_styles(
                [
                    {
                        "selector": "th",  # Apply styling to table headers
                        "props": [
                            ("font-size", "150%"),  # Font size for th
                            ("font-weight", "bold"),  # Bold for th
                        ],
                    },
                    {
                        "selector": "td",  # Apply styling to table cells
                        "props": [
                            ("font-size", "120%"),  # Font size for td
                        ],
                    },
                ]
            )
        )

        st.markdown(
            """ <span style="font-size: 20px;">  \u2705 The Exam Date is formatted as **DD/MM/YYYY** <br> \u2705 **No symbols** have been used with the values <br> \u2705 BMR accepts values formatted **X.XXX,YY** or **XXXX,YY** or **XXXX.YY**</span>""",
            unsafe_allow_html=True,
        )

    # Display wrong format information
    with wrong_format.container():
        st.subheader("Wrong format", divider="red")
        st.table(
            wrong_sample_df.style.set_table_styles(
                [
                    {
                        "selector": "th",  # Apply styling to table headers
                        "props": [
                            ("font-size", "150%"),  # Font size for th
                            ("font-weight", "bold"),  # Bold for th
                        ],
                    },
                    {
                        "selector": "td",  # Apply styling to table cells
                        "props": [
                            ("font-size", "120%"),  # Font size for td
                        ],
                    },
                ]
            )
        )

        st.markdown(
            """ <span style="font-size: 20px;"> \u274C Don't format the Exam Date as **DD-MM-YYYY**, **MM/DD/YYYY**, or any other variation. <br> \u274C Don't use **%** or **kg/lb** or **y/y.o.** annotations <br> \u274C BMR doesn't accept values like **X,XXX.YY** or **X,XXX,YY** </span> """,
            unsafe_allow_html=True,
        )
    return wrong_format, correct_format, info_format
