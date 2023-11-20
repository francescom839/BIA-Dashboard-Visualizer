import streamlit as st
# Costum modules
from features import show_info_data_formatting as show_info

st.label_visibility = "auto"
st.set_page_config(page_title="User Guide", page_icon="\U0001F4DA", layout="wide")
st.title("\U0001F4DA User Guide")
st.markdown(
    "<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True
)  # Using CSS to style the title

st.header("Project Description", divider="grey")
st.markdown(
    """ <span style="font-size: 22px;"> \U0001F31F This project, **BIA Dashboard Visualizer**, is designed for small groups of individuals interested 
    in monitoring their body health in a clear and visually appealing manner.
      Keeping track of your body's status is crucial for overall well-being.
      <br>Consult with your doctor for a **Bioelectric Impedance Analysis**, 
      upload the results as a **.CSV** file and gain insights into your health status!
      <br><br>
      \U0001F41E Found a bug? Contact me [francescom839@gmail.com](mailto:francescom839@gmail.com)
      """,
    unsafe_allow_html=True,
)

wrong_format, correct_format, info_format = show_info.display_data_formatting_info()

# Rest of your code
