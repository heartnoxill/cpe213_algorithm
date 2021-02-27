# a word that contains inner ' will have "" instead of ''
#note: unable to split the hyphen contained words
# %%timeit
# %load_ext memory_profiler
import glob # for importing every txt files
import timeit
from collections import Counter # fastest tallying method

__author__ = 'P. Buathong (4012), P. S. Pranayanuntana (4030)'
# change the path to file here
path = '/content/drive/MyDrive/Computery/CPE213_Algorithm/Corpus-Flies/'

# For manually remove the possible remaining leftover SGMLs
tags_list = ['<p>' ,'</p>' , '<p*>','<ul>','</ul>','<li>','</li>','<br>',
        '<strong>','</strong>','<span*>','</span>','<a href*>','</a>',
        '<em>','</em>','<text>','</text>', '<header>', '</header>', '<body>',
         '</body>', '<slug>', '</slug>','< p>', '< header>','< headline>', 
         '<headline>']

line_list = ['\n','\p','\s','\r']

global wordList
    
def cleanWord(wordList):
  for i in range(len(wordList)):
      wordList[i].split('\n')

      # replace < with blank (remove SGML)
      if wordList[i].startswith("<"): 
          wordList[i] = ''
      # remove punctuation and number
      for char in '1234567890!"#$%&()*+,./:;=?@[]^_`{|}~-':
          wordList[i] = wordList[i].replace(char,' ').strip()
          
      # Trying to remove the hyphen burden
      # for charac in wordList[i]:
      #     if charac == '-':
      #         wordList[i].split('-')

      # Trying to remove the possible Non-breaking space
      wordList[i] = wordList[i].replace(r'\xa0', ' ')
      wordList[i] = wordList[i].replace('\\xa0', ' ')
      wordList[i] = wordList[i].replace('\xc2\xa0', ' ')
      wordList[i] = wordList[i].replace(u'&nbsp;', u' ')
      wordList[i].split()
    
      if wordList[i].startswith("'") or wordList[i].endswith("'"):
          wordList[i] = wordList[i].replace("'",'')
      if wordList[i].startswith("``"):
          wordList[i] = wordList[i].replace("``",'')
      wordList[i] = wordList[i].lower()

      # removing the leftover 'bugs'
      # or some line that didnt start with <, or leftover /n /p
      for tags in tags_list: 
          wordList[i] = wordList[i].replace(tags,' ')
          wordList[i].split()
      for line in line_list:
          wordList[i] = wordList[i].replace(line,' ')
          wordList[i].split()
      wordList[i].split(" ")

def readFile():
    global wordList
    wordList = []
    wordList_all = []
    # for j in range(100,101): # sample file 100.txt
    for j in range(501,523): # every files
        for files in glob.glob(path + str(j) +".txt"):
            inputText = open(files).read()
            wordList.append(inputText)
            wordList = inputText.split()
            # print(len(wordList))
            cleanWord(wordList)
            wordList_all.extend(wordList) # do not use append
    print("All Words: %d" % (len(wordList_all)))

    # Tally Part in Dict
    count_store = {}
    for word in wordList_all:
        if word == '': # eliminating the emptiness
            continue
        count_store[word] = count_store.get(word, 0) + 1

    # Tally Part in List (Using Counter())
    # temp_store = wordList_all # since wordList_all is a list
    # count_store = Counter(temp_store)
    
    word_num = []
    for key, val in count_store.items():
        word_num.append((val,key)) # val,key
    word_num.sort(reverse=True) # Sort using Tuple, sort from the highest number
    
    # Since colab only shows last 5000 row, so we gonna write the file
    # with open(path+'output.txt','w') as out: 
    #     out.write(str(word_num)) 

    for k in range(len(word_num)):
        word_dump = tuple(reversed(word_num[k])) # swap the position of val, key
        print("%s %s" % (word_dump)) # single tab

def main():
    readFile()

if __name__ == '__main__':
    main()
    
# %memit main()