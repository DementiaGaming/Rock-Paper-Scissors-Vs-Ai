# Requirements

Custom Tkinter and Tkinter are required to run this script.

Install them with the pip command (tkinter usually comes intalled with python).
```
pip install tkinter
pip install customtkinter
```

# How It Works

The ai stores all of the players choices in the current session. It will establish which action the player has chosen most frequently and counter it. If they player chooses the same action repeatedly, the ai will counter this action.

The ai has a consistent winrate of around 70-80% (An rng system will in theory have a 33% winrate).

# Notes

The view ai memory button doesn't currently work as it displays all the options on a single line that exceedes the screen.

The Ai memory text file is not required for this script. It will be generated in the same folder as the script when exported through the program. It can be imported into the current session when the program is run to retain previous session data.

When saving the ai memory, the ai memory text file is appended to, not overwritten.
