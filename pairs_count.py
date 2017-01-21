import pandas as pd 
from collections import Counter


def pairs_count(df, col, group_by):
    df = df[[col, group_by]].sort_values(by=[col, group_by]).drop_duplicates().copy()
    it = df.itertuples()
    pair_finder = Counter()
    counter = 1
    
    for row in it:
        _, col, group_by = row
        inner_it = df.iloc[counter:,:].itertuples()
        
        for other_row in inner_it:
            _, other_col, other_group_by = other_row
            if group_by != other_group_by:
                break
            elif col == other_col:
                continue
            else:
                topic_pair = str(col) + '-' + str(other_col)
                pair_finder.update([topic_pair])

        counter += 1

    return pair_finder



