def reverse_words(s):
    words = s.split()          # handles extra spaces
    return " ".join(reversed(words))
