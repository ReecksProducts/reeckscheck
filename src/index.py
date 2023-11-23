import eel

if __name__ == '__main__':
    eel.init('web')
    eel.start('index.html', mode="chrome", size=(1000, 760), port=8080)
