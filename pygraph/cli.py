from os import path
import click
import graphviz
from functional import seq

ENGINES = ['dot', 'neato', 'twopi', 'circo', 'fdp', 'sfdp', 'patchword', 'osage']


@click.command()
@click.option('--engine', '-e', default='dot', type=click.Choice(ENGINES))
@click.option('--undirected/--directed', '-u/-d', default=True)
@click.option('--format', default='png', type=str)
@click.argument('file', type=click.Path(writable=True))
@click.argument('edges', nargs=-1, required=True)
def main(engine, undirected, format, file, edges):
    if undirected:
        graph = graphviz.Graph(engine=engine, format=format)
    else:
        graph = graphviz.Digraph(engine=engine, format=format)
    seq(edges)\
        .flatten()\
        .distinct()\
        .for_each(lambda n: graph.node(n))
    graph.edges(edges)
    filepath, filename = path.split(file)
    filepath = filepath if filepath != '' else None
    graph.render(filename=filename, directory=filepath, cleanup=True)


if __name__ == '__main__':
    main()
