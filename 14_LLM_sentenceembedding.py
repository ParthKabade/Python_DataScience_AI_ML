from sentence_transformers import SentenceTransformer
from sentence_transformers import util

#load pretrained embedding model
model=SentenceTransformer("all-MiniLm-L6-v2")

sentences1="Python is a programming language"
sentences2="i love to play cricket"

embedding1=model.encode(sentences1,convert_to_tensor=True)
embedding2=model.encode(sentences2,convert_to_tensor=True)

similarity=util.cos_sim(embedding1,embedding2)

print("sentences 1 :",sentences1)
print("sentences 2 :",sentences2)

print("cosin simalirity :")
print(similarity.item())