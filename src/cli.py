#!/user/bin/env python3

# cli.py

import click
from .calculate_hanka import flip_coin
from .calculate_hanka import roll_dice

@click.command()
def flip_coin_cli():
    click.echo(flip_coin())

@click.command()
def roll_dice_cli(n_dice, n_sides):
    click.echo("")
    for d in roll_dice( n_dice, n_sides):
        click.secho(f" {d} \n", bold=True, bg="red")

@click.option('--n_dice', default=1, help="Number of dice to roll")
@click.option('--n_sides', default=6, help="Number of sides on each die")
@click.command()



    

