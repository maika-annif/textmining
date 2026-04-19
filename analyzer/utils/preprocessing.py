import nltk_setup
import nltk
import re
import nltk
import re

def tokenize_text_df(texte, lang='german'):
    tokenized_texte = [nltk.tokenize.word_tokenize(text, language=lang) for text in texte["Text"]]
    # Tokens dem DataFrame hinzufügen
    texte["Tokens"] = tokenized_texte
    return texte

def rauschen_entfernen_df(texte, length_threshold=1):
    pattern = r'^[a-zA-ZäöüÄÖÜß-]+$'
    # Bedingung: Matcht das Muster UND Länge ist größer als 1
    gefilterte_texte = [
        [word for word in tokens if re.match(pattern, word) and len(word) > length_threshold] 
        for tokens in texte["Tokens"]
    ]
    texte["Tokens"] = gefilterte_texte
    return texte

def remove_stopwords_df(texte, lang='german',my_stopwords=None):
    # Stoppwortliste laden
    stopwords = nltk.corpus.stopwords.words(lang)
    # Stopwortliste durch eigene Stoppwörter erweitern
    stopwords.extend(my_stopwords)
    # Stoppwörter aus den Tokens entfernen
    gefilterte_texte = [[word for word in tokens if word not in stopwords] for tokens in texte["Tokens"]]
    texte["Tokens"] = gefilterte_texte
    return texte

def add_ngrams_df(texte, n=2):
    # Wir nehmen die Token, verbinden sie mit Leerzeichen und packen das in eine Liste
    ngram_texte = [
        [" ".join(gram) for gram in nltk.ngrams(tokens, n)] 
        for tokens in texte["Tokens"]
    ]
    texte[f"{n}-grams"] = ngram_texte
    return texte