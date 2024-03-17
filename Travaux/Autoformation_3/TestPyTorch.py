import PyTorchCNN
import torchvision
import torchvision.transforms as transforms

# Quelques constantes
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# Obtenir l'ensemble de donnees CIFAR10 et le normaliser
trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)

cnn = PyTorchCNN.CNN(batch_size=128, epochs=100, n_workers=4)

cnn.fit(trainset, save_model=True)

cnn.validate(testset, model_path='./cifar_net.pth')
