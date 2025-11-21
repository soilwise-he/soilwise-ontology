# Approaches to describe metadata at a column level

Different approaches exist to describe column metadata of soil observation data. Some are embedded in existing metadata practices. The column metadata can be used to:

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


### ISO19110 / ISO19115

[ISO19110 Standard on Feature cataloguing](https://www.iso.org/standard/57303.html) is an approach to describe columns in a dataset. Typical properties captured on a feature-attribute are type, uniqueness, etc. This approach is less optimal for capturing observation specific metadata, such as observed property and procedure.

An interesting approach to work with iso19110 metadata is the [MetadataControlFile](https://geopython.github.io/pygeometa/reference/mcf/) format. It is a convention of the geopython community. A subset of [iso19115](https://www.iso.org/standard/53798.html) encoded in YAML. 
Attributes in content info are extended to capture unit and procedure. See [sample](./mcf-sample.yml)

https://github.com/geopython/pygeometa


### OKFN Datapackage

An initiative of [OKFN](https://okfn.org/en/). Fields from the standard table-schema model could be extended to capture unit and procedure. See [sample](./datapackage-sample.json)

https://specs.frictionlessdata.io/table-schema/
 

### CSV-W 

An initiative of W3C. See [sample](./examples/example3/obs.csv-metadata.json)
Very rich method to annotate CSV's, if properly set up, can generate full SOSA/SSN or Schema.org compatible RDF.

https://csvw.org

In SoilWise we're trying out various aspects of CSV-W:

- A [tool in Excel](./CSVW-Excel-Template/) to annotate an existing sheet
- A [web based tool](https://lsc-hubs.github.io/tabular-soil-data-annotation/), where you can upload your data and annotate it in a web environment
- A [LLM based variation to the annotation tool](https://dataannotator-swr.streamlit.app/) 
- Fix bugs on and extend [CSVWLIB](https://github.com/pvgenuchten/csvwlib/tree/latest) to convert CSV-W to RDF
- A [validator tool](../RDF/shacl_sosa.ttl) to test if the generated RDF is valid for the SOSA ontology
- A tool to convert [RDF to RDB](../RDF/rdf2rdb/) (SQLite)
- [TAPIS](https://www.tapis.grumets.cat), A web tool to visualise and combine sensordata, including CSVW format

```mermaid
flowchart LR
    A[CSV] -->|Annotate| B(CSV-W)
    B -->|Serialize| C(RDF)
    D(SHACL) -->|Validate| C
    C -->|ETL| E[SQLite]
```

### YARRRML

https://rml.io/yarrrml/matey/ is a `friendly` approach to work with rml.io, a modelling technique to model tabular data as RDF.


