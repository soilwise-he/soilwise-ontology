# Soil Data data models

This folder contains various data modelling options to store or exchange soil observation data, which are explored by SoilWise 

- [Observations, Measurements and Samples](#oms)
- [SensorThings API](#sensor-things-api-sta)
- [Relational databases](#relational-databases)
- [Semantic web](#semantic-web)
- [CSVW](#annotated-tabular-data)

### OMS

The [Observations Measurements and Samples](https://www.ogc.org/standards/om/) (previously `observations & measurements`) working group of the Open Geospatial Consortium has a long history of interoperability of (sensor) observation data. Over time the group has prepared various editions of the OMS UML model. A model to exchange interoperable observation data.

Soil data models such as [ISO28258:2013](https://www.iso.org/standard/44595.html) and [INSPIRE Soil](https://github.com/INSPIRE-MIF/technical-guidelines/tree/main/data/so) are based on the OMS datamodel. Data following the UML based models are traditionally exchanged via a GML/XML encoding. 

The [Hale Desktop](https://github.com/halestudio/hale) software is an interesting utility to create or consume these GML documents.



### Sensor Things API (STA)

Over time the OMS group produced a number of data exchange mechanisms, beyond the Web Feature Service protocol, typically used to exchange GML data. The Sensor Observation Service and SensorThings API provide dedicated mechanisms to interact with observation data effectively (advanced select and filter options). 

[SensorThings API](https://www.ogc.org/standards/sensorthings/) is based on [ODATA protocol](https://www.odata.org/). An efficient implementation of the API is provided by the [Frost Server](https://github.com/FraunhoferIOSB/FROST-Server) software.

Beyond the API definition, STA has introduced some conventions on top of OMS, which could be interesting to explore in the scope of a file format.

[Read more](./STA/)

### Relational databases

Over time various groups have worked on initiatives to encode observation data following the OMS UML model in a relational database such as SQLite (GeoPackage), MS Access or PostGreSQL.

Based on the [INSPIRE good practive for geopackage encoding](https://github.com/INSPIRE-MIF/gp-geopackage-encodings) the EJP Soil project and CREA explored options to encode INSPIRE soil data in a GeoPackage format. GeoPackage is a spatial extension to the common SQLite database format. In the SoilWise project [this work](https://github.com/ejpsoil/inspire_soil_gpkg_template) is further extended and tested in an actual data exchange scenario. The SQLite format is focussed on data exchange.

At ISRIC - World Soil Information, a [relational database model for soil data](https://github.com/ISRICWorldSoil/iso-28258) based on ISO28258:2013 has been developed. This model is targetting the PostGreSQL database. The model is optimised for use in an operational multi user Soil Information System.  

[REad more](./GPKG/)

### Semantic web

In the project [Sino-EU Soil Observatory for intelligent Land Use Management (SIEUSOIL)](https://cordis.europa.eu/project/id/818346) the group developed a Semantic Web Ontology based on ISO28258, [GLOSIS-LD](https://github.com/glosis-ld/glosis), using existing ontologies, such as [SSN/SOSA](https://www.w3.org/TR/vocab-ssn/). This work extends on previous work of the [GLOSIS working group](https://github.com/FAO-SID/GloSIS) of FAO/GSP. The GLOSIS-LD initiative provides mechanisms to encode soil observation data in RDF. The ontology is quite rich in listing Observable properties and observation procedures. These Codelists are also used outside the semantic web context.

These days the [Schema.org](https://schema.org) ontology provides options to capture various aspects of observation data via its [Observation](https://schema.org/Observation) class and [variableMeasured](https://schema.org/variableMeasured) property.

Other relevant ontologies in this domain are [iMash](https://archive.researchdata.leeds.ac.uk/42/), [Sweet](https://earthportal.eu/ontologies/SWEET), [iAdopt](https://i-adopt.github.io/ontology/) and [ISO11074](https://www.iso.org/standard/83168.html).

[Read more](./RDF/)

### Annotated tabular data

In the soil science domain it is quite common to share soil observation data in a tabular format (Excel, CSV, DBF). Where samples are listed as rows and observed properties as columns. Column contents are further explained in a readme file or report. Various initiatives exist to standardise the syntax of these readme documents, so also machines can parse this information. We are aware of the following initiatives:

- [CSV-W](./data-models/CSVW/) a json-ld alike initiative to annotate CSV files (as rdf)
- [TableSchema](./data-models/README.md#soil-data-data-models) of the DataPackage inititative.
- [ISO19110:2016](./data-models/README.md#soil-data-data-models) which can be embedded in a ISO19115 document.

In [this repository](./) we're exploring the [CSV-W approach](https://csvw.org/) to annotate tabular data, to make it more interoperable. 

Matching of various Ontology terms is being done under metadata augmentation, see the [matching table](https://github.com/soilwise-he/metadata-augmentation/blob/main/keyword-matcher/result/terms.csv).

Work has been done under SoilWise on a [Soil Health Knowledge Graph](https://soilwise-he.github.io/soil-health/).

[Read more](./CSVW/)