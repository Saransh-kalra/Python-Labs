def vertical(word):
    if(word[0]==''):
        print('')
    else:
        print(word[0])
        vertical(word[1:])

vertical("sun")
        
