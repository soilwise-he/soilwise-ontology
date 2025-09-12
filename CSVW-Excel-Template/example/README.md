# An example on using the CSVW Excel template

The startingpoint is a dataset [soveur.csv](./soveur.csv), which has been exported from the [SOTER Eastern Europe dataset](https://data.isric.org/geonetwork/srv/metadata/b1fa4988-b511-48e3-9548-3c48f0a908fa). This database is made available by ISRIC - World Soil Information under a CC-BY-3.0 license.

- The contents of soveur.csv has been copied into the second tab of soveur.xslm (a renamed version of [template](../observation-data-with-column-metadata-template.xlsm)).
- The columns have been imported to the third tab and their type has been set
- The metadata has been exported

**The work is not completed**; some iterations are needed to complete the metadata in the third tab and optimize the script to provide a valid csvw context.

Idea would be to add a python script which imports the csvw concepts to a knowledge graph using [cattle](https://github.com/CLARIAH/cattle)


## Using cow-tool-cli

A python tool to parse the csvw

```
pip install cow-csvw
cow_tool_cli --dataset soveur --base http://github.io/soil-health# --format turtle convert ./soveur.csv
```

## Use [csvwlib](https://pypi.org/project/csvwlib/) to generate json-ld

Mind that the csvwlib only runs on uri's, so use the full (github) url to the csv or run a local webserver (node: `npx httpserver`).

```
pip install -r requirements.txt

python csvw2rdf.py --csv http://localhost:8080/soveur.csv --meta http://localhost:8080/soveur.csv-metadata.json --out data.jsonld
```

I had quite unexpected results with this approach, metadata is ignored