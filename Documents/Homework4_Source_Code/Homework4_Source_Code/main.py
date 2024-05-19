import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import os
import sys
import logging
from DataPreparation import DataPreparation
from Model import FashionMNISTModelV2
from ConfigParser import ConfigParser
from Trainer import Trainer
from Logger import Logger
from Plot import Plot
if os.path.exists("mylog.log"):
    log_file_size = os.path.getsize("mylog.log")
    if log_file_size > 2 * 1024 * 1024:
        os.remove("mylog.log")
        print("The log file was greater than 2MB and has been deleted.")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename="mylog.log",
    filemode='a'
)

stdout_logger = logging.getLogger('STDOUT')
sys.stdout = Logger(stdout_logger, logging.DEBUG)
config = ConfigParser(os.path.join(os.getcwd(), 'config.yaml'))
meta_config = config.get_config()["meta"]
model_config = config.get_config()["model"]

"""
Data Preparation
"""
data_preparation = DataPreparation(meta_config["data_save_path"])
train_data, test_data = data_preparation.get_data()
image_width = data_preparation.width
image_height = data_preparation.height
image_depth = 1
"""
Hyperparameters preparation
"""
config = ConfigParser(os.path.join(os.getcwd(), 'config.yaml'))
training_config = config.get_config()["training"]
model_config = config.get_config()["model"]
if training_config['model'] == "FashionMNISTModelV2":
    model = FashionMNISTModelV2(input_shape=image_depth,hidden_units=model_config["FashionMNISTModelV2"]["hidden_neurons"],output_shape=len(data_preparation.classes))
else:
    raise ValueError("Model not supported")
training_config['model'] = model
training_config['training_data'] = train_data
training_config['testing_data'] = test_data

"""
Training and Testing
"""
trainer = Trainer(**training_config)
trainer.train()
trainer.test()

"""
Plotting

"""
Plot().plot_prediction(training_config['model'],test_data,os.path.join(os.getcwd(), "predictions.png"))