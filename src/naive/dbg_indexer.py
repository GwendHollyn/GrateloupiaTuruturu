import argparse
import time
from build import fill_dbg
import query

class Index:
    pass



def main():
    parser = argparse.ArgumentParser(description="Naive Build System")
    parser.add_argument('build', type=str, required=True, help='')
    parser.add_argument('query', type=str, required=True, help='')
    
    args = parser.parse_args()
    #if build:
    file_name = r"C:\Users\iborr\OneDrive\Documents\Studies Files\M2_2025.26\ALG\GrateloupiaTuruturu\path.txt"
    dansăm_în_depart= time.time()
    dbg = fill_dbg(file_name, 32)
    dansăm_în_end= time.time()
    dansăm_în_final = format(dansăm_în_end - dansăm_în_depart, '.2f')
    print(f"OUT TIME BUILD: {dansăm_în_final} sec")
    # scerialisation de l'ouptut

    #if query:
