# NCBO_BIOPORTAL_EXTRACTOR_MONGOBUILDER
Python programs that extracts the desired data from specified NCBO BioPortal ontologies and creates a MongoDB database to store them in.

Runner employs subprocess to run the builder program with arguements to only extract desired ontologies, and add to databases one at a time. Previous attempts to build in one program were very inefficient and failed after about 5 ontologies. 
