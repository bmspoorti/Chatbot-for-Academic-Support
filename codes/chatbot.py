import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import nltk
import string
from nltk.stem import WordNetLemmatizer
import webbrowser
from threading import Timer

nltk.download('punkt')
nltk.download('wordnet')

# Load the dataset
data_path = 'Expanded_Academic_Support_Chatbot_Data_SRH.csv'
df = pd.read_csv(data_path)

# Data preprocessing
lemmatizer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greetings dictionary for basic interactions
greetings = {
    'hello': 'Hello! How can I assist you today?',
    'hi': 'Hi there! What would you like to know?',
    'hey': 'Hey! How can I help you today?'
}

def check_for_greeting(sentence):
    words = nltk.word_tokenize(sentence.lower())
    for word in words:
        if word in greetings:
            return greetings[word]
    return None

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Question'])

# IDash app layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("SRH Hochschule Heidelberg Chatbot", className="text-center mb-3", style={'color': 'white', 'backgroundColor': 'black', 'padding': '10px'}),
                    width=12)),
    dbc.Row(dbc.Col(html.Div("Ask me anything about the Applied Data Science and Analytics course.", className="text-center mb-3", style={'color': 'orange'}),
                    width=12)),
    dbc.Row([
        dbc.Col(dcc.Textarea(id='user-input', style={'width': '100%', 'height': '100px', 'margin-top': '20px', 'border': '2px solid orange', 'color': 'black'}),
                width=10),
        dbc.Col(dbc.Button('Submit', id='submit-val', n_clicks=0, className='btn btn-warning', style={'height': '100px', 'backgroundColor': 'orange', 'color': 'white', 'fontSize': '20px'}),
                width=2),
    ], justify="around"),
    dbc.Row(dbc.Col(html.Div(id='response', style={'color': 'white', 'backgroundColor': 'black', 'padding': '20px', 'border-radius': '5px', 'border': '2px solid orange', 'marginTop': '20px'}),
                    width=12))
], fluid=True, style={"max-width": "960px", 'padding': '20px', 'backgroundColor': 'white'})

# Callback function to update the chatbot response
@app.callback(
    Output('response', 'children'),
    Input('submit-val', 'n_clicks'),
    State('user-input', 'value')
)
def update_output(n_clicks, value):
    if not value:
        return "Please enter a question to get started."
    
    user_response = value.lower()
    greeting_response = check_for_greeting(user_response)
    if greeting_response:
        return f"ROBO: {greeting_response}"

    def response(user_response):
        robo_response = ''
        tfidf = vectorizer.transform([user_response])
        vals = cosine_similarity(tfidf, tfidf_matrix)
        idx = vals.argsort()[0][-1]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-1]
        
        if req_tfidf == 0:
            robo_response = "I am sorry! I do not understand you."
            return robo_response
        else:
            robo_response = df['Answer'].iloc[idx]
            return robo_response
    
    bot_response = response(user_response)
    return f"ROBO: {bot_response}"


def open_browser():
      webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)




