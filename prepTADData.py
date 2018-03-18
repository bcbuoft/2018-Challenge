import os
import pandas as p

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

def prepData():
    #load the biomart data
    rawFile = os.path.abspath("new_tad_positions.txt")
    rawData = p.read_table(rawFile, header=0)

    rawData = rawData.drop("misc", axis=1)
    rawData = rawData.drop("chr", axis=1)

    rawData = rawData.drop_duplicates()

    colfile = os.path.abspath("svgCols.txt")
    cols = p.read_table(colfile, header=None)

    #assign colours and place into ch20 dataframe
    rawData["colour"] = cols[0:len(rawData.index)]
    # rawData.to_csv("new_chr20_data.tsv", sep="\t")
    # print(rawData)
    return rawData

if __name__ == '__main__':
    prepData()