# zip : combine lists

languages = ["english", "french", "spanish", "mandarin", "german"]
countries = ["england", "france", "spain", "china", "germany"]
levels = ["C2", "C2", "B2", "A2", "B2"]

for x in zip(languages, countries, levels):
    print(x)

print()

for language, country, level in zip(languages, countries, levels):
    print(f"{language} is spoken in {country}. I speak {language} at a {level} level.")
    
print()
my_zip = list(zip(languages, countries, levels)) # associated elements
print(my_zip)

print()

print(list(zip(*my_zip))) #unzip => each list individually