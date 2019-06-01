# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     server
   Description :
   Author :       StephenLau
   date：          2019/6/1
-------------------------------------------------
   Change Activity:
                   2019/6/1:
-------------------------------------------------
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
from socket import *
from time import ctime

def predict(message):
    NB_spam_model = open('./model/NB_spam_model.pkl','rb')
    clf = joblib.load(NB_spam_model)
    data = [message]
    df = pd.read_csv("spam.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    # Features and Labels
    X = df['message']
    cv = CountVectorizer()
    X = cv.fit_transform(X)  # Fit the Data
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)
    return my_prediction

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

print('waiting for connection...')
tcpClientSock, addr = tcpServSock.accept()
print('...connected from: ', addr)

while True:
    data = str(tcpClientSock.recv(BUFSIZ), encoding='utf-8')
    if not data:
        break
    print('服务器收到：', data)
    recv_string = tcpClientSock.send(bytes('[%s]%s' % (ctime(), predict(data)), 'utf-8'))
    print('服务器返回：', recv_string)

tcpClientSock.close()
tcpServSock.close()

