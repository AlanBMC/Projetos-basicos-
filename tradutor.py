from deep_translator import GoogleTranslator, MicrosoftTranslator
import pyttsx3
import speech_recognition as sr


def pt_p_en():
    texto = texto_traduzido()
    tradutor = GoogleTranslator(source="en", target="pt")
    traducao = tradutor.translate(texto)
    print(traducao)


def en_p_pt():
    texto = texto_p_en()
    tradutor = GoogleTranslator(source="pt", target="en")
    traducao = tradutor.translate(texto)
    print(traducao)


def fala_texto_pt():
    print('digite o texto a ser falado')
    texto1 = input()
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voices', voices[0].id)
    print(voices[0])
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate-65)

    speaker.say(texto1)
    speaker.runAndWait()


def fala_texto_en():
    print('digite o texto a ser falado')
    texto1 = input()
    speaker2 = pyttsx3.init()
    voices2 = speaker2.getProperty('voices')
    speaker2.setProperty('voices', voices2[1].id)
    rate2 = speaker2.getProperty('rate')
    speaker2.setProperty('rate', rate2-85)

    speaker2.say(texto1)
    speaker2.runAndWait()


def texto_traduzido():
    print('digite o texto em ingles')
    texto = input()
    return texto

def texto_p_en():
    print('digite o texto em portugues\n')
    texto = input()
    return texto


def voz_p_texto_pt():
    microfone = sr.Recognizer()
    with  sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('fale agora')
        audio = microfone.listen(source, timeout=10, phrase_time_limit=5)
    try:
        frase = microfone.recognize_google(audio, language="pt-BR")
        print('voce disse:' + frase)
    except sr.UnknownValueError:
        print('nao entendi')

def voz_p_texto_en():
    microfone = sr.Recognizer()
    with  sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('fale agora')
        audio = microfone.listen(source, timeout=10, phrase_time_limit=5)
    try:
        frase = microfone.recognize_google(audio, language="en-US")
        print('voce disse:' + frase)
    except sr.UnknownValueError:
        print('nao entendi')


def main():
    print('Qual opcao ?')
    aaa = True
    while  aaa:
        print('1 - traduzir para ingles\n')
        print('2 - traduzir para portugues\n ')
        print('3 - fala em ingles\n')
        print('4 - fala em portugues\n')
        print('5 - ouvir em portugues\n')
        print('6 - ouvir em ingles\n')

        print('0 - para sair')
        escolha = int(input())
        if escolha == 1:
            pt_p_en()
        elif escolha == 2:
            en_p_pt()
        elif escolha == 3:
            fala_texto_en()
        elif escolha == 4:
            fala_texto_pt()
        elif escolha == 5:
            voz_p_texto_pt()
        elif escolha == 6:
            voz_p_texto_en()
        elif escolha == 0:
            aaa = False
        else:
            aaa = False

main()