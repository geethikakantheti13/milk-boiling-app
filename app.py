import streamlit as st
import time

st.set_page_config(page_title="Milk Boiling Simulator", page_icon="🥛", layout="centered")

# Title Section
st.markdown("<h1 style='color: #8B0000;'>🥛 Milk Boiling Simulator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #006400;'>Boil milk safely – virtually!</h3>", unsafe_allow_html=True)

# 🎨 Colored Tip Box
st.markdown(
    """
    <div style='background-color: #FFF3CD; padding: 15px; border-radius: 10px; border: 1px solid #FFEEBA;'>
        <h4 style='color: #856404;'>💡 Tip:</h4>
        <p style='color: #856404;'>Always watch the milk while boiling. It might overflow anytime! 🥛💥</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Mode selection
mode = st.radio("Choose boiling method", ["⏲️ Time-Based", "🌡‍🌫️️ Temperature-Based"])

# TIME MODE
if mode.startswith("⏲️"):
    boil_time = st.slider("Set boil duration (seconds)", 5, 30, 10)

    if st.button("🔥 Start Boiling"):
        with st.spinner("Heating up the milk..."):
            for i in range(boil_time):
                st.markdown(f"🕒 Boiling... **{i + 1} seconds**")
                time.sleep(1)
        st.success("🤭 Milk is boiled! Quickly turn off the stove👽!")

# TEMPERATURE MODE
else:
    temp = st.slider("Current milk temperature 😁(°C)", 20, 120, 30)

    if temp < 80:
        st.warning("Still cold 🥶🧊- Keep heating😐!")
    elif 80 <= temp < 99:
        st.info("Getting hot🌡 ! Almost there😎...")
    else:
        st.success("NO WAY 😱, MILK gonna spill😭")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>geethika-kantheti's version 🙂‍↔ in Streamlit</p>", unsafe_allow_html=True)
