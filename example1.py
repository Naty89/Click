import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)
        #you can also use just use print
        #print('Hello %s!' % name)

if __name__ == '__main__':
    hello()
    
# you can aso run the function normaly by just saying hello().
