def reverse(word): #вводим функцию reverse
    punctuation_marks = '.,?-:;!"' #punctuation_marks хранит все знаки.
    word_rev = '' #word_rev присваиваем пустую строку
    res = '' #res присваиваем пустую строку
    for sym in word: #Для sym в слове выполняется следующее
        if sym not in punctuation_marks: #Если символ sym не принадлежит набору знаков, то
            word_rev += sym #sym добавляется к word_rev
        else: #Иначе
            word_rev = word_rev[::-1] #word_rev переворачивается и добавляется к переменной res с сохранением пунктуации
            res += word_rev + sym #переворачивает значение переменной word_rev
            word_rev = '' #word_rev переворачивается и добавляется к переменной res с сохранением знаков
    word_rev = word_rev[::-1] #Переменная "word_rev" сбрасывается в пустую строку
    res += word_rev #word_rev переворачивается и добавляется к переменной res
    return res #возвращение результата res
message = input('сообщение: ').split() #даем пользователю ввести сообщение, которое разделится на слова
reverse_mes = '' #reverse_mes присваиваем пустую строку
for word in message: #для каждого слова в сообщении
    reverse_mes += ' ' + reverse(word) #добавляем перевернутое слово в переменную reverse_mes
print('новое сообщение:', reverse_mes) #выводим reverse_mes