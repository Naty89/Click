# Click

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. You will also be able to understand what the developer wants you to do with the code.

## Installation

Use the package manager [pip](https://pypi.org/project/click/) to install foobar.

```bash
pip install click
```

## Usage

An example code showing the usage of click on a function:

```bash
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

```

You can use this command line to find out what option you have:

```bash
$python filename.py --help
```

and that command line will show thisL

```bash
Usage: filename.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.

```
