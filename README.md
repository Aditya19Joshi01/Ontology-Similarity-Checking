# Ontology Similarity Checker

This project provides a framework for assessing the similarity between two ontologies using Jaccard and Cosine similarity measures. The framework is developed in Python and utilizes the `rdflib` and `owlready2` libraries to load, parse, and analyze ontologies in OWL format.

## Features

- Load and parse ontologies in OWL format.
- Extract and process classes and properties.
- Compute similarity using Jaccard and Cosine similarity measures.
- Compare identical, partially overlapping, and completely different ontologies.
- User-friendly command-line interface for easy ontology comparison.

## Prerequisites

- Python 3.x
- `rdflib` library
- `owlready2` library
- Protégé (optional, for ontology editing and visualization)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Aditya19Joshi01/Ontology-Similarity-Checking.git
    cd ontology-similarity-checker
    ```

2. **Install the required Python libraries:**
    ```bash
    pip install rdflib owlready2
    ```

## Usage

1. **Prepare your ontologies:**
    - Ensure your ontologies are in OWL format and saved as `.owl` files.
    - Place the ontology files in the project directory or specify the full path when running the script.

2. **Run the similarity checker:**
    ```bash
    python compare_ontologies.py ontology1.owl ontology2.owl
    ```

3. **View the results:**
    - The script will print the similarity results to the console, including common classes, common properties, total classes, and total properties for each ontology.
    - Jaccard and Cosine similarity scores will be displayed to assess the similarity between the ontologies.

## Example

```bash
python compare_ontologies.py examples/ontology1.owl examples/ontology2.owl
```

**Expected Output:**
```
Similarity Results:
Common Classes: 10
Common Properties: 5
Total Classes in Ontology 1: 20
Total Classes in Ontology 2: 25
Total Properties in Ontology 1: 15
Total Properties in Ontology 2: 18
Jaccard Similarity (Classes): 0.40
Jaccard Similarity (Properties): 0.33
Cosine Similarity (Classes): 0.67
Cosine Similarity (Properties): 0.61
```

## Files

- **compare_ontologies.py**: Main script for loading ontologies and calculating similarity.
- **examples/**: Directory containing example ontology files for testing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the developers of `rdflib` and `owlready2` for their powerful libraries.
- Thanks to the Protégé team for providing an excellent ontology editor.
