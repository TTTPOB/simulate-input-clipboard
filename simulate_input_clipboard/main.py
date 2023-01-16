import pyautogui
import pyperclip
from time import sleep


def main():
    clip_string = pyperclip.paste()
    sleep(1)
    pyautogui.press([char for char in clip_string])


if __name__ == "__main__":
    main()
