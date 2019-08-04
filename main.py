# Import `requests`
import requests

# Import BeautifulSoup from bs4
from bs4 import BeautifulSoup

# Import RegexpTokenizer from nltk.tokenize
from nltk.tokenize import RegexpTokenizer

# Import nltk
import nltk


def plot_word_freq(url):
    """Takes a url (from Project Gutenberg) and plots a word frequency
    distribution"""
    
    # Make the request and check object type
    r = requests.get(url)
    
    # Extract HTML from Response object and print
    html = r.text
    
    # Create a BeautifulSoup object from the HTML
    #soup = BeautifulSoup(html, "html5lib")
    soup = BeautifulSoup(r.content, features="html")
    
    # Get the text out of the soup and print it
    text = soup.get_text()
    
    # Create tokenizer
    tokenizer = RegexpTokenizer('\w+')
    
    # Create tokens
    tokens = tokenizer.tokenize(text)
    
    # Initialize new list
    words = []
    # Loop through list tokens and make lower case
    for word in tokens:
        words.append(word.lower())
        
    # Get English stopwords and print some of them
    sw = nltk.corpus.stopwords.words('english')
    
    # Initialize new list
    words_ns = []
    # Add to words_ns all words that are in words but not in sw
    for word in words:
        if word not in sw:
            words_ns.append(word)
    
    # Create freq dist and plot
    freqdist1 = nltk.FreqDist(words_ns)
    freqdist1.plot(25)
    
    return ()
    
    
# Scrap url from Project Gutenberg and plot word frequency distributions
url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
plot_word_freq(url)