import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

centroids = np.array([[1, 2, 1], [2, 5, 2], [-3, 3, 0], [5, -1, -1], [-2, -2, -2]])
num_centroids = len(centroids)
dimensionality = len(centroids[0])
num_datapoints = 100

gaussian_distribution = 0.8 * np.random.randn(num_datapoints, num_centroids, dimensionality)
input_datapoints = np.array([centroids + x for x in gaussian_distribution])
input_datapoints.shape = (num_datapoints * num_centroids, dimensionality)
np.random.shuffle(input_datapoints)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(input_datapoints[:,0], input_datapoints[:,1], input_datapoints[:,2], 'b.')
plt.show()

normalization_factor = np.linalg.norm(input_datapoints)
input_datapoints_norm = input_datapoints / normalization_factor

neural_net = nl.net.newc([[0, 1] for _ in range(dimensionality)], num_centroids)
error = neural_net.train(input_datapoints_norm, epochs=500, show=50)
predicted_centroids = neural_net.layers[0].np['w']
predicted_centroids = predicted_centroids * normalization_factor

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(input_datapoints[:,0], input_datapoints[:,1], input_datapoints[:,2], 'c.')
ax.plot(centroids[:,0], centroids[:,1], centroids[:,2], 'r*', markersize=12)
ax.plot(predicted_centroids[:,0], predicted_centroids[:,1], predicted_centroids[:,2], 'kh', markersize=8)
plt.legend(['datapoints', 'actual centroids', 'predicted centroids'])
plt.show()
