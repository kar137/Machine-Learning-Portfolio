import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def decision_surface_visualization(X, y, tree_clf):
  plot_step = 0.02
  fig, ax = plt.subplots()
  fig.set_figheight(7)
  fig.set_figwidth(7)

  # For decision surface
  x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
  y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
  xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                            np.arange(y_min, y_max, plot_step))
  colors = ListedColormap(['r','g','b'])

  Z = tree_clf.predict(np.c_[xx.ravel(), yy.ravel()])
  Z = Z.reshape(xx.shape)
  cs = plt.contourf(xx, yy, Z, cmap = colors)

  #decision boundary plotting ends

  scatter = ax.scatter(x=X[:, 0], y=X[:, 1], c=y, edgecolor='black',cmap=colors)

  # produce a legend with the unique colors from the scatter
  legend1 = ax.legend(*scatter.legend_elements(), loc="upper left", title="Classes")
  ax.add_artist(legend1)

  # Produce a legend with a cross section of sizes from the scatter
  handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)

  plt.xlabel('petal length')
  plt.ylabel('petal width')
  plt.title("Decision boundary/surface visualization")
  plt.show()