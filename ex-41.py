# ex-41.py

# Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

print(count_dollar_signs('word'))  # 0   
