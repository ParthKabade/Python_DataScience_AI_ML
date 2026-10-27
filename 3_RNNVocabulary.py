sentences=[
    "Food Was Good",
    "Food Was Bad",
    "Food Was Not Good"
]


vocabulary=[]

for sentence in sentences:
    words=sentence.split()

    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

for index,word in enumerate(vocabulary):
    print("position",index+1,":",word)