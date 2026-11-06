from sentence_transformers import SentenceTransformer
from sentence_transformers import util

#load pretrained embedding model
model=SentenceTransformer("all-MiniLm-L6-v2")

#knowlge base
documents=[
    "Python is used for machine learning",
    "java is used for enterprice application",
    "SQL is used to manage Databases",
    "Html is used to create webpages",
    "TensorFlow is used for deep learning"
]

#generate doucument embedding 
document_embedding=model.encode(documents,convert_to_tensor=True)

#Accept question
query=input("Enter your question")

#generate doucument embedding 
query_embedding=model.encode(query,convert_to_tensor=True)

#calculate similarity
scores=util.cos_sim(query_embedding,document_embedding)[0]

#display scores
for index,score in enumerate(scores):
    print(documents[index]," : ",score.item())

#find the best document
best_index=score.argmax().item()

print(f"Most relevant document :{documents[best_index]}")