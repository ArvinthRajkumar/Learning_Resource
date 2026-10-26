def count_vowels(s):
    vowels = set("aeiou")
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count
