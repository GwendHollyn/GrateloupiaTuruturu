import argparse
import time
import os

class NaiveBuilder:
    def __init__(self, kmer_size):
        self.kmer_size = kmer_size

    def read_input_file(input_file):
        out = []
        with open(input_file,"r") as f:
                for path in f:
                    path = path.strip()
                    out.append(path)
        return out

def fill_dbg(input_file, k):
        dbg = {}
        j = 0
        paths = NaiveBuilder.read_input_file(input_file)
        for path in paths:
            j += 1
            print(j)
            with open(path, "r") as genome:
                for line in genome:
                    line = line.strip()
                    if not line.startswith('>'):
                        for i in range(len(line)-k+1):
                            kmer = line[i:i+k]
                            if kmer in dbg:
                                if f"G{j}"  not in dbg[kmer]:
                                    dbg[kmer].append(f"G{j}")
                            else:
                                dbg[kmer] = [f"G{j}"]
                
        return dbg

file_name = r"C:\Users\iborr\OneDrive\Documents\Studies Files\M2_2025.26\ALG\GrateloupiaTuruturu\path.txt"
dansăm_în_depart= time.time()
dbg = fill_dbg(file_name, 32)
dansăm_în_end= time.time()
dansăm_în_final = format(dansăm_în_end - dansăm_în_depart, '.2f')
print(f"OUT TIME BUILD: {dansăm_în_final} sec")


