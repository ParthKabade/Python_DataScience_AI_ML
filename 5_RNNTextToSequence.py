from tensorflow.keras.preprocessing.text import Tokenizer

sentences=[
    "Food Was Good",
    "Food Was Bad",
    "Food Was Not Good"
]

tokenizer=Tokenizer()

tokenizer.fit_on_texts(sentences)

sequences=tokenizer.texts_to_sequences(sentences)

for sentance,sequence in zip(sentences,sequences):
    print("Sentence :",sentance)
    print("Sequence :",sequence)
    print("---------------------------")