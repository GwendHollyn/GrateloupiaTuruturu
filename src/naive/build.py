import time

class NaiveBuilder:
    """
    Naive colored de Bruijn graph builder from genome sequences.

    Attributes:
    """
    def __init__(self, k_size):
        self.k_size = k_size # k-mer size
        self.graph = {} # dictionary (kmer, set(genome_ids))
        # maybe self.n_genomes = 0 # to count the number of genomes used for the query part

    def add_kmer(self, kmer, genome_id):
        """
        Add a kmer to the graph with its associated genome ID.

        Args:
        """
        if kmer not in self.graph:
            self.graph[kmer] = set() # init new set if new kmer
        self.graph[kmer].add(genome_id) # add gen_id to the set

def read_input_file(input_file):
    """
    Read the input file containing genome paths and return it as a list.

    Args:
    Returns:
    """
    paths_list = []
    with open(input_file,"r") as file:
        for path in file:
            paths_list.append(path.strip())
    return paths_list

def extract_kmers(genome_file, k):
    """
    Extract all k-mers of length k from a genome file.

    Args:
    Yields:
    """
    with open(genome_file, "r") as genome:
        for line in genome:
            line = line.strip()
            if not line.startswith('>'): # skip header lines
                for i in range(len(line)-k+1):
                    yield line[i:i+k] # yield k-mer of length k
                    # yield instead of return to save memory
                    # return one kmer one by one

def naive_dbg(input_file, k):
    """
    Build a naive de Bruijn graph from a list of genome files.

    Args:
    Returns:
    """    
    dansăm_în= time.time() # start time
    dbg = NaiveBuilder(k) # init the DBG
    paths = read_input_file(input_file) # get genome paths
    # dbg.n_genomes = len(paths)  # store the number of genomes used

    for i, path in enumerate(paths, start=1):
        genome_id = f"G{i}"
        for kmer in extract_kmers(path, k): #the current yielded kmer
            dbg.add_kmer(kmer, genome_id)
    dansăm_în= time.time() - dansăm_în # elapsed time
    print(f"OUT TIME_BUILD: {format(dansăm_în, '.2f')} seconds")
    return dbg

# Test
# file_name = "genomes_paths.txt"
# dbg = naive_dbg(file_name, 21)
# print(dbg)



