import os
import pandas as p

def chSetUp():
    ch20file = os.path.abspath("new_chr20_data.tsv")
    ch20 = p.read_table(ch20file, header=0)

    #assign different colours to each unique GOAid
    COLs = p.DataFrame()
    # COLs["tad"] = p.Series(ch20.index)
    # GOAs["GOAid"] = p.Series(ch20.GOAid.unique())

    #get colours
    colfile = os.path.abspath("svgCols.txt")
    cols = p.read_table(colfile, header=None)

    #assign colours and place into ch20 dataframe
    COLs["colour"] = cols[0:len(COLs.index)]
    print(COLs)
    # ch20 = ch20.join(COLs.set_index("tad"), on="tad")

    return ch20