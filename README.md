# soilwise-ontology
the soilwise ontology is a model for a knowledge graph including datasets, organisations and catalogues

``` mermaid
flowchart LR
    ppl[individual] -->|memberOf| o[organisations]
    ppl -->|authorOf| d
    o -->|partnerIn| p[projects]
    p -->|produce| d[data & knowledge resources]
    o -->|publish| d
    d -->|describedIn| c[catalogues]
    d -->|link| d 
    p -->|part-of| fs[Fundingscheme]
```
