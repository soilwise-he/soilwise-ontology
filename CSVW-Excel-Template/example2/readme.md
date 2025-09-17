# Leafy Tree Example

Goal is to research how a simple relationship between leaves and trees, originating from 2 tables, is managed in csvw.

In this scenario the leaves have been modeled as leaf `dct:isPartOf` tree.

Some findings:
- the array of tables lists all csv's, each with their tableSchema
- The key is in the `aboutUrl` which mints unique identifiers for trees and leaves using a template pattern: `http://example.com/tree/{treeid}`.
The isPartOf relationship is minted with a similar pattern approach.
- To indicate the type described in a row, a convention is to add a virtual column (last) with the rdf:type
- The virtual column doesn't need a titles element from the spec, however the csvwlib tool requires it (but doesn't use it)



