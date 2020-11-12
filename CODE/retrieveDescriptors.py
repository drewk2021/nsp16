import pandas as pd




def getDescriptors(path):
    """
    Read in CSV to pandas Data Frame Object.
    """
    descriptors = pd.read_csv(path, header = 0, index_col = 0)

    return descriptors

if __name__ == '__main__':
    nsp16drugsdescriptors = getDescriptors("C:\\Users\\Tamara\\Desktop\\nsp16\\descriptors\\nsp16drugsdescriptors.csv")
    print(nsp16drugsdescriptors.dtypes)
    print(nsp16drugsdescriptors.head())