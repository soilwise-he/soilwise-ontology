# Approaches to describe metadata at a column level

Different approaches exist to describe column metadata of soil & landscape observation data. Some are embedded in existing metadata practices.
The column metadata can be used to:

- improve discovery of datasets, by filtering on the observed properties 
- validate if a CSV is valid
- provide overview statistics of a tabular dataset (min-max-avg)
- ingest data to a common model

## Details

Assumes soil observation data in 1 or 2 related tables

Location

ID | Label | X | Y
--- | --- | --- | ---
uae438 | 10m from street | 2.35 | 50.35 
fte218 | 30m bhind barn | 2.45 | 51.15

Horizon

Profile | Label | Upper | Lower | Date | N | P | K 
--- | --- | --- | --- | --- | --- | --- | --- 
uae438 | O | 0 | 10 | 2025-10-04 | 0.3 | 0.01 | 0.01
uae438 | A | 10 | 30 | 2025-10-04 | 0.1 | 0.01 | 0.01

## Approaches

### Soilwise CSV

A tailored CSV format, every row on the table describes a column of a dataset. Notice that dataset metadata (title, abstract, ...) is stored in a separate file.

table | column | title | type | property | unit | procedure
--- | --- | --- | --- | --- | --- | ---
obs.csv | N | Nitrogen | numeric | Nitrogen | mole/kg | TotalN_dc
obs.csv | Profile | Profile | loc.csv#ID | | |
loc.csv | ID | Identifier | string | | |
loc.csv | Label | Label | String | | |


### pygeometa MCF / ISO19115

MCF is a convention of the geopython community. A subset of [iso19115](https://www.iso.org/standard/53798.html) encoded in YAML. 
Attributes in content info are extended to capture unit and procedure. See [sample](./mcf-sample.yml)
Related to [iso19110](https://www.iso.org/standard/57303.html)

https://github.com/geopython/pygeometa

### OKFN Datapackage

An initiative of OKFN. Fields from the table-schema model are extended to capture unit and procedure. See [sample](./datapackage-sample.json)

https://specs.frictionlessdata.io/table-schema/
 

### CSV-W 

An initiative of W3C. See [sample](../CSVW-Excel-Template/example3/obs.csv-metadata.json)

https://csvw.org


### YARRRML

https://rml.io/yarrrml/matey/ is a `friendly` approach to work with rml.io, a modelling technique to model tabular data as RDF.

