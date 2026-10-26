gamma = 0.9
rewards = [1, 1, 1, 10]
G = sum(gamma ** t * r for t, r in enumerate(rewards))
print("discounted return: %.3f" % G)
print("same rewards with gamma=0.5: %.3f" % sum(0.5 ** t * r for t, r in enumerate(rewards)))
