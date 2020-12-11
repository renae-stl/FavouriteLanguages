#Usisng dictionaries
favourite_languages = {
    'jen': 'french',
    'pete':'spanish',
    'greg': 'C++',
    'sue': 'javascript',
}
while True:
    for name, language in favourite_languages.items():
        print(name.title() + "'s favourite language is " + language.title() + '\n' )

    user = input('what is your name? (to quit type q) ')
    
    if user == 'q':
        print('quit')
        break
    else:
        fave_language = input('what is your favourite language? ')
        print ('\nadding you to the dictionary...\n')

    favourite_languages[user] = fave_language

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + '\n')
