from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['aarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print('------')
origin_favorite_languages = {'jen': 'python', 'aarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name, language in origin_favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
