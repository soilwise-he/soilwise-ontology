# Leafy Tree Example

Goal is to research how a simple relationship between leaves and trees, originating from 2 tables, is managed in csvw.

In this scenario the leaves have been modeled as leaf `dct:isPartOf` tree.

Some findings:
- the array of tables lists all csv's, each with their tableSchema
- The key is in the `aboutUrl` which mints unique identifiers for trees and leaves using a template pattern: `http://example.com/tree/{treeid}`.
The isPartOf relationship is minted with a similar pattern approach.
- To indicate the type described in a row, a convention is to add a virtual column (last) with the rdf:type
- The virtual column doesn't need a titles element from the spec, however the csvwlib tool requires it (but doesn't use it)


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
