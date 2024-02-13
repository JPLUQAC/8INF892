import MLPRandomHidden
import numpy as np
import matplotlib.pyplot as plt
import torchvision
import torchvision.transforms as transforms

# Configurer les transformations (juste ToTensor)
transform = transforms.Compose([transforms.ToTensor()])

# Definir quelques constantes
ROOT = "./Data/Fashion-MNIST/"
n_epochs = 1000

# Obtenir les donnees d'entrainement
trainset = torchvision.datasets.FashionMNIST(ROOT, download=True, transform=transform)

# Obtrenir les donnes de test
testset = torchvision.datasets.FashionMNIST(ROOT, train=False , download=True, transform=transform)

# Diviser en X et y
X_train, y_train = [], []
for data, target in trainset:
    X_train.append(data.numpy().flatten())
    y_train.append(target)

X_train = np.array(X_train)
y_train = np.array(y_train)

X_test, y_test = [], []
for data, target in testset:
    X_test.append(data.numpy().flatten())
    y_test.append(target)

X_test = np.array(X_test)
y_test = np.array(y_test)


nn = MLPRandomHidden.NeuralNetMLP(n_output=10,
                  n_features=X_train.shape[1],
                  n_hidden=50,
                  l2=0.1,
                  l1=0.0,
                  epochs=n_epochs,
                  eta=0.001,
                  alpha=0.001,
                  decrease_const=0.00001,
                  minibatches=50,
                  shuffle=True,
                  random_state=1)

nn.fit(X_train, y_train, print_progress=True)

# Plot the cost during training
plt.plot(range(len(nn.cost_)), nn.cost_)
plt.ylim([0, 2000])
plt.ylabel('Cost')
plt.xlabel('Epochs * 50')
plt.tight_layout()
plt.show()

# Plot the averaged cost
batches = np.array_split(range(len(nn.cost_)), 1000)
cost_ary = np.array(nn.cost_)
cost_avgs = [np.mean(cost_ary[i]) for i in batches]

plt.plot(range(len(cost_avgs)), cost_avgs, color='red')
plt.ylim([0, 2000])
plt.ylabel('Cost')
plt.xlabel('Epochs')
plt.tight_layout()
plt.show()

# Evaluate training accuracy
y_train_pred = nn.predict(X_train)
acc = np.sum(y_train == y_train_pred, axis=0) / X_train.shape[0]
print('\nTraining accuracy: %.2f%%' % (acc * 100))

# Evaluate test accuracy
y_test_pred = nn.predict(X_test)
acc = np.sum(y_test == y_test_pred, axis=0) / X_test.shape[0]
print('Test accuracy: %.2f%%' % (acc * 100))

# Plot misclassified samples
miscl_img = X_test[y_test != y_test_pred][:25]
correct_lab = y_test[y_test != y_test_pred][:25]
miscl_lab = y_test_pred[y_test != y_test_pred][:25]

fig, ax = plt.subplots(nrows=5, ncols=5, sharex=True, sharey=True,)
ax = ax.flatten()
for i in range(25):
    img = miscl_img[i].reshape(28, 28)
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[i].set_title('%d) t: %d p: %d' % (i+1, correct_lab[i], miscl_lab[i]))

ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
