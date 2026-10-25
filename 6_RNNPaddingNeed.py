from tensorflow.keras.preprocessing.text import Tokenizer

sequences = [
    [1,2,3],
    [1,2,4],
    [1,2,5,3]
]

print("Original Sequences in ")

for sequence in sequences:
    print(sequence,"Length:",len(sequence))

print("All Sequences are of Different Lengths")
