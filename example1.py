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
