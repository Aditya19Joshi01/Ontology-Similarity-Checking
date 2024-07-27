import rdflib
from sklearn.metrics import jaccard_score
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def load_ontology(file_path):
    graph = rdflib.Graph()
    graph.parse(file_path, format="xml")
    return graph

def extract_classes_and_properties(ontology):
    classes = set(ontology.subjects(rdflib.RDF.type, rdflib.OWL.Class))
    object_properties = set(ontology.subjects(rdflib.RDF.type, rdflib.OWL.ObjectProperty))
    datatype_properties = set(ontology.subjects(rdflib.RDF.type, rdflib.OWL.DatatypeProperty))
    return classes, object_properties.union(datatype_properties)

def calculate_jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def calculate_cosine_similarity(set1, set2):
    vectorizer = CountVectorizer().fit_transform([' '.join(set1), ' '.join(set2)])
    vectors = vectorizer.toarray()
    return np.dot(vectors[0], vectors[1]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1]))

def compare_ontologies(ontology1, ontology2):
    ontology1_classes, ontology1_properties = extract_classes_and_properties(ontology1)
    ontology2_classes, ontology2_properties = extract_classes_and_properties(ontology2)

    jaccard_classes = calculate_jaccard_similarity(ontology1_classes, ontology2_classes)
    jaccard_properties = calculate_jaccard_similarity(ontology1_properties, ontology2_properties)

    cosine_classes = calculate_cosine_similarity(ontology1_classes, ontology2_classes)
    cosine_properties = calculate_cosine_similarity(ontology1_properties, ontology2_properties)

    return {
        "common_classes": len(ontology1_classes.intersection(ontology2_classes)),
        "common_properties": len(ontology1_properties.intersection(ontology2_properties)),
        "total_classes_ontology1": len(ontology1_classes),
        "total_classes_ontology2": len(ontology2_classes),
        "total_properties_ontology1": len(ontology1_properties),
        "total_properties_ontology2": len(ontology2_properties),
        "jaccard_classes": jaccard_classes,
        "jaccard_properties": jaccard_properties,
        "cosine_classes": cosine_classes,
        "cosine_properties": cosine_properties
    }

def main(ontology_path1, ontology_path2):
    ontology1 = load_ontology(ontology_path1)
    ontology2 = load_ontology(ontology_path2)

    similarity_results = compare_ontologies(ontology1, ontology2)

    print("Similarity Results:")
    print(f"Common Classes: {similarity_results['common_classes']}")
    print(f"Common Properties: {similarity_results['common_properties']}")
    print(f"Total Classes in Ontology 1: {similarity_results['total_classes_ontology1']}")
    print(f"Total Classes in Ontology 2: {similarity_results['total_classes_ontology2']}")
    print(f"Total Properties in Ontology 1: {similarity_results['total_properties_ontology1']}")
    print(f"Total Properties in Ontology 2: {similarity_results['total_properties_ontology2']}")
    print(f"Jaccard Similarity (Classes): {similarity_results['jaccard_classes']}")
    print(f"Jaccard Similarity (Properties): {similarity_results['jaccard_properties']}")
    print(f"Cosine Similarity (Classes): {similarity_results['cosine_classes']}")
    print(f"Cosine Similarity (Properties): {similarity_results['cosine_properties']}")

if __name__ == "__main__":
    ontology_path1 = "ontology1.owl"
    ontology_path2 = "ontology4.owl"  # similar but not identical ontologies
    main(ontology_path1, ontology_path2)


