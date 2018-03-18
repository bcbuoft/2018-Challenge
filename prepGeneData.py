import os
import pandas as p
from prepTADData import prepData

# Read file obtained via custom download from ensembl biomart
# Custom download:
# Filters: Chromosome/scaffold: 20
#          With HGNC Symbol ID(s): Only
# Attrib.: Gene stable ID
#          Gene start (bp)
#          Gene end (bp)
#          Strand
#          GOSlim GOA Accession(s)
#          GOSlim GOA Description
#          HGNC symbol

def prepGeneData():
    #load the biomart data
    rawFile = os.path.abspath("genes_by_TAD.txt")
    rawData = p.read_table(rawFile, header=0)

    tads = prepData()
    # print(tads)

    #remove duplicate rows
    rawData = rawData.drop_duplicates()

    rawData["circle_len"] = 0

    for g in rawData.index:
        tad_start = tads.iloc[rawData.loc[g].TAD - 1].start
        rawData.loc[g, "start"] -= tad_start
        rawData.loc[g, "end"] -= tad_start
        rawData.loc[g, "circle_len"] = tads.iloc[rawData.loc[g].TAD].end - tad_start

    return rawData

if __name__ == '__main__':
    prepGeneData()