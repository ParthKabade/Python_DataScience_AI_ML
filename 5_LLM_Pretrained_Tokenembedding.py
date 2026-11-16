import torch
from transformers import AutoTokenizer 
from transformers import AutoModelForCausalLM

#prtrained model name
model_name="distilgpt2"

#loadtokensizer
tokenizer=AutoTokenizer.from_pretrained(model_name)

#load pretrained language model
model=AutoModelForCausalLM.from_pretrained(model_name)

#input prompt 
prompt="I love"

#Convert input into token ids
inputs=tokenizer(
    prompt,
    return_tensor="pt"
)

#Enabel evaluation mode
model.eval()

#perform inference without gradient calculations
with torch.no_grad():
    output=model(**inputs)

#Extract logits for final input position
logits=outputs.logits[0,-1,:]

#coverts logits into probablities
probabilites=torch.softmax(
    logits,
    dim=1
)

#select five highest probailites token
values,indices=torch.topk(
    probabilites,
    5
)

print("Input :",prompt)

for value,index in zip(values,indices):
    token=tokenizer.decode([index.item()])
    print(repr(token),round(values.item(),4))