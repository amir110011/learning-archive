from nltk import *
from nltk.corpus import stopwords # Import the stop word list
import re
import nltk.corpus

#print nltk.data.path[0]
nltk.data.path.append('C:\Users\mh\AppData\Roaming\nltk_data')

text = "Machine learning is the subfield of computer science Machine achine learning algorithms and their performance. although he wanted to kill him because of this guilt and he sent him to jail after sentence him with murderer. is a branch of theoretical computer science known as computational learning theory. Because training sets are finite and the future learning and data mining often employ the same methods and overlap significantly, but while machine learning focuses on prediction, based on known properties learned from the training data, data mining focuses Machine learning and statistics are closely related fields. According to Michael I. Jordan, the ideas of machine learning, from methodological principles to theoretical tools, have had a long pre-history in statistics that gives computers the ability to learn without being explicitly programmed (Arthur Samuel, 1959).[1] Evolved from the study of pattern recognition and computational learning theory in artificial intelligence Machine learning tasks are typically classified into three broad categories, depending on the nature of the learning signal or feedback available to a learning system. These are[15  Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars,machine practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, youll learn about some of Silicon Valleys best practices in innovation as it pertains to machine learning and AI. my machine is the best "
stemmer = stem.PorterStemmer()

letters_only = re.sub("[^a-zA-Z]"," ",text )  
lower_case = letters_only.lower()      
words = lower_case.split()   
#print words
print len(words)
#print stopwords.words("english")
words = [w for w in words if not w in stopwords.words("english")]
#print words
print len(words)
words = " ".join( words )
#print words
tokens = nltk.word_tokenize(words)

print tokens
text = nltk.Text(tokens)

print len(text)
vocabularyUsed = sorted(set(text))
print len(vocabularyUsed)
myWord = "machine"
print text.count(myWord)
print text.collocations()

print "--------------------"
print text.concordance(myWord)
print "--------------------"
myWord = "victim"
print text.similar(myWord)
print  "---------------"
vocab = text.vocab()

print vocab.items()



def normalize(s):
    words = tokenize.wordpunct_tokenize(s.lower().strip())
    return ' '.join([stemmer.stem(w) for w in words])

print str(normalize(words))
print edit_distance("rain", "shine")

 

