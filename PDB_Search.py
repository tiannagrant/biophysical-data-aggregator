#PDB query, advanced search finds all PDBs that have been resolved using Solid State NMR.

# functions for conducting searches and obtaining lists of PDB ids
def make_query(search_term, querytype='AdvancedKeywordQuery'):
    ''' Repackage strings into a search dictionary
    This function takes a list of search terms and specifications
    and repackages it as a dictionary object that can be used to conduct a search
