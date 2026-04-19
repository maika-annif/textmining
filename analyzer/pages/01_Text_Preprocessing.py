import streamlit as st
import nltk_setup
from utils.file_handler import load_txt_file
from utils.preprocessing import tokenize_text_df, rauschen_entfernen_df, remove_stopwords_df, add_ngrams_df
import nltk_setup
import pandas as pd
import numpy as np
import os
import nltk
import re 

st.set_page_config(page_title="Text Mining App", layout="wide")
# Logo einfügen
st.image("assets/logo.png", width=200)
st.title("Text Mining App - Text Processing")

texte = load_txt_file()

if(texte is None):
    st.warning("Keine Textdateien hochgeladen.")
else:
    st.subheader("Rohdaten")
    st.dataframe(texte)
    # ----------------------------------------------------------------------------
    # Textverarbeitung: Tokenisierung
    # ----------------------------------------------------------------------------
    texte = tokenize_text_df(texte)
    st.subheader("Texte in Tokens zerlegen")
    st.text(f"Tokenisierung: Die Texte werden in einzelne Wörter oder Tokens zerlegt. Summe aller Tokens: {sum(len(tokens) for tokens in texte['Tokens'])} ")
    st.dataframe(texte[["Titel", "Tokens"]])
    # ----------------------------------------------------------------------------
    # Rauschen entfernen: Sonderzeichen, Zahlen, etc.
    # ----------------------------------------------------------------------------
    texte = rauschen_entfernen_df(texte, length_threshold=1) 
    # length_threshold ist optional: Minimallänge der Tokens angeben, um sehr kurze Tokens zu entfernen
    st.subheader("Rauschen entfernen: Sonderzeichen, Zahlen, etc.")
    st.text("Summe aller Tokens nach Rauschentfernung: " + str(sum(len(tokens) for tokens in texte['Tokens'])))
    st.dataframe(texte[["Titel", "Tokens"]])
    # ---------------------------------------------------------------------------
    # Normalisieren (Wörter in Kleinbuchstaben) und Stoppwörter entfernen
    # ----------------------------------------------------------------------------
    my_stopwords = [] # optional: eigene Stoppwörter hinzufügen
    texte = remove_stopwords_df(texte, lang='german', my_stopwords=my_stopwords)
    st.subheader("Normalisieren und Stoppwörter entfernen")
    st.text(f"Tokens nach Stoppwortentfernung: {sum(len(tokens) for tokens in texte['Tokens'])}")
    st.dataframe(texte[["Titel", "Tokens"]])
    # ---------------------------------------------------------------------------
    # N-Gramme hinzufügen
    # ---------------------------------------------------------------------------
    n = 2
    texte = add_ngrams_df(texte, n)
    st.subheader("N-Gramme hinzufügen")
    st.dataframe(texte[["Titel", "Tokens", f"{n}-grams"]])