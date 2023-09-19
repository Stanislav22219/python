str = 'http://dl.dropbox.com/u/7334460/Magick_py/py_magick.pdf'
index = str.rfind('/')
file_name = str[index+1:]
print(file_name)
