# Made by @mellowestmel on Discord
# Fisch MiguRod Counter Rebind v1.1.0

# NOTES:
# YOU MUST SET YOUR MIGUROD COUNTER-ATTACK KEYBIND TO CTRL IN THE FISCH SETTINGS FOR THIS TO WORK

# Setup
# Make sure you have pynput and python installed.

# python install: https://www.python.org/downloads/
# pynput install: run the following in terminal: pip install pynput

# Imports
from pynput import mouse as Mouse, keyboard as Keyboard

# Controllers
KeyboardController = Keyboard.Controller()

# Keybinds
# Both can be any mouse or keyboard button.

# Keyboard.KeyCode.from_char('1') <- normal keyboard keys
# Keyboard.Key.f1 <- function / big keys
# Mouse.Button.left <- mouse buttons

# Change this to whatever you prefer.
CounterAttackKeybind = Mouse.Button.x1

# State
IsPressed = False

# Controls the counter-attack state.
def ToggleCounterAttack():
    KeyboardController.tap(Keyboard.Key.ctrl)


# Handles keyboard input.
def OnKeyboardPress(key):
    if isinstance(CounterAttackKeybind, Mouse.Button): return
    if key != CounterAttackKeybind: return
    ToggleCounterAttack()

# Handles mouse input.
def OnMousePress(_, __, button, pressed):
    if not isinstance(CounterAttackKeybind, Mouse.Button): return
    if button != CounterAttackKeybind or not pressed: return
    ToggleCounterAttack()


# Listens for keyboard and mouse input.
with Mouse.Listener(on_click = OnMousePress) as MouseListener:
    with Keyboard.Listener(
        on_press = OnKeyboardPress
    ) as KeyboardListener:
        MouseListener.join(); KeyboardListener.join()
