# coding: utf-8

import streamlit as st


def display_messages():
    messages = ["Première ligne", "Deuxième ligne",
                "Affichage à l'écran"]
    for m in messages:
        st.write(m)

if __name__ == "__main__":
    display_messages()