class QueryProcessor:
    def __init__(self, dbg):
        self.dbg = dbg
        self.k_size = dbg.k_size
        # maybe self.n_genomes = dbg.n_genomes  # number of genomes used in the DBG


    def compute_similarity(self, sequence):
        """
        Query the DBG with a given (id, seq) and return ???
        """
        pass

def load_dbg(cdbg_path):
    """
    Load a serialized DBG from a file.
    Args:
    Returns: cdbg
    """
    pass

def get_queries():
    """
    Get the query sequence from file.
    Args:
    Returns: list of query_sequence (id, seq)
    """
    pass

def naive_query():
    """
    main
    Args: cdbg_path, query_file, output_file
    Writes: output_file
    """
    # load the DBG
    # get the queries
    # init QueryProcessor

    # open output_file
    # for each query, compute similarity
        # write the result to output_file
    pass