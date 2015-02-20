from wordnik import *

key='c17e17b7d601024c8450e09f0830206b9d12c91729fa15a2c'
url='http://api.wordnik.com/v4'
client = swagger.ApiClient(key, url)

words = WordsApi.WordsApi(client)
example = words.getWordOfTheDay()
string = 'The Word of the Day is ' + example.word +'.'
print string
string = 'Definition: '+example.definitions[0].text
print string
string = 'Date = '+example.publishDate.strftime("%D")
print string