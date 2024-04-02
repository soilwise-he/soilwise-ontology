# soilwise-ontology

The soilwise ontology is a model for a knowledge graph including datasets, organisations and catalogues.

It aims to capture on both data and knowledge resources:

- in which context (project/funding) the resource has been created
- in which catalogue(s) it is described
- any observations (validation, usage, user feedback) on the resource during its lifetime

``` mermaid
flowchart LR
    ppl[individual] -->|memberOf| o[organisation]
    ppl -->|authorOf| d
    o -->|partnerAs| r
    p[project] -->|produce| d[data & knowledge resource]
    obs[observation] -->|on| d
    o -->|publish| d
    d -->|describedIn| c[catalogue]
    d -->|link| d
    r[role] -->|in| p
    p -->|partOf| g[grant]
    g -->|funding| fs[Fundingscheme]
```

## DCAT

Datasets (as part of catalogues) is commonly described using the [DCAT ontology](https://www.w3.org/TR/vocab-dcat-2/).

![DCAT datamodel](https://www.w3.org/TR/vocab-dcat-2/images/DCAT-summary-all-attributes.png)

DCAT includes aspects of the dublin core, skos, vcard (to describe an individual) and foaf (to contact a person) ontologies.

## Cordis 

[cordis](https://cordis.europa.eu/) is a catalogue of Horizon Europe funded research projects.

![Cordis data model](https://blog.sparna.fr/wp-content/uploads/2024/01/EURIO_v2.4-1024x812.png)
