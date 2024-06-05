import click
import logging
import documenter.coordinates
from documenter.runner import Runner
from time import sleep

@click.command()
def run():
    logging.basicConfig(level=logging.INFO)
    runner = Runner()
    runner.run()

if __name__ == '__main__':
    run()