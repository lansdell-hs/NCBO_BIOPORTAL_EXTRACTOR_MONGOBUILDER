import os
import subprocess #required to run commands                                                                                                                                       


#Program runs the builder program for each ontology in the below list, one after the other without additional use input. 
When rebuilding the entire database and an additional ontology is desired, merely add the name to below list in the format 
'ACRONYM' following a comma. Acronyms can be found on the page: https://bioportal.bioontology.org/ontologies. 

#The ontologies that will be extracted                                                                                                                                            
selected_acronyms=['UBERON','BTO','NCBI','OMIM','HP','PR','PAE','WHO','UO','SYMP','PSIMOD','OGMS','BAO','BFO','PATO','DDO','CLO',
                     'NPO','CTCAE','OBI','PO','PW','ICF','ECSO','VIVO','CHEBI','ECO','DERMLEX','TMO','MS','STY','ZEA','GFVO','SO','ZFA','IAO','MDDB','IDO','MP','GO-EXT','CHEMINF\
','RAO','COSTART','COG','FYPO','OCRE','SEDI','HFO','SCDO','NIFSTD','OGG','ORTH','BCGO','AERO','CO-WHEAT','DINTO','ADO',
                     'OBOREL','VT','GENEPIO','GEXO','CTO','ICW','IMMDIS','FB-BT','ABA-AMB','SSO','MAMO','DCM','NLMVS','NATPRO','CSEO','CHEAR','EXO'
                     ,'CHMO','PROCCHEMICAL','PIERO','CHEMBIO','MS','STY','RAO','CL','CPT','EDAM','ENM','ENVO','GO','MEDDRA','MESH','NCIT','RCD','SNOMEDCT']

#Run the builder program for each of the above ontologies, when done, display the message: "Database Built."                                                              
for acronym in selected_acronyms:
    cmd=['python','mongo_builder.py',acronym]
    print cmd
    subprocess.call(cmd)
print "Database Built"







