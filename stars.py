# To run: streamlit run stars.py
import streamlit as st

st.title('Award Calculator')

if st.button("Reset All", type="primary", shortcut="Backspace"):
    st.session_state.w = 0
    st.session_state.m = 0
    st.session_state.a = 0
    st.session_state.d = 0
    st.session_state.w2 = 0
    st.session_state.w3 = 0
    st.session_state.ten = 0
    st.session_state.free = 0
    st.session_state.d4 = 0

st.header("Pages")
col1, col2, col3, col4 = st.columns(4)

with col1:
    w = st.number_input("White Pages", min_value=0, step=1, key="w")
with col2:
    m = st.number_input("Mastery Checks", min_value=0, step=1, key="m")
with col3:
    a = st.number_input("Assessment Pages", min_value=0, step=1, key="a")
with col4:
    d = st.number_input("Dice Roll", min_value=0, step=1, key="d")


# If there are spins...
st.header("Spins")
with st.expander("Wheel Bonuses"):

    st.subheader("Stars")
    col1, col2, col3 = st.columns(3)

    with col1:
        w2 = st.number_input("2x White", min_value=0, step=1, key="w2")
    with col2:
        w3 = st.number_input("3x White", min_value=0, step=1, key="w3")
    with col3:
        ten = st.number_input("10 Stars", min_value=0, step=1, key="ten")

    w_coeff = max(1, 2*w2 + 3*w3)

    stars_base = w_coeff*w + 5*m + 2*a + 10*ten + d

    st.subheader("Cards")
    col4, col5 = st.columns(2)

    with col4:
        free = st.number_input("Free Card", min_value=0, step=1, key="free")
    with col5:
        d4 = st.number_input("D4 for Cards (Put Rolled Number)", min_value=0, key="d4")

    cards_base = d4 + free

# Level selection
st.header("Level")
l1, l2, l3, l4 = st.columns(4)

level_stars = None
if l1.button("Level 1"):
    level_stars = 24
if l2.button("Level 2"):
    level_stars = 18
if l3.button("Level 3"):
    level_stars = 15
if l4.button("Level 4"):
    level_stars = 12

# Waits until level is selected to display awards
if level_stars is not None:
    con_cards, con_stars = divmod(stars_base, level_stars)

    st.header("Earned")

    col1, col2 = st.columns(2)
    col1.metric("Stars", con_stars)
    col2.metric("Cards", cards_base + con_cards)

