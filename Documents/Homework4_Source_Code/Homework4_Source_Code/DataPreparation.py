import torch
import numpy as np
from torchvision import datasets
from torchvision.transforms import ToTensor

class DataPreparation:

    def __init__(self, data_save_path):

        
        self.data_save_path = data_save_path
        self.classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        self.width = 28
        self.height = 28
    def get_data(self):
        # Setup training data
        train_data = datasets.FashionMNIST(
            root=self.data_save_path, # where to download data to?
            train=True, # get training data
            download=True, # download data if it doesn't exist on disk
            transform=ToTensor(), # images come as PIL format, we want to turn into Torch tensors
        )

        # Setup testing data
        test_data = datasets.FashionMNIST(
            root=self.data_save_path,
            train=False, # get test data
            download=True,
            transform=ToTensor()
        )
        return train_data, test_data