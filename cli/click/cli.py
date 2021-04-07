import click

# @click.command(name='greet')
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
# if __name__ == '__main__':
#     hello()

# @click.group()
# def cli():
#     pass
#
# @click.command()
# def initdb():
#     click.echo('Initialized the database')
#
# @click.command()
# def dropdb():
#     click.echo('Dropped the database')
#
# cli.add_command(initdb)
# cli.add_command(dropdb)
#
# if __name__ == '__main__':
#     cli()

from ase import Atoms
from ase.io import read
from ase import io

print(Atoms.__mro__)
print(io.__all__)
print(io.PickleTrajectory.__mro__)