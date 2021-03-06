import urllib2
import json
import ast

REST_URL = "http://data.bioontology.org"
API_KEY = "**********************"

def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(url).read())

# Get all ontologies from the REST service and parse the JSON
all_ontologies = get_json(REST_URL+"/ontologies")
selected_ontologies=['CPT','MEDDRA']
# Iterate looking for ontology with acronym BRO
ont = None
onts=[]

for ontology in all_ontologies: #python if in logic
    if ontology["acronym"] in selected_ontologies:#== "BRO": #"BRO" or
        ont = ontology
        onts.append(ontology["acronym"])

labels = []
synonyms=[]
definitions=[]

# Using the hypermedia link called `classes`, get the first page
page = get_json(ont["links"]["classes"])

# Iterate over the available pages adding labels from all classes
# When we hit the last page, the while loop will exit
next_page = page
while next_page:
    next_page = page["links"]["nextPage"]
    for ont_class in page["collection"]:

        labels.append(ont_class["prefLabel"])
        synonyms.append(ont_class["synonym"])
        definitions.append(ont_class["definition"])

    if next_page:
        page = get_json(next_page)

labels_literal=ast.literal_eval(json.dumps(labels))
definitions_literal=ast.literal_eval(json.dumps(definitions))



for label, definition in zip(labels_literal,definitions_literal):
    print (label,definition)
