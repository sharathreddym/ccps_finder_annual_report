



from nltk import sent_tokenize, word_tokenize
import pandas as pd
import numpy as np
import nltk
import os
from nltk import ne_chunk


os.getcwd()
os.chdir('C:\\Users\\Sharath\\Desktop\\senttext')

df=open('ge.txt',encoding='utf8').read()

dt=sent_tokenize(df)

compraw=[]
peerraw=[]
custraw=[]
partraw=[]
suppraw=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in dt:
    if 'competitor' in i:
        if 'includ' in i:
            list1.append(i)
            compraw.append(nltk.pos_tag(word_tokenize(i)))
    if 'peer' in i:
        list2.append(i)
        peerraw.append(nltk.pos_tag(word_tokenize(i)))
    if 'customer' or 'client' in i:
        list3.append(i)
        custraw.append(nltk.pos_tag(word_tokenize(i)))
    if 'partner' in i:
        list4.append(i)
        partraw.append(nltk.pos_tag(word_tokenize(i)))
    if 'supplier' in i:
        list5.append(i)
        suppraw.append(nltk.pos_tag(word_tokenize(i)))
cmp=[j for i in compraw for j in i]
competitors=[i[0] for i in cmp if i[1]=='NNP']
peer=[j for i in peerraw for j in i]
peers=[i[0] for i in peer if i[1]=='NNP']
cust=[j for i in custraw for j in i]
customers=[i[0] for i in cust if i[1]=='NNP']
part=[j for i in partraw for j in i]
partners=[i[0] for i in part if i[1]=='NNP']
supp=[j for i in suppraw for j in i]
suppliers=[i[0] for i in supp if i[1]=='NNP']


len(list1)

from nltk.tokenize import PunktSentenceTokenizer


custtok=df

custom_sent_tokenizer = PunktSentenceTokenizer(custtok)

lst1=' '.join(list1)

tokenized = custom_sent_tokenizer.tokenize(lst1)

tokenized


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            print(namedEnt)
    except Exception as e:
        print(str(e))


process_content()

ner=[]
for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk_sents(tagged, binary=False)
            ner.append(namedEnt)


type(namedEnt)


from nltk.tree import Tree

dd=[]
for chunk in namedEnt:
    if type(chunk)==Tree:
        dd.append(" ".join([token for token, pos in chunk.leaves()]))


dd

named_entities = []
for t in namedEnt.subtrees():
    if t.label() == 'ORGANIZATION':
        named_entities.append(t)
        # named_entities.append(list(t))  # if you want to save a list of tagged words instead of a tree

print (named_entities)


ROOT = 'ROOT'
tree = namedEnt
def getNodes(parent):
    for node in parent:
        if type(node) is nltk.Tree:
            if node.label() == ROOT:
                print ("======== Sentence =========")
                print ("Sentence:", " ".join(node.leaves()))
            else:
                print ("Label:", node.label())
                print ("Leaves:", node.leaves())

            getNodes(node)
        else:
            print ("Word:", node)

getNodes(tree)

competitors


