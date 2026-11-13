from sentence_transformers import SentenceTransformer

#load pretrained embedding model
model=SentenceTransformer("all-MiniLm-L6-v2")

sentences=[
    "Python is a programming language",
    "Python is used for data science",
    "I support indian cricket team"
]

embedding=model.encode(sentences)

#display sentence embeddings
for index,embedding in enumerate(embedding):
    print("-"*40)
    print("\nSentences :",sentences[index])

    print("Embedding :\n",embedding)

    print("Total dimetion :",len(embedding))

