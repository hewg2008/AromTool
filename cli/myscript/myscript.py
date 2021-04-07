import click

# @click.command(name='dot')
# @click.option('--n', default=1, show_default=True)
# @click.argument('dot')
# def dots(n, dot):
#     click.echo('.' * n)
#
@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug modes is %s'('on' if debug else 'off'))

@cli.command()
def sync():
    click.echo('Syncing')