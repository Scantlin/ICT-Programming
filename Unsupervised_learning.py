#THIS UNSUPERVISED LEARNING USES KMEANS

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    data = sns.load_dataset('iris')
    data.drop(['species', 'sepal_length', 'sepal_width'], axis=1, inplace=True)
    
    #visualize the given dataset
    '''
    plt.scatter(data['petal_length'], data['petal_width'], c='r')
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.savefig('Unsupervised_learning.png')
    plt.show()'''

    K_range = range(1, 10+1)
    sse = []

    for k in K_range:
        K = KMeans(n_clusters=k)
        K.fit(data) #fit the data
        sse.append(K.inertia_)

    #visualize the sse for us to known the K_numbers
    '''
    plt.plot(K_range, sse, 'o-')
    plt.xlabel('number of K')
    plt.ylabel('SSE')
    plt.xticks(range(1, 11))
    plt.savefig('Unsupervised_learning_elbow_method.png')
    plt.show()'''

    clustering = KMeans(n_clusters=3) #model of clustering
    predict = clustering.fit_predict(data[['petal_length', 'petal_width']]) #prediction
    centroids = clustering.cluster_centers_ #to get the centroids

    #add cluster prediction into the dataset
    data['clusters'] = predict
    
    cluster1 = data[data.clusters==0] #retrieve only the clusters that is 0
    cluster2 = data[data.clusters==1] #retrive only the clusters that is 1
    cluster3 = data[data.clusters==2] #retrive only the clusters that is 2
    
    plt.style.use('dark_background')
    plt.title('Unsupervised Learning: Clustering')
    plt.scatter(cluster1['petal_length'], cluster1['petal_width'], color='green', label='Cluster 1')
    plt.scatter(cluster2['petal_length'], cluster2['petal_width'], color='blue', label='cluster 2')
    plt.scatter(cluster3['petal_length'], cluster3['petal_width'], color='orange', label='Cluster 3')
    plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker="*")

    plt.xlabel('petal_length')
    plt.ylabel('petal_width')
    plt.legend()
    plt.savefig('Unsupervised_learning_clustering.png')
    plt.show()

if __name__ == '__main__':
    main()