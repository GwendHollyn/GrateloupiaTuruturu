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

    return parser.parse_args()

def run_build(args):
    """
    Naive build of the cDBG and serialize it to a file.
    Args: args with input_file, kmer_size, output_file
    Writes: output_file
    """
    # if args.kmer_size < 17: raise ValueError

    # --- build the DBG ---

    # --- serialize the DBG ---
    # time start
    # pickle dump le dbg into args.output_file
    # print time taken

    # add whatever other infos
    pass

def run_query(args):
    """
    Run query on a serialized DBG.
    Args: args with cdbg_path, query_file, output_file
    Writes: output_file
    """
    # time start
    # load the DBG
    # run the query
    # print time taken

    # add whatever other infos
    pass

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