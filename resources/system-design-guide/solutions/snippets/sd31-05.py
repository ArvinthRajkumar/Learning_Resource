import re
SPAM_WORDS = {"winner": 2.0, "free": 1.0, "urgent": 1.5, "click here": 2.5, "unsubscribe": -0.5}
def spam_score(subject, body, spf_pass, dkim_pass, links):
    text = (subject + " " + body).lower()
    score = sum(w for word, w in SPAM_WORDS.items() if word in text)
    score += 0 if spf_pass else 2.0
    score += 0 if dkim_pass else 1.5
    score += 0.5 * max(0, links - 2)
    score += 1.0 if re.search(r"[A-Z]{6,}", subject) else 0.0
    return round(score, 1)
msgs = [("Team notes", "meeting at 3", True, True, 0), ("URGENT WINNER", "free prize click here now", False, False, 6)]
for s, b, spf, dkim, links in msgs:
    sc = spam_score(s, b, spf, dkim, links)
    print(f"{s!r}: score {sc} -> {'SPAM folder' if sc >= 5 else 'inbox'}")
