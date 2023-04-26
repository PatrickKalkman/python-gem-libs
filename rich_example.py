from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax

console = Console()

# Text styling
console.print("Hello, [bold]World[/bold]!")
console.print("Python is [italic]awesome![/italic]")
console.print("Rich is a [italic][bold]hidden gem[/bold][/italic]")
console.print("Let's [underline]learn[/underline] something new.")

# Table
table = Table(title="Books", show_header=True, header_style="bold magenta")
table.add_column("Title", style="cyan")
table.add_column("Author", style="green")
table.add_column("Year", style="yellow")

table.add_row("The Catcher in the Rye", "J.D. Salinger", "1951")
table.add_row("To Kill a Mockingbird", "Harper Lee", "1960")
table.add_row("Pride and Prejudice", "Jane Austen", "1813")

console.print(table)

# Syntax highlighting
code = """
def hello_world():
    print("Hello, World!")

hello_world()
"""

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
