---
title: 'Terminology'
date: 2024-06-27
authors:
  - Paul van Genuchten
  - Luis de Sousa
  - Mickael Beaufils
  - Beichen Wang
  - Kathy Schleidt
  - Fenny van Egmond
  - Giovanni l'Abate
---

# Terminology

Harmonising terminology within or between communities is an important aspect in cooperation. The SKOS ontology is a common mechanism to advertise (and link between) terminologies.  

For the soil domain we should distinghuish various types of entities for which definitions can be listed. 

- General glossary on soil related terms, what is soil, soil health, soil quality
- Soil **properties** / Soil health indicators to be monitored
- **Results**, in those cases that a result is a reference to a classification (low, medium, high) a proper definition of the class needs to be defined
- **Observation Procedures** describe how an observation has been performed
- The potential occurence of a soil **thread** can be determined by combining a number of indicators
- **Remediation procedures** describe how soil threads can be reduced
- Ability to perform Soil **functions** is estimated by the quality indicators
- Feature Of Interest **types**, an (set of) observation should be representative for a FOI, eg a horizon, profile, plot, site, body



# Inventarisation of existing onotologies

## Agrovoc

[AGROVOC](https://www.fao.org/agrovoc/) is a Linked Open Dataset about agriculture, available for public use and facilitates access and visibility of data across domains and languages. It offers a structured collection of agricultural concepts, terms, definitions and relationships which are used to unambiguously identify resources, allowing standardized indexing processes and making searches more efficient.

- [Browser](https://agrovoc.fao.org/browse/agrovoc/en/) (SKOSMOS)
- [HTML pages](https://aims.fao.org/aos/agrovoc.html) (Loddy)
- [SPARQL end-point](https://agrovoc.fao.org/sparql)

## INSPIRE registry

The INSPIRE infrastructure involves a number of items, which require clear descriptions and the possibility to be referenced through unique identifiers. Examples for such items include INSPIRE themes, code lists, application schemas or discovery services. Registers provide a means to assign identifiers to items and their labels, definitions and descriptions (in different languages). The [INSPIRE registry](https://inspire.ec.europa.eu/registry) provides a central access point to a number of centrally managed INSPIRE registers. The content of these registers are based on the INSPIRE Directive, Implementing Rules and Technical Guidelines.

## IATE

Interactive Terminology for Europe [IATE](https://iate.europa.eu/home) is the EU's terminology management system. It has been used in the EU institutions and agencies since summer 2004 for the collection, dissemination and management of EU-specific terminology. The project was launched in 1999 with the aim of providing a web-based infrastructure for all EU terminology resources, enhancing the availability and standardisation of the information.

## GEMET

EEA and Eionet - the institutional environmental network of almost 40 European countries - are committed to update [GEMET](https://www.eionet.europa.eu/gemet/en/about/) as a source of common and relevant terminology used under the ever-growing environmental agenda.

## ISO11074

The International Standards Organisation has prepared a large number of standards related to [exchange of soil data](https://www.iso.org/obp/ui#iso:std:iso:28258:ed-1:v1:en), [recording soil and site information](https://www.iso.org/obp/ui#iso:std:iso:15903:ed-1:v1:en), [Field soil description](https://www.iso.org/obp/ui#iso:std:iso:25177:ed-2:v1:en), [soil contamination](https://www.iso.org/obp/ui#iso:std:iso:21365:ed-1:v1:en). These standards each reference the iso11074 standard for relevant definitions. These definitions are publicly available via the iso public OBP veiwer [Soil vocabulairy standard (iso11074)](https://www.iso.org/obp/ui#iso:std:iso:11074:ed-2:v1:en:term:2.1.1) ISLANDR project had an initiave to host a [RDF/SKOS version](https://data.geoscience.earth/ncl/ISO11074) of this list

## Glosis web ontology

[Glosis web ontolgy](https://glosis-ld.github.io/glosis/) is a community initiative based on work from FAO and Sieusoil project. The set of soil vocabularies around [FAO guidelines for soil description](https://github.com/iuss-wrb/wrb) is continuously updated to reflect the the latest in soil classification and description.

## ANSIS

The Australian National Soil Information System provides a [complete vocabulary](https://ansis.net/standards/australian-soil-and-land-survey-field-handbook/) service on various aspects of the soil domain.

## WRB

Despite limited online presence various editions of the [World Reference Base](https://github.com/iuss-wrb/wrb) describe a classification system for soils, maintained by the WRB working group of IUSS.
Recent versions include a Fieldguide including a reange of classifications for soil properties (including lab procedures)

## Glosolan

[Standard Operating Procedures of the Global Soil Partnership](https://www.fao.org/global-soil-partnership/glosolan-old/soil-analysis/standard-operating-procedures/en/) are described in pdf's, not available in SKOS (yet) 

## NALT

[National Agricultural thesaurus](https://lod.nal.usda.gov/nalt/en/) is an initiative of USDA, it is widely used due to its completeness and acurateness
