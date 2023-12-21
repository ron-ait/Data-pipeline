# <u>Data-pipeline</u>

## Architecture
![data-pipeline-new (1)](https://github.com/ron-ait/Data-pipeline/assets/100356208/cb7fd9e3-a1ad-4fbe-ad67-318cb4c55963)

## Introduction 
In this project, you will execute an End-To-End Data Pipeline on Real-Time Order Data using Kafka and ELK stack using Docker-Compose.

## Technology Used
🔹 Python3

🔹 Docker-compose 

🔹 Apache Kafka

🔹 ELK Stack 

## Dependency

▪️ For **Python** you can see __requirement.txt__

▪️ In **docker-compose** we have not used logstash, So we need to configure it on our system. 

▪️ In **Logstash** install __/usr/share/logstash/bin/logstash-plugin install logstash-integration-kafka__.



## Kafka Architecture

![Kafka-Architectureedit](https://github.com/ron-ait/Data-pipeline/assets/100356208/4b5498a0-f520-4c56-9031-0e7065ebe25f)

__Kafka__ is a distributed streaming platform that can handle real-time data feeds. It was initially developed by LinkedIn and later open-sourced by Apache Software Foundation. Kafka achieves its high-throughput and fault-tolerance by distributing the load over multiple servers.

### Key Components:

➣ ***Producer:*** The producer is responsible for creating the data and sending it to the Kafka cluster. The producer is decoupled from the cluster and can send data at high speed.

➣ ***Consumer:*** The consumer is responsible for consuming the data produced by the producer. It connects to the Kafka cluster and subscribes to specific topics.

➣ ***Topic:*** A topic is a category or feed name to which the records are published. Topics are used to organize the data into categories.

➣ ***Broker:*** A broker is a Kafka server that receives the records from producers and serves them to consumers. A Kafka cluster can consist of multiple brokers.

➣ ***Zookeeper:*** Zookeeper is a centralized service for maintaining configuration information and providing synchronization and coordination. In a Kafka cluster, Zookeeper helps in electing the cluster's controller and maintaining the broker and partition state.

### Kafka offers several advantages:

🔶 **Horizontal scalability:** Kafka can handle high volumes of data with a scalable and distributed architecture.

🔶 **High throughput:** Kafka can handle millions of records per second.

🔶 **Fault-tolerance:** Kafka ensures data durability and reliability by replicating data across multiple nodes.

🔶 **Low latency:** Kafka allows real-time processing of data with minimal latency.



If you encounter any issues or have suggestions for improvements, please feel free to contribute or report them on the __GitHub repository__. We welcome any feedback to enhance the script further.
