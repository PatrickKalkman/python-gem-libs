import typer

app = typer.Typer()


@app.command(help="Convert text between different letter cases.")
def convert(
    text: str = typer.Argument(..., help="The text you want to convert."),
    case: str = typer.Option(
        "lower", help="The target letter case: lower, upper, or title."
    ),
):
    if case == "lower":
        result = text.lower()
    elif case == "upper":
        result = text.upper()
    elif case == "title":
        result = text.title()
    else:
        typer.echo(f"Invalid case option: {case}")
        raise typer.Exit(code=1)

    typer.echo(result)


if __name__ == "__main__":
    app()
