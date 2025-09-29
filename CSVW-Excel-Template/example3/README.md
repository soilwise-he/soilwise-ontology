# A basic observations-on-samples csv

A basic case of multiple observed properties on a featureOfInterest

I had difficulty modelling this in csvw, due to a bug in csvwlib related to valueUrl, [bug is fixed](https://github.com/DerwenAI/csvwlib/pull/4) in latest csvwlib (not on pypi yet) 

Notice that a lot of virtual columns are added, which define relations between the various entities in sosa

**SOSA**
```
pip install csvwlib
csvwlib --meta http://localhost:8080/obs.csv-metadata.json -f ttl --out data.ttl
```

**Schema.org**
```
pip install csvwlib
csvwlib --meta http://localhost:8080/obs.csv-schema-org-metadata.json --out data.jsonld
```
Test the json in [schema.org validator](https://validator.schema.org)

Run a webserver at the current folder (npx httpserver) to be able to call the files as url's.

## also tried csv2rdf, but results are poor

docker run --rm -v $(pwd):/data europe-west2-docker.pkg.dev/swirrl-devops-infrastructure-1/public/csv2rdf:v0.7.1 -t /data/obs.csv -o foo.ttl

