import tkinter
from tkinter import filedialog
import customtkinter
import random
from collections import defaultdict

def rockSelected ():
    global playerSelectionInt, playerSelection
    playerSelection = "rock"
    playerSelectionInt = 1
    simulateGame()

def paperSelected():
    global playerSelectionInt, playerSelection
    playerSelection = "paper"
    playerSelectionInt = 2
    simulateGame()

def scissorsSelected():
    global playerSelectionInt, playerSelection
    playerSelection = "scissors"
    playerSelectionInt = 3
    simulateGame()

def simulateGame():
    global playerSelectionInt, playerSelection, aiSelectionInt, playerWins, AiWins, whoWonDisplay, playerWinRate, aiWinRate, Games

    memory.append(playerSelectionInt)
    memorySize = len(memory)
    playerChoices = [0, 0, 0] # first is 1(rock) second is 2(paper) third is 3(scissors)
    mostCommonChoice = 0

    if memorySize <= 3:
        aiSelectionInt = random.randint(1,3)
    else:
        for i in range(memorySize):
            if memory[i] == 1:
                playerChoices[0] += 1
            elif memory[i] == 2:
                playerChoices[1] += 1
            elif memory[i] == 3:
                playerChoices[2] += 1
    largestNum = max(playerChoices)

    if largestNum == playerChoices[0]:
        mostCommonChoice = 1
    if largestNum == playerChoices[1]:
        mostCommonChoice = 2
    if largestNum == playerChoices[2]:
        mostCommonChoice = 3

    if len(memory) > 4:
        if memory[-3] and memory[-2] and memory[-1] == memory[-1] or memory[-2] or memory[-3]:
            if memory[-1] == 1:
                aiSelectionInt = 2
            elif memory[-2] == 2:
                aiSelectionInt = 3
            elif memory[-3] == 3:
                aiSelectionInt = 1

    else:
        if mostCommonChoice == 1:
            aiSelectionInt = 2
        elif mostCommonChoice == 2:
            aiSelectionInt = 3
        elif mostCommonChoice == 3:
            aiSelectionInt = 1

    if playerSelectionInt == 1 and aiSelectionInt == 3:
        playerWins += 1
        whoWonDisplay.configure(app, text = "Player Won")
    elif playerSelectionInt == 2 and aiSelectionInt == 1:
        playerWins += 1
        whoWonDisplay.configure(app, text = "Player Won")
    elif playerSelectionInt == 3 and aiSelectionInt == 2:
        playerWins += 1
        whoWonDisplay.configure(app, text = "Player Won")
    elif playerSelectionInt == 3 and aiSelectionInt == 1:
        AiWins += 1
        whoWonDisplay.configure(app, text = "Ai Won")
    elif playerSelectionInt == 1 and aiSelectionInt == 2:
        AiWins += 1
        whoWonDisplay.configure(app, text = "Ai Won")
    elif playerSelectionInt == 2 and aiSelectionInt == 3:
        AiWins += 1
        whoWonDisplay.configure(app, text = "Ai Won")
    aiChoices.append(aiSelectionInt)

    Games += 1

    playerWinRate = playerWins/Games*100
    aiWinRate = 100 - playerWinRate

    winsAiDisplay.configure(app, text = f"AI Wins: {AiWins} ({aiWinRate: .2f}%)")
    winsPlayerDisplay.configure(app, text = f"Player Wins: {playerWins} ({playerWinRate: .2f}%)")
    

def saveMemory():
    with open("ai memory.txt", "a") as file:
        for item in memory:
            file.write(f"{item}\n")
    with open("ai choices.txt", "a") as file:
        for item in aiChoices:
            file.write(f"{item}\n")
    newWindow = customtkinter.CTkToplevel(app)

    
    newWindow.geometry("200x100")
    newWindow.lift()
    newWindow.attributes("-topmost", True)
    done = customtkinter.CTkButton(newWindow, text = "Success", command = newWindow.destroy)
    done.pack()

def importMemory():
    global memory
    filePath = filedialog.askopenfilename(title = "Select a file", filetypes =(("Text files", "*.txt*"), ("All files", "*.*")))
    if filePath:
        with open(filePath, "r") as file:
            memory = [int(line.strip()) for line in file]
        importedSuccesfullyDisplay.configure(app, text = "Success!")

def viewAiMemory():
    newWindow = customtkinter.CTkToplevel(app)
    newWindow.geometry("400x400")
    newWindow.lift()
    newWindow.attributes("-topmost", True)
    displayAiMemory = customtkinter.CTkLabel(newWindow, text = memory)
    displayAiMemory.pack()

def simulate100Games():
    global playerSelectionInt
    for i in range(100):
        playerSelectionInt = random.randint(1,3)
        simulateGame()

def simulate10000Games():
    global playerSelectionInt
    for i in range(10000):
        playerSelectionInt = random.randint(1,3)
        simulateGame()

# rock = 1, paper = 2, scissors = 3
# 1 beats 3
# 2 beats 1
# 3 beats 2

memory = []
aiChoices = []
playerSelection = ""
playerSelectionInt = 0
aiSelectionInt = 0
playerWins = 0
AiWins = 0
Games = 0
playerWinRate = 0
aiWinRate = 0

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x500")
app.title("Rock Paper Scissors AI")


whoWonDisplay = customtkinter.CTkLabel(app, text = "")
whoWonDisplay.pack()

rock = customtkinter.CTkButton(app, text = "Rock", command = rockSelected)
rock.pack()

paper = customtkinter.CTkButton(app, text = "Paper", command = paperSelected)
paper.pack()

scissors = customtkinter.CTkButton(app, text = "Scissors", command = scissorsSelected)
scissors.pack()

winsPlayerDisplay = customtkinter.CTkLabel(app, text = f"Player Wins: {playerWins} ({playerWinRate: .2f}%)")
winsPlayerDisplay.pack()

winsAiDisplay = customtkinter.CTkLabel(app, text = f"AI Wins: {AiWins} ({aiWinRate: .2f}%)")
winsAiDisplay.pack()

saveMemoryToFile = customtkinter.CTkButton(app, text = "Save Memory and Ai choices to .txt file", command = saveMemory)
saveMemoryToFile.pack()

importMemoryToProgram = customtkinter.CTkButton(app, text = "Import Memory", command = importMemory)
importMemoryToProgram.pack()

importedSuccesfullyDisplay = customtkinter.CTkLabel(app, text = "")
importedSuccesfullyDisplay.pack()

sim100gamesbutton = customtkinter.CTkButton(app, text = "Simulate 100 Games", command = simulate100Games)
sim100gamesbutton.pack()

sim10000gamesbutton = customtkinter.CTkButton(app, text = "Simulate 10,000 Games (dont do this it'll crash)", command = simulate10000Games)
sim10000gamesbutton.pack()

displayAiMemory = customtkinter.CTkButton(app, text = "View Ai Memory", command = viewAiMemory)
displayAiMemory.pack()

app.mainloop()