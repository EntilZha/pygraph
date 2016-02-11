# pygraph
pygraph is an extremely simple CLI tool for using graphviz. The intended use case is for generating
small graphs to embed in things like homework problems. The API is documented via the `--help`
option

## Usage
```bash
$ pygraph --help
Usage: pygraph [OPTIONS] FILE EDGES...

Options:
  -e, --engine [dot|neato|twopi|circo|fdp|sfpd|patchword|osage]
  -u, --undirected / -d, --directed
  --format TEXT
  --help                          Show this message and exit.
```

### Examples
```bash
pygraph -d tree ab ac bd be cd ce
```

![tree](tree.png)

```
pygraph -u -e neato circle ab bc cd de ea
```

![circle](circle.png)
