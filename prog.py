import random
import numpy as np
from sklearn.cluster import KMeans
import math
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

class Cluster():

    # K-Means
    def clusterring(xy, orig_cls, n):
        print('Запускаю k-means')
        kmeans = KMeans(n_clusters=n)
        kmeans.fit(xy)
        labels = kmeans.predict(xy)
        centroids = kmeans.cluster_centers_
        cls = []
        for i in range(n):
            cls.append([])
        # Для оценки эффективности находим точки пересечения
        for point in xy:
            min_dist = float('inf')
            dists = []
            i = 0
            for centroid in centroids:
                dist = math.sqrt(((point[0] - centroid[0]) ** 2) + ((point[1] - centroid[1]) ** 2))
                dists.append(dist)
                if dist < min_dist:
                    min_dist = dist
            p = 0
            for dist in dists:
                if dist == min_dist:
                    cls[i].append(point)
                    p += 1
                    if p > 1:
                        print(point, '- точка касания кластеров')
                i += 1
        k = 0
        for cl in orig_cls:
            for c in cls:
                if cl == c:
                    print('Одинаковые кластеры')
                    print(cl)
                    print(c)
                    k += 1
        if k >= n:
            print("K-means работает отлично")
        else:
            for cl in cls:
                print(cl)
        # Иерархическая кластеризация
        print('Запускаю иерархическую кластеризацию по методу Уорда')
        hc = AgglomerativeClustering(n_clusters=n, affinity='euclidean', linkage='ward')
        xy_hc = hc.fit_predict(xy)
        print(xy)
        print(xy_hc)

if __name__ == '__main__':
    print('Hi')