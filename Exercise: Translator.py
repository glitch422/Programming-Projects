from translate import Translator

translator = Translator(to_lang="ja")
file = input('Insert a path to a file:\n')
try:
  with open(file, 'r') as my_file:
    text = (my_file.read())
    translation = translator.translate(text)
    with open(file, mode='w') as my_file2:
      my_file2.write(translation)
except FileNotFoundError as e:
  print('File not found')
