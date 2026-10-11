import streamlit as st
st.set_page_config(page_title="JAMB Aggregator by Taiwo David", page_icon="📚")
st.title("📚 JAMB Score Aggregator")
st.caption("Built by Taiwo David - SSS2 Science | Lagos")
name = st.text_input("Your Name")
st.subheader("Enter Your 4 JAMB Scores")
col1, col2 = st.columns(2)
with col1:
    english = st.number_input("English", 0, 100, 70)
    subj2 = st.number_input("Subject 2", 0, 100, 65)
with col2:
    subj3 = st.number_input("Subject 3", 0, 100, 65)
    subj4 = st.number_input("Subject 4", 0, 100, 65)
SECRET_CODE = "TAIWO2026"
if st.button("Calculate My Score"):
    total = english + subj2 + subj3 + subj4
    st.success(f"{name}, your JAMB Total is {total}/400")
    st.divider()
    st.subheader("🔒 UNILAG Aggregate (Paid)")
    st.write("To see if UNILAG will give you admission:")
    st.info("Pay ₦500 to Palmpay: 8028519092\nName: Shola Taiwo\nThen WhatsApp me for unlock code")
    code = st.text_input("Enter Unlock Code:", type="password")
    if code == SECRET_CODE:
        st.balloons()
        olevel = st.slider("Your O'level Points (Best 5)", 0, 20, 12)
        jamb_points = total / 8
        aggregate = jamb_points + olevel
        st.metric("Your UNILAG Aggregate", f"{aggregate:.2f}/70")
        if aggregate >= 50:
            st.success("Safe for UNILAG!")
        else:
            st.warning("Consider less competitive course")
    elif code != "":
        st.error("Wrong code! Message Taiwo David")
