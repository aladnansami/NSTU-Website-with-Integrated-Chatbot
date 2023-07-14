# IMPORT ALL REQUIRED PACKAGES
# LIBRARY FUNCTION
# INITIALIZING FILES & EMPTY LIST

# GETTING PATTERN FROM FILE & TOKENIZING
# STEMMING, LEMMATIZING, REMOVING DUPLICATES & STOP WORDS
# SORTING TOKEN & TAGS
# DISPLAYING PROGRESS - PRINTING WORDS(TOKEN), CLASSES(TAGS) AND DOCUMENTS(TOKEN WITH TAGS)
# GENERATING PKL FILES - SAVING SERIALIZED DATA

# CREATING OUR TRAINING DATA - INDEXING TOKEN
# RANDOMLY ORGANIZED DATA
# CREATING TEST DATA

# CREATING NEURAL MODEL
# KERAS MODEL
# COMPILE MODEL
# TRAINED MODEL
# SAVED MODEL


# IMPORT ALL REQUIRED PACKAGES
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from nltk.stem import WordNetLemmatizer
import nltk
import json
import pickle
import numpy as np
from keras.optimizers import SGD
import random

# LIBRARY FUNCTION
lemmatizer = WordNetLemmatizer()

# INITIALIZING FILES & EMPTY LIST
words = []
classes = []
documents = []
ignore_words = ['?', '!']
data_file=open('data.json', 'r', encoding='utf-8').read()
intents = json.loads(data_file)

# GETTING PATTERN FROM FILE & TOKENIZING
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # TOKENZIE EACH QUERY
        w = nltk.word_tokenize(pattern)

        # STORING ALL TOKEN(WORD) ONE BY ONE
        words.extend(w)

        # STORING TOKEN ALONG WITH EACH TOKEN
        documents.append((w, intent['tag']))

        # STORING UNIQUE TAG
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# STEMMING, LEMMATIZING, REMOVING DUPLICATES & STOP WORDS
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# DISPLAYING PROGRESS
print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

# SAVING SERIALIZED DATA
pickle.dump(words, open('texts.pkl', 'wb'))
pickle.dump(classes, open('labels.pkl', 'wb'))

# CREATING OUR TRAINING DATA - INDEXING TOKEN

# INITALLY THERE HAVE AN EMPTY DATA
training = []

# CREATING EMPTY ARRAY FOUR ALL TOKEN
output_empty = [0] * len(classes)

# TRAING SET BAG OF WORDS FOR EACH SENTENCE - INDEXING RELATED TAG WITH TOKENS
for doc in documents:
    # INITIALIZE OUR BAG OF WORDS - EMPTY ARRAY FOR TOKENS
    bag = []

    # LIST OF TOKENIZED WORS FOR THE PATTERN - LIST OF TOKEN/WORD FOR EACH TAG
    pattern_words = doc[0]

    # LEMMATIZE EACH WORD - CREATE BASE WORD, IN ATTEMPT TO PRESENT RELATED WORDS - BEFORE WE LEMMATIZE FOR WORDS(TOKEN), HERE LEMMATIZE FOR DOC[0](TOKEN) WHICH IS ALSO TOKEN
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

    # CREATE OUR BAG OF WORDS ARRAY WITH 1, IF WORD MATCH FOUND IN CURRENT PATTERN - INDEXING DEPEND ON RELATED TAG, TOKENS
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # OUTPUT IS '0' FOR EACH TAG, AND '1' FOR CURRENT TAG(FOR EACH PATTERN)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# RANDOMLY ORGANIZE TRAINING DATA & MAKING IT AS ARRAY(BEFORE IT WAS PYTHON LIST)
random.shuffle(training)
training = np.array(training)

# create train and test lists. X - patterns, Y - intents
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")

# CREATING NEURAL MODEL - 3 LAYERS
model = Sequential()

# FIRST LAYER - 128 NEURONS
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))

# SECOND LAYER - 64 NEURONS
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

# FINAL LAYER - NEURON NUMBER DEPEND ON TAG NUMBER
model.add(Dense(len(train_y[0]), activation='softmax'))

# KERAS MODEL
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

#COMPILING MODEL
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# TRAING/FITTING AND SAVING THE MODEL
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('model.h5', hist)

print("Model Created")