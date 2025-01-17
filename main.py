from playsound import playsound
import time

translate_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-', " ": "/"}

message = "Lucas"
message = " ".join(translate_dict[c] for c in message.upper())


def play_morse_code(message):
    for c in message:
        if c == ".":
            playsound("Censor beep sound effect.mp3")
            time.sleep(0.3)
        elif c == "-":
            playsound("censor-beep-1sec-8112.mp3")
            time.sleep(0.3)
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("Invalid character detected!")


print(message)
play_morse_code(message)

reverse_dict = {v: k for k, v in translate_dict.items()}
reverse_message = "".join(reverse_dict[c] for c in message.split(" "))
print(reverse_message)

