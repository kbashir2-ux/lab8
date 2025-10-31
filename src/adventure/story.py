from adventure.utils import read_events_from_file
import random
from rich import print

from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()



def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[bold green]You wake up in a dark forest.[/bold green]")
    console.print("[cyan]You can go [bold]left[/bold] or [bold]right[/bold].[/cyan]")

    while True:
        choice = Prompt.ask("[bold yellow]Which direction do you choose?[/bold yellow]", choices=["left", "right", "exit"])
        if choice == 'exit':
            console.print("[red]You decide to leave the forest. Goodbye![/red]")
            break

        result = step(choice, events)
        console.print(f"[magenta]{result}[/magenta]")




'''
def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("You wake up in a dark forest. You can go left or right.")
    while True:
        choice = input("Which direction do you choose? (left/right/exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
'''
