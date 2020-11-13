import pandas as pd
from sklearn.cluster import KMeans
from retrieveDescriptors import getDescriptors, clean_dataset


drugs = getDescriptors("C:\\Users\\Tamara\\Desktop\\nsp16\\descriptors\\nsp16drugsdescriptors.csv")
controls = getDescriptors("C:\\Users\\Tamara\\Desktop\\nsp16\\descriptors\\randomcontrolsdescriptors.csv")

unsupervisedComb = pd.concat([drugs, controls])
print(unsupervisedComb.shape)

kmeans = KMeans(n_clusters = 5, random_state = 0).fit_predict(unsupervisedComb,y = None, sample_weight = None)
print(kmeans)
