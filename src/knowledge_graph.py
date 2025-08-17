import spacy
import networkx as nx

nlp = spacy.load("en_core_web_sm")


def extract_entities_relations(text: str) -> list[tuple[str, str, str]]:
    """Extract entities and relations from text using NLP.

    Args:
        text (str): Input text.
    Returns:
        list[tuple[str, str, str]]: List of triplets (entity1, relation, entity2).
    """
    doc = nlp(text)
    triplets = []

    for sent in doc.sents:
        for token in sent:
            if token.pos_ != "VERB":
                continue
            verb = token.lemma_
            subject = None
            obj = None

            for child in token.children:
                if "subj" in child.dep_:
                    subject = child.text
                    break

            if not subject:
                continue

            for child in token.children:
                if "obj" in child.dep_:
                    obj = child.text
                elif child.dep_ == "prep":
                    for pobj in child.children:
                        if pobj.dep_ != "pobj":
                            continue
                        obj = pobj.text

            if obj:
                triplets.append((subject, verb, obj))

    return triplets


def build_knowledge_graph(triplets: list[tuple[str, str, str]]):
    """Build a knowledge graph from entity-relation triplets.

    Args:
        triplets (list[tuple[str, str, str]]): Extracted triplets.
    Returns:
        object: Graph object (e.g., networkx.Graph or Neo4j connection).
    """
    graph = nx.DiGraph()
    for subj, rel, obj in triplets:
        graph.add_node(subj)
        graph.add_node(obj)
        graph.add_edge(subj, obj, relation=rel)
    return graph


def query_graph(graph, query: str) -> list[str]:
    """Query the knowledge graph to answer questions.

    Args:
        graph (object): The knowledge graph.
        query (str): User question in natural language or keyword.
    Returns:
        list[str]: Answers found in the graph.
    """
    pass
