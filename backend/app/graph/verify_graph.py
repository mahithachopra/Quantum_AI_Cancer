from connection import get_session

session = get_session()

queries = {

    "Genes":
    "MATCH (n:Gene) RETURN count(n)",

    "Pathways":
    "MATCH (n:Pathway) RETURN count(n)",

    "Drugs":
    "MATCH (n:Drug) RETURN count(n)",

    "CellLines":
    "MATCH (n:CellLine) RETURN count(n)",

    "Gene_Pathway":
    "MATCH ()-[r:INVOLVED_IN]->() RETURN count(r)",

    "Drug_Gene":
    "MATCH ()-[r:TARGETS]->() RETURN count(r)",

    "Drug_Response":
    "MATCH ()-[r:RESPONDS_TO]->() RETURN count(r)",

    "Pathway_Hierarchy":
    "MATCH ()-[r:PARENT_OF]->() RETURN count(r)"
}

print("=" * 60)
print("KNOWLEDGE GRAPH SUMMARY")
print("=" * 60)

for name, query in queries.items():

    value = session.run(query).single()[0]

    print(f"{name:25}: {value:,}")

session.close()

print("=" * 60)