import nltk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NLTK_DATA_DIR = os.path.join("nltk_data")

if NLTK_DATA_DIR not in nltk.data.path:
    nltk.data.path.append(NLTK_DATA_DIR)