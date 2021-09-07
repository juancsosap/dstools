def get_binary_columns(data, verbose=False):
    '''Return Binary Categorical Columns'''
    binary_columns = [] 
    for column in data.select_dtypes('object').columns:
        values = data[column].value_counts().index
        if len(values) == 2:
            if verbose: print(data[column].value_counts(), '\n')
            binary_columns.append(column)
    return binary_columns