import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class CNN(nn.Module):

    def __init__(self, batch_size, epochs, n_workers):

        self.batch_size = batch_size
        self.epochs = epochs
        self.n_workers = n_workers

        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.conv2 = nn.Conv2d(16, 32, 3)
        self.conv3 = nn.Conv2d(32, 64, 3)
        self.conv4 = nn.Conv2d(64, 128, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.10)
        self.softmax = nn.LogSoftmax(dim=1)
        self.fc1 = nn.Linear(128 * 5 * 5, 1200)
        self.fc2 = nn.Linear(1200, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = self.pool(x)
        x = F.relu(self.conv4(x))
        x = self.pool(x)
        x = torch.flatten(x, 1)
        x = self.dropout(x)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        x = self.softmax(x)

        return x

    def fit(self, trainset, save_model=False):
        trainloader = torch.utils.data.DataLoader(trainset, batch_size=self.batch_size, shuffle=True, num_workers=self.n_workers)

        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(self.parameters(), lr=0.001, momentum=0.9)

        print('Training mode: ' + str(self.device))
        self.to(self.device)

        print('Started Training')
        for epoch in range(self.epochs):

            print('Epoch :' + str(epoch) + '/' + str(self.epochs))
            for i, data in enumerate(trainloader, 0):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)

                optimizer.zero_grad()

                outputs = self(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
        
        if save_model:
            PATH = './cifar_net.pth'
            torch.save(self.state_dict(), PATH)

        print('Finished Training')

    def validate(self, testset, model_path):
        testloader = torch.utils.data.DataLoader(testset, batch_size=self.batch_size, shuffle=False, num_workers=self.n_workers)

        print('Validate mode: ' + str(self.device))
        self.to(self.device)

        dataiter = iter(testloader)
        images, labels = next(dataiter)[0].to(self.device), next(dataiter)[1].to(self.device)

        self.load_state_dict(torch.load(model_path))

        outputs = self(images)

        _, predicted = torch.max(outputs, 1)

        correct = 0
        total = 0
        with torch.no_grad():
            for data in testloader:
                images, labels = data[0].to(self.device), data[1].to(self.device)
                outputs = self(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')