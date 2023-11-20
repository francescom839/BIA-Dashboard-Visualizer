import pandas as pd


def filter_and_format_dataframe(dataframe, dataframe3, name, surname, age):
    """
    Filters and formats a DataFrame based on user-selected filters and performs additional data processing.

    Parameters:
    - dataframe (pd.DataFrame): The original DataFrame containing the data.
    - dataframe3 (pd.DataFrame): The filtered version of the original DataFrame.
    - name (list): List of selected names for filtering.
    - surname (list): List of selected surnames for filtering.
    - age (list): List of selected ages for filtering.

    Returns:
    - Tuple[pd.Series, pd.Series, pd.DataFrame]: A tuple containing the most_recent_record, the previous_record,
      and the filtered_dataframe.

    Notes:
    - If no filters are selected (empty name, surname, and age lists), the function returns the original DataFrame.
    - The function handles various combinations of filtering based on name, surname, and age.
    - Additional data processing includes converting columns to appropriate data types and extracting most recent and
      previous records based on the "ExamDate" column.
    """
    if not name and not surname and not age:
        filtered_dataframe = dataframe
    elif not surname and not age:
        filtered_dataframe = dataframe[dataframe["Name"].isin(name)]
    elif not name and not age:
        filtered_dataframe = dataframe[dataframe["Surname"].isin(surname)]
    elif surname and age:
        filtered_dataframe = dataframe3[
            dataframe["Surname"].isin(surname) & dataframe3["Age"].isin(age)
        ]
    elif name and age:
        filtered_dataframe = dataframe3[
            dataframe["Name"].isin(name) & dataframe3["Age"].isin(age)
        ]
    elif surname and name:
        filtered_dataframe = dataframe3[
            dataframe["Surname"].isin(surname) & dataframe3["Name"].isin(name)
        ]
    elif age:
        filtered_dataframe = dataframe3[dataframe["Age"].isin(age)]
    else:
        filtered_dataframe = dataframe3[
            dataframe3["Surname"].isin(surname)
            & dataframe3["Name"].isin(name)
            & dataframe3["Age"].isin(age)
        ]
    
    # Converting all the values into strings for manipulation purposes
    filtered_dataframe = filtered_dataframe.astype(str)

    # First, ensure that the "ExamDate" column is of datetime data type
    filtered_dataframe["ExamDate"] = pd.to_datetime(
        filtered_dataframe["ExamDate"], dayfirst=True, errors="coerce", format="ISO8601"
    )
    # Formatting the data
    data_to_convert = ["Weight", "FFM%", "FM%", "ICW%", "ECW%", "FFM", "FM"]
    for data in data_to_convert:
        filtered_dataframe[data] = (
            filtered_dataframe[data].str.replace(",", ".").astype(float)
        )
    filtered_dataframe["BMR"] = (
    filtered_dataframe["BMR"]
    .str.replace(".", "")
    .str.replace(",", ".", regex=False)
    .astype(float)
)


    # Get the most recent record based on the "ExamDate" column
    most_recent_record = filtered_dataframe.sort_values(
        by="ExamDate", ascending=False
    ).iloc[0]

    if (
        len(filtered_dataframe["ExamDate"].unique()) > 1
    ):  # in case there is just one BIA exam done, so no previous values are available
        previous_record = filtered_dataframe.sort_values(
            by="ExamDate", ascending=False
        ).iloc[1]
    else:
        previous_record = most_recent_record

    return previous_record, most_recent_record, filtered_dataframe
