# cli.py
import click

@click.command()
@click.argument('rjcode')
def main(rjcode):
    print(rjcode)

if __name__ == "__main__":
    main()
