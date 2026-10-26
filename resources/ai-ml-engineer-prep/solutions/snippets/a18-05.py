import math
words = ["the", "animal", "was", "tired"]
scores = {"the": [1, 0, 0, 0], "animal": [0.2, 1, 0, 0], "was": [0, 0.8, 1, 0], "tired": [0, 2.0, 0.3, 1]}      # hand-made similarity scores for illustration
def softmax(z): e = [math.exp(v) for v in z]; s = sum(e); return [v / s for v in e]
w = softmax(scores["tired"])
print("when processing 'tired', attention weights over", words, "=", [round(v, 2) for v in w], "-> it listens most to 'animal'")
