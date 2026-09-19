# Made by @mellowestmel on Discord
# Fisch MiguRod Counter Rebind

# NOTES:
# YOU MUST SET YOUR MIGUROD COUNTER-ATTACK KEYBIND TO CTRL IN THE FISCH SETTINGS FOR THIS TO WORK

# Setup
# make sure you have pynput and python installed.

# python install: https://www.python.org/downloads/
# pynput install, run in the terminal: pip install pynput

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
def ToggleCounterAttack(override = None):
    global IsPressed

    if override is None: override = not IsPressed
    if IsPressed == override: return

    IsPressed = override

    if IsPressed: KeyboardController.press(Keyboard.Key.ctrl)
    else: KeyboardController.release(Keyboard.Key.ctrl)


# Handles keyboard input.
def OnKeyboardPress(key):
    if isinstance(CounterAttackKeybind, Mouse.Button): return
    if key != CounterAttackKeybind: return
    ToggleCounterAttack(True)


def OnKeyboardRelease(key):
    if isinstance(CounterAttackKeybind, Mouse.Button): return
    if key != CounterAttackKeybind: return
    ToggleCounterAttack(False)


# Handles mouse input.
def OnMousePress(_, __, button, pressed):
    if not isinstance(CounterAttackKeybind, Mouse.Button): return
    if button != CounterAttackKeybind: return
    ToggleCounterAttack(pressed)


# Listens for keyboard and mouse input.
with Mouse.Listener(on_click = OnMousePress) as MouseListener:
    with Keyboard.Listener(
        on_press = OnKeyboardPress,
        on_release = OnKeyboardRelease
    ) as KeyboardListener:

        MouseListener.join(); KeyboardListener.join()
