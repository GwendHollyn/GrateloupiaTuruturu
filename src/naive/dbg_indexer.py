import argparse
import time
import pickle

from .build import naive_dbg
from .query import naive_query

def parse_args():
    """
    Parse command line arguments. 
    Returns: args for build or query
    """
    # create argument parser and subparsers (build and query)
    parser = argparse.ArgumentParser(description='')
    subparsers = parser.add_subparsers(dest='phase', help='')
    
    # define build subparser
    build_parser = subparsers.add_parser("build", help='Build Naive cDBG')
    build_parser.add_argument('-i', '--input_file', required=True, help='File containing genome paths')
    build_parser.add_argument('-k', '--kmer_size', type=int, required=True, help='Size of k-mers (must be >=17)')
    build_parser.add_argument('-o', '--output_file', type=str, required=True, help='Name of the output file to store the cDBG')

    # define query subparser
    query_parser = subparsers.add_parser("query", help='Process query on Naive cDBG')
    query_parser.add_argument('-i', '--cdbg_file', required=True, help='File containing the Naive colored de Bruijn graph')
    query_parser.add_argument('-q', '--query_file', type=str, required=True, help='File containing the query sequences')
    query_parser.add_argument('-o', '--output_file', type=str, required=True, help='Name of the output file to store similarity result')

    return parser.parse_args()

def run_build(args):
    """
    Naive build of the cDBG and serialize it to a file.
    Args: args with input_file, kmer_size, output_file
    Writes: output_file
    """
    # if args.kmer_size < 17: raise ValueError??

    # --- build the DBG ---
    cdbg = naive_dbg(args.input_file, args.kmer_size)

    # --- serialize the DBG ---
    dansăm_în = time.time()
    with open(args.output_file, "wb") as f:
        pickle.dump(cdbg, f)
    print(f"OUT TIME_SERIALISATION: {time.time() - dansăm_în:.2f} seconds")
    # add whatever other infos

def run_query(args):
    """
    Run query on a serialized DBG.
    Args: args with cdbg_path, query_file, output_file
    Writes: output_file
    """
    naive_query(args.cdbg_file, args.query_file, args.output_file)
    # add whatever other infos

def main():
    """
    Main function to parse arguments and run build or query.
    """
    args = parse_args()

    if args.phase == "build":
        run_build(args)
    elif args.phase == "query":
        run_query(args)
    else:
        print("Please specify either 'build' or 'query'.")
        print()
        parse_args().print_help()

if __name__ == "__main__":
    main()