# Log Monitoring and Anomaly Detection Application

This application is designed to monitor log files and identify anomalies within the logs. The training process for the anomaly detection model utilizes the **NSL-KDD dataset**, which provides a standard benchmark for training and evaluating models in network intrusion detection and anomaly detection.

## Features
- Real-time log monitoring for anomalies.
- Integration of machine learning models for anomaly detection.
- Based on a reliable and widely used dataset (NSL-KDD) for training the detection model.

## Purpose
The primary purpose of this application is to assist system administrators and IT professionals in identifying and mitigating potential issues or security threats by analyzing log files efficiently and effectively.

## Training Dataset
The **NSL-KDD** dataset is used during the training phase to build and fine-tune the anomaly detection model. This dataset is a refined version of the original KDD Cup 1999 dataset, designed to overcome some inherent issues in the original version, such as redundancy and imbalance.

## How It Works
1. The application processes incoming log files in real-time or in batch mode.
2. It applies the trained model to detect patterns of normal and abnormal behavior in the logs.
3. Alerts or reports are generated for detected anomalies, allowing for prompt action.

## Requirements
- A trained model based on NSL-KDD (provided with the application or trainable using the dataset).
- Log files in a structured format for effective processing.

## Getting Started
1. Install the required dependencies.
2. Configure the application to point to the location of your log files.
3. Run the application to start monitoring and anomaly detection.

## User Interface Overview
### EDA feature
![Application Homepage](AI_security_app/Picture/pages_EDA1.png)
