# To run: streamlit run stars.py

base="dark"
primaryColor="forestGreen"

primaryColor="darkGoldrod"

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
    st.session_state.p = 0

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
st.header("Bonuses")

with st.expander("Special Days"):
    col1, col2, col3 = st.columns(3)

    with col1:
        x2 = st.checkbox("Double Stars", key="x2")

    with col2:
        pp = st.checkbox("Perfect Pages", key="pp")

    with col3:
        p = st.number_input(
            "Perfect Pages",
            min_value=0,
            max_value=w+m,
            step=1,
            key="p",
            disabled=not pp
        )

with st.expander("Wheel Spins"):

    st.subheader("Stars")
    col1, col2, col3 = st.columns(3)

    with col1:
        w2 = st.number_input("2x White", min_value=0, step=1, key="w2")
    with col2:
        w3 = st.number_input("3x White", min_value=0, step=1, key="w3")
    with col3:
        ten = st.number_input("10 Stars", min_value=0, step=1, key="ten")

    w_coeff = max(1, 2*w2 + 3*w3)

    stars_base = w_coeff*w + 5*m + 2*a + 10*ten + d + p

    if x2:
        stars_base = 2 * stars_base

    st.subheader("Cards")
    col4, col5 = st.columns(2)

    with col4:
        free = st.number_input("Free Card", min_value=0, step=1, key="free")
    with col5:
        d4 = st.number_input("D4 for Cards (Put Rolled Number)", min_value=0, key="d4")

    cards_base = d4 + free



st.header("Earned")

level = st.radio(
    "Select Level",
    ["**Level 1**", ":red[**Level 2**]", ":gray[**Level 3**]", ":yellow[**Level 4**]"],
    horizontal=True,
    label_visibility="collapsed"
)

level_map = {
    "**Level 1**": 24,
    ":red[**Level 2**]": 18,
    ":gray[**Level 3**]": 15,
    ":yellow[**Level 4**]": 12
}

level_stars = level_map[level]

con_cards, con_stars = divmod(stars_base, level_stars)

col1, col2 = st.columns(2)
col1.metric("Stars", con_stars)
col2.metric("Cards", cards_base + con_cards)

