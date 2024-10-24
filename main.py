import subprocess
import typer

app = typer.Typer()


@app.command()
def update():
    subprocess.Popen("echo 'This is a test'", shell=True)


if __name__ == "__main__":
    app()
