from flask import Flask
from flask import render_template
from flask import request

from math import log
import json
import re
import nltk

nltk.download('stopwords')

app = Flask(__name__)



label_count=[]
words_index_dict=dict()
tfidf=dict()

with open('mysite/label_count.json','r') as f_obj:
    label_count = json.load(f_obj)
with open('mysite/words_index_dict.json','r') as f_obj:
    words_index_dict = json.load(f_obj)
with open('mysite/tfidf.json','r') as f_obj:
    tfidf = json.load(f_obj)

# @app.route('/rate')
# def hello_world():
#     return 'Hello, World!'

@app.route('/predict')
def post_html():
    return render_template('post.html')

@app.route('/predict', methods = ['POST'])
def deal_request():
    review = request.form["review"]
    rating = predict(review)
    return render_template("post.html", result=rating)


def segmentation(str):
    words = re.sub('[^a-zA-Z]',' ', str).lower().split() # Remove non-alphabetic characters
    stop_words = (nltk.corpus.stopwords.words('english')) # Remove stopwords
    words =  [x for x in words if x not in stop_words]
    return words

def count_value(list):
    value_count=dict()
    for x in list:
        if x not in value_count:
            value_count[x]=0
        value_count[x]+=1
    return value_count

def predict(review):
    review = segmentation(review)
    probability = []
    words_in_review_set = set(review)
    words_counts = count_value(review)
    for label in range(11):
        prob = 0
        for word in words_in_review_set:
            if word not in words_index_dict:
                continue
            prob+=log(tfidf[str(label)][words_index_dict[word]]*words_counts[word]+1)
        prob *= (label_count[label]/label_count[-1])
        probability.append(prob)
    return probability.index(max(probability))



# if __name__ == '__main__':
#     # app.run(host, port, debug, options)
#     # Default：host=127.0.0.1, port=5000, debug=false
#     app.run()