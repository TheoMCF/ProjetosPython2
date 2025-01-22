import random
import sounddevice as sd
import soundfile as sf
import sys
import os

def play_sound(filename):
    data, samplerate = sf.read(filename)
    sd.play(data, samplerate)
    sd.wait()

def clear_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")  
    sys.stdout.flush()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

print('Lets go gambling \n')
play_sound('Caça_Níquel\lesgo gambling.mp3')


tentativa = 0
alternativas = ['win', 'lose']
peso_alternativas = [1, 100]


while True:
    
    resultado = random.choices(alternativas, weights=peso_alternativas, k=1)[0]

    if resultado == 'win':
        print("\n JACKPOT!! YIPIEEE \n")
        numeros = random.randint(1, 9)
        print(f"""    ┌───────────┐
    │  S L O T  │
    ├───────────┤ O
    │ {numeros} | {numeros} | {numeros} |_|
    ├───────────┤
    │           │
    │           │
    └───────────┘""")
        
        if tentativa == 1:
            print('\n Hakari ahh luck')
        
        elif tentativa <= 7:
            print(f'\n Congratulations, you won in {tentativa} tries')
        
        elif tentativa >= 8:
            print(f'\n You needed {tentativa} tries... Bro get some help')
        
        elif tentativa >= 10:
            print(f'\n You needed {tentativa} tries... Quit gambling.')
        play_sound("Caça_Níquel\jackpot.mp3")
        break
    
    else:
        numeros = random.sample(range(1, 10), 3)
        print(f"""    ┌───────────┐
    │  S L O T  │ 
    ├───────────┤ O
    │ {numeros[0]} | {numeros[1]} | {numeros[2]} |_|
    ├───────────┤
    │           │
    │           │
    └───────────┘""")
        play_sound("Caça_Níquel/aw dang it.mp3")
        clear_lines(8)
        peso_alternativas[0] = peso_alternativas[0] + 5
        tentativa += 1