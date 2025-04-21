# import streamlit as st  # type: ignore
# from pyquran import quran

# # Page config
# st.set_page_config(page_title="Holy Quran", layout="centered")
# st.title("📖 Holy Quran")

# # --- Surah & Ayah Selection ---
# st.subheader("🔍 Read by Surah & Ayah")

# # Surah List (1 to 114)
# surah_list = [f"Surah {i}" for i in range(1, 115)]
# selected_surah = st.selectbox("Select Surah", surah_list)
# selected_surah_number = surah_list.index(selected_surah) + 1

# # Get Ayahs from selected Surah
# ayahs = quran.get_sura(selected_surah_number)
# ayah_numbers = list(range(1, len(ayahs) + 1))
# selected_ayah = st.selectbox("Select Ayah", ayah_numbers)

# # Display Ayah
# if st.button("Display Ayah"):
#     st.markdown(f"**{selected_surah} - Ayah {selected_ayah}**")
#     st.markdown(f"### {ayahs[selected_ayah - 1]}")

import streamlit as st  # type: ignore
from pyquran import quran

# Page config
st.set_page_config(page_title="Holy Quran", layout="centered")
st.title("📖 Holy Quran")

# --- Surah & Ayah Selection ---
st.subheader("🔍 Read by Surah & Ayah")

# Generate Surah list with names
surah_list = [f"{i}. {quran.get_sura_name(i)}" for i in range(1, 115)]
selected_surah_display = st.selectbox("Select Surah", surah_list)

# Extract the surah number from the selected option
selected_surah_number = int(selected_surah_display.split(".")[0])

# Get Ayahs from selected Surah
ayahs = quran.get_sura(selected_surah_number)
ayah_numbers = list(range(1, len(ayahs) + 1))
selected_ayah = st.selectbox("Select Ayah", ayah_numbers)

# Display Ayah
if st.button("Display Ayah"):
    surah_name = quran.get_sura_name(selected_surah_number)
    st.markdown(f"**Surah {surah_name} - Ayah {selected_ayah}**")
    st.markdown(f"### {ayahs[selected_ayah - 1]}")
