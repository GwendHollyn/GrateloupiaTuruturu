import pickle

def compute_similarity(cdbg, query):
    """
    Query the DBG with a given (id, seq) and compute similarity.

    Args:
        cdbg: the colored de Bruijn graph
        query: (id, seq)
    Returns
        (id, [similarity values])
    """
    seq_id, sequence = query
    kmers = list(extract_kmers(sequence, cdbg.k_size))
    kmer_count = len(kmers)
    similarity_results = [0 for _ in range(cdbg.n_genomes)]

    for kmer in kmers:
        if kmer in cdbg.graph:
            for genome_id in cdbg.graph[kmer]:
                index = int(genome_id[1:]) - 1
                similarity_results[index]+=1
    # Ratio per genome
    similarity_results = [count/kmer_count for count in similarity_results]

    return (seq_id, similarity_results)

def extract_kmers(sequence, k):
    """
    Extract all k-mers of length k in the query sequence.

    Args:
        sequence (str): sequence of the query
    Yields:
        str: k-mer of length k
    """
    for i in range(len(sequence)-k+1):
        yield sequence[i:i+k]        
        # return one kmer one by one

def get_queries(query_file):
    """
    Get the query sequence from file.
    Args:
        query_file: path to the query file
    Returns: 
        list of query_sequence (id, seq)
    """
    query_list = []
    i = 1
    with open(query_file,"r") as file:
        for query in file:
            if not query.startswith('>'): # skip header lines
               query_list.append((f"query_n{i}" , query))
               i+=1
    return query_list

def naive_query(cdbg_path, query_file, output_file):
    """
    Load DBG, compute similarity for each query, and write output file.
    Args:
        cdbg_path: path to the serialized cDBG
        query_file: path to the query file
        output_file: path to the output file
    Writes:
        output_file: similarity results
    """
    # Load CDBG
    with open(cdbg_path, "rb") as f:
        cdbg = pickle.load(f)
    
    # Get queries
    queries = get_queries(query_file)

    with open(output_file, "w") as output:
        for query in queries:
            seq_id, scores = compute_similarity(cdbg, query)
            scores_as_str = "\t".join(f"{s:.3f}" for s in scores) #insert tab between scores
            output.write(f"{seq_id}\t{scores_as_str}\n") # write to output file