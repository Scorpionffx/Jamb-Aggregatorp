import streamlit as st

st.set_page_config(page_title="JAMB Score Aggregator", page_icon="📚")

try:
    st.image("founder.jpg", width=150, caption="Founder: Taiwo David")
except:
    pass

st.title("📚 JAMB Score Aggregator")
st.write("Built by **Taiwo David - SSS2 Science** | Lagos")
st.write("---")

def suggest_courses(total):
    if total >= 300:
        return "🔥 Medicine, Law, Pharmacy, Aerospace Eng"
    elif total >= 270:
        return "⭐ Computer Science, Nursing, Electrical Eng, Architecture"
    elif total >= 240:
        return "👍 Biochemistry, Microbiology, Accounting"
    elif total >= 200:
        return "✅ Education, Business Admin, Polytechnics"
    else:
        return "💪 IJMB, Pre-degree, Polytechnic - You can still make it!"

name = st.text_input("Your Name")
eng = st.number_input("English", 0, 100, 70)
subj2 = st.number_input("Subject 2", 0, 100, 65)
subj3 = st.number_input("Subject 3", 0, 100, 65)
subj4 = st.number_input("Subject 4", 0, 100, 65)

if st.button("Calculate My Score 🚀"):
    total = eng + subj2 + subj3 + subj4
    st.balloons()
    st.success(f"{name}, your JAMB Total is {total} / 400")
    st.info(f"With {total}, you can get: {suggest_courses(total)}")

st.write("---")
st.subheader("💖 Support Developer")
st.code("PalmPay: 8028519092\nName: Shola Taiwo")
st.caption("© 2026 Taiwo David | SSS2 Science")
