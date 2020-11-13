import pandas as pd
from sklearn.cluster import KMeans
from retrieveDescriptors import getDescriptors


drugs = getDescriptors("C:\\Users\\Tamara\\Desktop\\nsp16\\descriptors\\nsp16drugsdescriptors.csv")
controls = getDescriptors("C:\\Users\\Tamara\\Desktop\\nsp16\\descriptors\\randomcontrolsdescriptors.csv")

unsupervisedComb = pd.concat([drugs, controls])

kmeans = KMeans(n_clusters = 6, random_state = 0).fit(unsupervisedComb)
print(kmeans.labels_)