import pandas as pd
from io import BytesIO

sample_data = pd.DataFrame(
    {
        "Name": ["Mario"] * 8 + ["Giulia"] * 8,
        "Surname": ["Rossi"] * 8 + ["Bianchi"] * 8,
        "Age": ["35"] * 8 + ["28"] * 8,
        "ExamDate": [
            "15/11/2023", "03/09/2023", "10/05/2023", "22/01/2023", "05/07/2022", "15/03/2022", "20/06/2021", "05/12/2020",  # Lean phase for Mario Rossi
            "15/11/2023", "03/09/2023", "10/05/2023", "22/01/2023", "05/07/2022", "15/03/2022", "20/06/2021", "05/12/2020",  # Lean phase for Giulia Bianchi
        ],
        "Weight": [
            "75.5", "62.0", "73.2", "61.8", "74.0", "63.2", "68.0", "60.5",  # Overweight and Lean phases for Mario Rossi
            "62.0", "61.5", "60.8", "58.5", "61.2", "60.0", "58.0", "57.5",  # Lean phase for Giulia Bianchi
        ],
        "ICW%": [
            "60.5", "58.0", "59.8", "57.5", "61.0", "59.2", "58.5", "57.0",  # Overweight and Lean phases for Mario Rossi
            "58.0", "57.5", "56.8", "56.5", "57.2", "56.0", "54.0", "53.5",  # Lean phase for Giulia Bianchi
        ],
        "ECW%": [
            "39.5", "42.0", "41.2", "42.5", "39.0", "40.8", "41.5", "43.0",  # Overweight and Lean phases for Mario Rossi
            "42.0", "42.5", "43.2", "43.5", "42.8", "44.0", "46.0", "46.5",  # Lean phase for Giulia Bianchi
        ],
        "BMR": [
            "1700,22", "1.400,32", "1650,80", "1.380,45", "1720,15", "1.420,90", "1.480,15", "1.450,20",  # Overweight and Lean phases for Mario Rossi
            "1.400,32", "1.380,45", "1.360,80", "1.340,45", "1.380,20", "1.360,00", "1.340,00", "1.320,20",  # Lean phase for Giulia Bianchi
        ],
        "FM": [
            "22.3", "21.4", "23.4", "21.7", "21.1", "21.4", "21.8", "22.2",  # Overweight and Lean phases for Mario Rossi
            "21.0", "20.8", "20.5", "19.8", "20.5", "19.5", "18.5", "18.0",  # Lean phase for Giulia Bianchi
        ],
        "FFM": [
            "53.2", "40.6", "50.1", "40.1", "52.9", "41.8", "46.2", "38.3",  # Overweight and Lean phases for Mario Rossi
            "40.6", "41.7", "39.6", "41.0", "39.5", "41.0", "43.0", "44.5",  # Lean phase for Giulia Bianchi
        ],
        "FM%": [
            "29.8", "34.5", "32.0", "35.2", "28.5", "33.8", "31.8", "36.8",  # Overweight and Lean phases for Mario Rossi
            "34.5", "35.5", "34.5", "35.0", "34.5", "35.5", "36.5", "37.0",  # Lean phase for Giulia Bianchi
        ],
        "FFM%": [
            "70.2", "65.5", "68.0", "64.8", "71.5", "66.2", "68.2", "63.2",  # Overweight and Lean phases for Mario Rossi
            "65.5", "64.5", "65.5", "65.0", "65.5", "64.5", "63.5", "62.0",  # Lean phase for Giulia Bianchi
        ],
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
