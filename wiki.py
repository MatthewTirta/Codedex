import wikipedia

search_phrase = "Python (programming language)"

summary = wikipedia.summary(search_phrase, sentences=2)
print(summary)
