from time import sleep
from rich.console import Console
import os
from argparse import ArgumentParser
from colorama import Fore, Style
import timeit

start = timeit.default_timer()
parser = ArgumentParser(
    description="Creates a blank slh project")

parser.add_argument("name", help="create a slh project.")
arg = parser.parse_args()

console = Console()
tasks = [f"Creating {n}" for n in range(1,4)]

with console.status("[bold green]Creating slh project...") as status:
    try:
        os.mkdir(arg.name)
    except FileExistsError:
        print(Fore.RED + "Couldn't make a project because the file already exists. Try using another project name or delete the existing project. Closing.......")
        print(Style.RESET_ALL)
        quit()
    with open(f"{arg.name}/main.slh", 'w') as f:
        f.write('''
start:
    printout "Hello World"
    skip to_this
    printout "We are back"
    break
    printout "This wont show, sed :(."

to_this:
    printout "Lets go somewhere"
        ''')
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} for project: {arg.name}")

stop = timeit.default_timer()
total_time = stop - start

print(Fore.GREEN + 
f"Done.... Happy Coding !!!. Process completed in {round(total_time)} seconds")
print(Style.RESET_ALL)