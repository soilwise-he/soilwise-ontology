# An example on using the CSVW Excel template

The startingpoint is a dataset [soveur.csv](./soveur.csv), which has been exported from the [SOTER Eastern Europe dataset](https://data.isric.org/geonetwork/srv/metadata/b1fa4988-b511-48e3-9548-3c48f0a908fa). This database is made available by ISRIC - World Soil Information under a CC-BY-3.0 license.

- The contents of soveur.csv has been copied into the second tab of soveur.xslm (a renamed version of [template](../observation-data-with-column-metadata-template.xlsm)).
- The columns have been imported to the third tab and their type has been set
- The metadata has been exported

**The work is not completed**; some iterations are needed to complete the metadata in the third tab and optimize the script to provide a valid csvw context.

Idea would be to add a python script which imports the csvw concepts to a knowledge graph using [cattle](https://github.com/CLARIAH/cattle)



