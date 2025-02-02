words = list(map(str, input().split()))

def reverse(words):
    text = ""
    for word in reversed(words):
        text += word + ' '
    print(text)

reverse(words)