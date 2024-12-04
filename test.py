import json
import MorseDecorder

morseDecoder = MorseDecorder.MorseDecoder()
print("Mode:", morseDecoder.mode)
while True:

  code = input("Press Enter morse code: ")

  if code == "ChangeMode":
    morseDecoder.change_mode()
    print("Mode:", morseDecoder.mode)
  else:
    result = morseDecoder.decode_morse_to_str(code)
    if result==None:
      print("Not Found")
    else:
      print(result)
