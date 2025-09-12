# Leafy Tree Example

A basic example to indicate a relation between leaves and trees, imported from 2 tables.

## csv2rdf (python)

Serialize the graph to rdf with the [csvwlib](https://pypi.org/project/csvwlib/) utility:

```bash
pip install -r requirements.txt
python csvw2rdf.py --meta https://raw.githubusercontent.com/soilwise-he/soilwise-ontology/refs/heads/main/CSVW-Excel-Template/example2/leaves-of-tree-metadata.json --out data.jsonld
```

Or in rdf/xml:
```bash
python csvw2rdf.py --meta https://raw.githubusercontent.com/soilwise-he/soilwise-ontology/refs/heads/main/CSVW-Excel-Template/example2/leaves-of-tree-metadata.json --out data.xml --format xml
```

csvwlib operates on csv and metadata files on the web, you can run a webserver locally to use local files (with node: `npx httpserver`).

## Read more 

- https://w3c.github.io/csvw/syntax
- https://www.w3.org/TR/tabular-data-primer/
- https://gss-cogs.github.io/csvw-example
- https://www.stevenfirth.com/csv-on-the-web-working-with-units-of-measure/