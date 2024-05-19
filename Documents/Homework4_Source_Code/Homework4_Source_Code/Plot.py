import matplotlib.pyplot as plt
import numpy as np
import torch
from torch.utils.data import DataLoader

class Plot:

    def __init__(self):
        self.device = device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    def plot_prediction(self, model, data, figname):
        fashion_mnist_labels = {0: 'T-shirt/top', 1: 'Trouser', 2: 'Pullover', 3: 'Dress', 4: 'Coat',
                            5: 'Sandal', 6: 'Shirt', 7: 'Sneaker', 8: 'Bag', 9: 'Ankle boot'}
        model.eval()
        dataloader = DataLoader(data,batch_size=25,shuffle=False)
        for images, labels in dataloader:
            with torch.no_grad():
                # Assuming data is a batch of images
                images = images.to(self.device)
                labels = labels.to(self.device)
                model.to(self.device)
                predictions = model(images).squeeze()
                predicted_labels = torch.argmax(predictions, axis=1)
                
                # Setting up the plot
                plt.figure(figsize=(10, 10))
                
                # Plotting a subset of images, their true labels, and model's predictions
                for i in range(25):  # Plot 25 images
                    plt.subplot(5, 5, i+1)
                    plt.xticks([])
                    plt.yticks([])
                    plt.grid(False)
                    plt.imshow(images[i].cpu().numpy().reshape(28, 28), cmap=plt.cm.binary)
                    true_label = labels[i].item()
                    predicted_label = predicted_labels[i].item()
                    color = 'green' if true_label == predicted_label else 'red'
                    plt.xlabel("{} ({})".format(fashion_mnist_labels[predicted_label],
                                                fashion_mnist_labels[true_label]),
                            color=color)
                plt.tight_layout()
                plt.savefig(figname)
                plt.close()
            break
