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
