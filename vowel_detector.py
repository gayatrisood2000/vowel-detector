def vowel_detector(text, letter='aeiou'):
    counter = 0
    highlighted_text = ""

    for char in text:
        if char.lower() in letter:
            counter += 1
            highlighted_text += f"\033[1;31m{char}\033[0m"
        else:
            highlighted_text += char

    print('Number of vowels found: ', counter)
    print('Vowels found: ', highlighted_text)


while True:
    print('''
██╗   ██╗ ██████╗ ██╗    ██╗███████╗██╗                            
██║   ██║██╔═══██╗██║    ██║██╔════╝██║                            
██║   ██║██║   ██║██║ █╗ ██║█████╗  ██║                            
╚██╗ ██╔╝██║   ██║██║███╗██║██╔══╝  ██║                            
 ╚████╔╝ ╚██████╔╝╚███╔███╔╝███████╗███████╗                       
  ╚═══╝   ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝                       

██████╗ ███████╗████████╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║   ██║██████╔╝
██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    ''')
    user_input = input('Enter a word, phrase, or sentence or type "EXIT" to quit: ')
    if user_input.upper() == 'EXIT':
        print('Give it a try the next time you\'re here. Until then, toodles!')
        break
    else:
        vowel_detector(user_input)