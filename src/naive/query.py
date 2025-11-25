import pickle

def compute_similarity(cdbg, sequence):
    """
    Query the DBG with a given (id, seq) and return results of the similarity.

    return list (id, [similarity values])
    """
    kmer_count = 0
    similarity_results = [0 for _ in range(cdbg.n_genomes)]
    for kmer in extract_kmers(sequence, cdbg.kmer_size):
        kmer_count += 1
        if kmer in cdbg.graph:
            for genome in cdbg.graph[kmer]:
                similarity_results[genome[1]-1]+=1      
    return (sequence[0], similarity_results/kmer_count)

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
    Returns: list of query_sequence (id, seq)
    """
    query_list = []
    i = 1
    with open(query_file,"r") as file:
        for query in file:
            if not query.startswith('>'): # skip header lines
               query_list.apend((f"Seq {i}" , query))
               i+=1
    return query_list

def naive_query(cdbg_path, query_file, output_file):
    """
    main
    Args: cdbg_path, query_file, output_file
    Writes: output_file
    """
    # load the DBG
    # get the queries

    # open output_file
    # for each query, compute similarity
        # write the result to output_file

    cdbg = pickle.load(cdbg_path)
    query_dict = get_queries(query_file)
    for query in query_dict:
        out = compute_similarity(query)
        # with open(output_file, "w") as output:
        #     output.write(f"")
    print(out)