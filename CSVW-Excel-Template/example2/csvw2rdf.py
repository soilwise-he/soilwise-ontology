#!/usr/bin/env python3
"""
csv_to_jsonld_csvwlib.py
Convert a CSV + CSVW metadata file into JSON-LD using csvwlib.
"""

import argparse
from csvwlib import CSVWConverter
import rdflib

def convert_to_jsonld(csv_path=None, metadata_path=None, mode="standard"):
    # Run csvwlib conversion
    graph = CSVWConverter.to_rdf(csv_path, metadata_path, mode=mode)
    # Ensure result is an rdflib.Graph
    if not isinstance(graph, rdflib.Graph):
        raise RuntimeError("csvwlib did not return an rdflib.Graph")
    return graph.serialize(format="json-ld", indent=2)

def main():
    parser = argparse.ArgumentParser(description="Convert CSV + metadata to JSON-LD with csvwlib")
    parser.add_argument("--csv", "-c", help="Path or URL to CSV file (optional if metadata references it)")
    parser.add_argument("--meta", "-m", help="Path or URL to CSVW metadata JSON")
    parser.add_argument("--out", "-o", help="Output JSON-LD file (default: print to stdout)")
    parser.add_argument("--mode", default="standard", choices=["standard", "minimal"],
                        help="CSVW conversion mode")
    args = parser.parse_args()

    jsonld = convert_to_jsonld(args.csv, args.meta, mode=args.mode)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(jsonld)
        print(f"✔ Wrote JSON-LD to {args.out}")
    else:
        print(jsonld)


if __name__ == "__main__":
    main()
