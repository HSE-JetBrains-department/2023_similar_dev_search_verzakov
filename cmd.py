import click
from pprint import pprint
from code.statistics.file_stat import find_info


@click.command()
@click.option("--paths", "-p", multiple=True)
def file_stat_cmd(paths):
    for file in paths:
        print(f'{file}:')
        pprint(find_info(file))


if __name__ == "__main__":
    file_stat_cmd()
