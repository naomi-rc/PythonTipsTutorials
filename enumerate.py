# enumerate : function to loop over something and provide a counter
languages = ["java", "javascript", "typescript", "python", "csharp"]
for index, language in enumerate(languages):
    print(index, language)

print()

starting_index = 1
for index, language in enumerate(languages, starting_index):
    print(index, language)

print()

language_tuple = list(enumerate(languages, starting_index))
print(language_tuple)