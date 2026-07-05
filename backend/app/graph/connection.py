from neo4j import GraphDatabase

from config import *

driver = GraphDatabase.driver(

    NEO4J_URI,

    auth=(NEO4J_USER, NEO4J_PASSWORD)

)


def get_session():

    return driver.session()


def close():

    driver.close()