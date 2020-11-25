# Click

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. You will also be able to understand what the developer wants you to do with the code.

## Installation

Use the package manager [pip](https://pypi.org/project/click/) to install foobar.

```bash
$ pip install click
```

## Usage with Functions:

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

You can use this command line to find out what options you have:

```bash
$ python filename.py --help
```

and that command line will show this:

```bash
Usage: filename.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.

```

you can use the commands that you see in options like this:

```bash
$ python filename.py --count 10 --name 'John'
```

and it would return this:

```bash
Hello John!
Hello John!
Hello John!
Hello John!
Hello John!
Hello John!
Hello John!
Hello John!
Hello John!
Hello John!
```

## Usage with Classes

An example code showing the usage of click in a class:

```bash
import click


class Employee():
  def __init__(self, name, title, salary):
    self.name = name
    self.title = title
    self.salary = salary

  def introduce(self):
    print("I am {}. I work as {}. I make {}.".format(self.name, self.title, self.salary))

@click.command()
@click.option('--name', required=True, default=None,  help='Name of employee')
@click.option('--title', required=True, default=None, help='Job title of employee')
@click.option('--salary', required=True, default=None, help='How much money the employee makes')

def runIntroduction(name,title,salary):
  x = Employee(name,title,salary)
  x.introduce()


if __name__ == '__main__':
    runIntroduction()
```

This is a less complicated way to use click with a class that has only one method, so this wouldn't be good with a class that has many methods, but this code would be able to handle having multiple methods.

```bash
import click


class hello():
    def __init__(self, count, age, name):
        self.count = count
        self.age = age
        self.name = name


    def say_hello(self):
        for i in range(self.count):
            print("My name is {}".format(self.name))
            
    def ages(self):
        print("my age is {}".format(self.age))

    def counts(self):
        print('the count I put in was {}'.format(self.count))

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--age', default=15, help='The persons age.')
@click.option('--name', default='naty', help='The person to greet.')
@click.option('--method', default='say_hello', help='a method that you can run: say_hello, ages, counts')

def runmethod(count, age, name, method):
    x = hello(count, age, name)

    if method.lower() == 'say_hello':
        x.say_hello()

    elif method.lower() == 'ages':
        x.ages()

    elif method.lower() == 'counts':
        x.counts()

if __name__ == '__main__':
    runmethod()
```

This is a code that will be able to handle a class with multiple method, and its less complicated and easier to understand whats going on. This isn't the most efficient but it will get the the job done and there other ways that are more effiecient, but more complicated.
