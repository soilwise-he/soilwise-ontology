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
