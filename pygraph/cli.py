from os import path
from collections import namedtuple
import click
import graphviz
from functional import seq

ENGINES = ['dot', 'neato', 'twopi', 'circo', 'fdp', 'sfdp', 'patchword', 'osage']
Edge = namedtuple('Edge', 'left right label')


def split_edge(edge):
    edge_label = None
    if ':' in edge:
        edge, edge_label = edge.split(':')
    if '-' in edge:
        left, right = edge.split('-')
        if right == '':
            right = None
    else:
        left, right = edge
    return Edge(left, right, edge_label)


@click.command()
@click.option('--engine', '-e', default='dot', type=click.Choice(ENGINES))
@click.option('--undirected/--directed', '-u/-d', default=True)
@click.option('--format', default='png', type=str)
@click.option('--name', '-n', default=None, type=str)
@click.option('--dot', is_flag=True)
@click.argument('file', type=click.Path(writable=True))
@click.argument('edges', nargs=-1, required=True)
def main(engine, undirected, format, name, dot, file, edges):
    if undirected:
        graph = graphviz.Graph(engine=engine, format=format)
    else:
        graph = graphviz.Digraph(engine=engine, format=format)
    if name:
        graph.body.append(r'label = "{0}"'.format(name))
    edges = seq(edges).map(split_edge)
    edges.map(lambda e: (e.left, e.right)).flatten().distinct()\
        .filter_not(lambda n: n is None).for_each(lambda n: graph.node(n))
    edges.filter(lambda e: e.right is not None)\
        .for_each(lambda e: graph.edge(e.left, e.right, label=e.label))
    filepath, filename = path.split(file)
    filepath = filepath if filepath != '' else None
    graph.render(filename=filename, directory=filepath, cleanup=not dot)


if __name__ == '__main__':
    main()
