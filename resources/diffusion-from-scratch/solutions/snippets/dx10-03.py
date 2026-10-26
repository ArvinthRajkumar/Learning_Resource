import re
captions = ["IMG_2031.jpg", "buy now cheap!!!", "A red bicycle leaning against a brick wall in soft morning light, shallow depth of field", "dog", "Photo of a golden retriever puppy playing with a blue ball on green grass"]
def caption_quality(c):
    words = re.findall(r"[A-Za-z]+", c); issues = []
    if len(words) < 4: issues.append("too short")
    if re.search(r"\.(jpg|png)$|img_\d+", c, re.I): issues.append("filename")
    if re.search(r"buy|cheap|click|sale", c, re.I): issues.append("spam words")
    return issues
for c in captions: print(f"{c[:56]:<58}-> {'OK' if not caption_quality(c) else caption_quality(c)}")
