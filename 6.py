s = "abcdeabc"
result = ''.join(dict.fromkeys(s))
print(result)