import pandas as pd
from io import BytesIO

sample_data = pd.DataFrame(
    {
        "Name": ["Mario", "Giulia", "Mario", "Giulia", "Mario", "Giulia"],
        "Surname": ["Rossi", "Bianchi", "Rossi", "Bianchi", "Rossi", "Bianchi"],
        "Age": ["35", "28", "35", "28", "35", "28"],
        "ExamDate": [
            "15/11/2023",
            "03/09/2023",
            "10/05/2023",
            "22/01/2023",
            "05/07/2022",
            "15/03/2022",
        ],
        "Weight": ["75.5", "62.0", "73.2", "61.8", "74.0", "63.2"],
        "ICW%": ["60.5", "58.0", "59.8", "57.5", "61.0", "59.2"],
        "ECW%": ["39.5", "42.0", "41.2", "42.5", "39.0", "40.8"],
        "BMR": ["1700,22", "1.400,32", "1650,80", "1.380,45", "1720,15", "1.420,90"],
        "FM": ["22.3", "21.4", "23.4", "21.7", "21.1", "21.4"],
        "FFM": ["53.2", "40.6", "50.1", "40.1", "52.9", "41.8"],
        "FM%": ["29.8", "34.5", "32.0", "35.2", "28.5", "33.8"],
        "FFM%": ["70.2", "65.5", "68.0", "64.8", "71.5", "66.2"],
    }
)


# Function to create a downloadable link
def download_sample_data():
    # Convert the DataFrame to CSV format
    csv_data = sample_data.to_csv(index=False, sep=";")

    # Encode the CSV data as bytes
    csv_bytes = csv_data.encode()

    # Create a BytesIO object to handle the binary data
    csv_buffer = BytesIO(csv_bytes)

    # Return the BytesIO object
    return csv_buffer
