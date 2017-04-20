import urllib

def read_text():
  fileloc = open("check_text.txt")
  filetxt = fileloc.read()
  fileloc.close()
  check_profanity(filetxt)

def check_profanity(text_to_check):
  connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
  output = connection.read()
  print(output)
  connection.close()

read_text()