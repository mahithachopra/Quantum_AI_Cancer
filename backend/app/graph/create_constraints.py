from connection import get_session

session = get_session()

constraints = [

"""
CREATE CONSTRAINT gene_symbol IF NOT EXISTS
FOR (g:Gene)
REQUIRE g.symbol IS UNIQUE
""",

"""
CREATE CONSTRAINT pathway_id IF NOT EXISTS
FOR (p:Pathway)
REQUIRE p.reactome_id IS UNIQUE
""",

"""
CREATE CONSTRAINT drug_name IF NOT EXISTS
FOR (d:Drug)
REQUIRE d.name IS UNIQUE
""",

"""
CREATE CONSTRAINT cell_name IF NOT EXISTS
FOR (c:CellLine)
REQUIRE c.name IS UNIQUE
"""

]

for c in constraints:

    session.run(c)

session.close()

print("Constraints Created")