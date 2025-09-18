# A template to annotate the columns in your Excel/CSV dataset with metadata

[CSV on the web](https://www.w3.org/TR/tabular-data-primer/) is an initiative of W3C to annotate CSV with proper metadata so the CSV 
data can be effectively re-used. This repository contains an Excel template which can assist you in annotating each column of a CSV 
and export the result to a CSVW metadata file. Place the exported file alongside the original CSV while uploading the dataset to a 
repository such as Zenodo. 

How To:
- Open this sheet with macro's enabled
- Adjust the document properties (exported as dataset level metadata)
- Paste your dataset in the `data tab` of this excel
- On the `metadata tab`, click `import columns` to fetch the columns of the data sheet
- Complete the metadata for each of the columns
- Export the columns metadata to {datafile}-metadata.json
- Place the metadata file in the same folder (or zip file) of your the datafile 

**The tool is beta, syntax has not been validated to the CSV-W standard yet**

# A command line tool to work with csvwlib

[csvwlib](https://pypi.org/project/csvwlib/) is a python library to work with csvw concepts. this script enables to work with csvwlib from the commandline.

Install (use a virtual environment):
```bash
pip install -r requirements.txt
python csvw2rdf.py --help
```

Serialize:
```bash
python csvw2rdf.py --meta https://raw.githubusercontent.com/soilwise-he/soilwise-ontology/refs/heads/main/CSVW-Excel-Template/example2/leaves-of-tree-metadata.json --out data.jsonld
```

Or in rdf/xml:
```bash
python csvw2rdf.py --meta https://raw.githubusercontent.com/soilwise-he/soilwise-ontology/refs/heads/main/CSVW-Excel-Template/example2/leaves-of-tree-metadata.json --out data.xml --format xml
```

csvwlib operates on csv and metadata files on the web, you can run a webserver locally to use local files (with node: `npx httpserver`).

## Validate SOSA

[pyshacl](https://pypi.org/project/pyshacl/) is a tool to validate a knowledge graph against a set of shacl statements. KWG prepared a [shacl validation for sosa](https://github.com/KnowWhereGraph/KWG-SHACL/blob/main/shacl_sosa.ttl).

```bash
pip install pyshacl
pyshacl -s https://github.com/KnowWhereGraph/KWG-SHACL/raw/refs/heads/main/shacl_sosa.ttl -m -i rdfs -a -j -f human data.ttl
```

## Read more 

- https://w3c.github.io/csvw/syntax
- https://www.w3.org/TR/tabular-data-primer/
- https://gss-cogs.github.io/csvw-example
- https://www.stevenfirth.com/csv-on-the-web-working-with-units-of-measure/
- https://greggkellogg.net/2015/04/implementing-csv-on-the-web/