import urllib2
import json
import ast
import sys
from pymongo import MongoClient
from datetime import datetime

#Meant for usage with a subprocess runner program

REST_URL = "http://data.bioontology.org"
API_KEY = "*****"

client=MongoClient()
db=client.test


print "Accessed database." #Informs user connection is established to MongoDB                                                                                                     

def get_json(url): #Function to employ json and http verbs to load API pages                                                                                                      
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(url).read())

# Get all ontologies from the REST service and parse the JSON                                                                                                                    \
                                                                                                                                                                                  
all_ontologies = get_json(REST_URL+"/ontologies") #opens the first page http://data.bioontology.org/ontologies                                                                    

onts_acronyms=[] #creates empty list to iterate through                                                                                                                           

#For every ontology, if the ontology is a match to one of those we want proceed through the below process                                                                         

for ontology in all_ontologies:
    
    if ontology["acronym"]==sys.argv[1]:
       onts_acronyms.append(ast.literal_eval(json.dumps(ontology["acronym"])))    #cleans names and removes whitespaces using ast package                                         
       print sys.argv[1] #prints the name for the user to see which collection is being added                                                                                     

for acronym in onts_acronyms:
    #For every desired ontology the following will be collected from the page http://data.bioontology.org/ontologies/INSERT ACRONYM HERE/classes                                  
    
    page= get_json(REST_URL+"/ontologies/"+acronym+"/classes")
    next_page=page
    
    while next_page: #Continue collecting terms until the last page                                                                                                               
        next_page=page["links"]["nextPage"]
        for each_class in page["collection"]:

            if each_class["prefLabel"]!= None:
                result = db[acronym].insert({each_class["prefLabel"]:{"definition":each_class["definition"],"synonyms":each_class["synonym"]}}, check_keys=False)
                #For each term also collect defintion and any synonyms. This line also directly inserts each term in a collection named for the ontology.                         
        
        if next_page:
            page=get_json(next_page)

print  "Added."  #Tells user when this collection has been added to the database  
