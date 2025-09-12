# Leafy Tree Example

a simple example to indicate a relation between leaves and trees, imported from 2 tables

## csv2rdf

Serialize the graph to json-ld with the csvwlib utility

```
pip install -r requirements.txt
python csvw2rdf.py --meta https://raw.githubusercontent.com/soilwise-he/soilwise-ontology/refs/heads/main/CSVW-Excel-Template/example2/leaves-of-tree-metadata.json --out data.jsonld
```