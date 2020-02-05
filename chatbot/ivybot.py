#-----------------------------------------------Importing libraries---------------------------------------------------
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle
#-----------------------------------------------Openning intents file--------------------------------------------------
with open("intents.json") as file:
    data = json.load(file)
#-----------------------------------------------Open the saved model---------------------------------------------------
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
#-----------------------------------------------Splitting the string into substring------------------------------------
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
        
        if intent["tag"] not in labels:
            labels.append(intent["tag"])
#-----------------------------------------------Defining roots of the words--------------------------------------------
    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]
#-----------------------------------------------Counting letters-------------------------------------------------------
    for x, doc in enumerate(docs_x):
        bag = []
    
        wrds = [stemmer.stem(w) for w in doc]
    
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
            
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
    
        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)
#-----------------------------------------------Saving the model-------------------------------------------------------
    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

#-----------------------------------------------Training the model---------------------------------------------------
tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
import os.path
from os import path

if path.exists("model.tflearn"):
    model.load("model.tflearn")
else:
	model.fit(training, output, n_epoch=300, batch_size=8, show_metric=True)
	model.save("model.tflearn")


#-----------------------------------------------Counting latters in a substring----------------------------------------
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    
    return numpy.array(bag)
    
#-----------------------------------------------Starting the model-----------------------------------------------------    
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        
        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
                
        print(random.choice(responses))
        
chat()
    
    

