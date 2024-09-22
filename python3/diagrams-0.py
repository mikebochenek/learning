#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mike : Created on Sun Jun 25 09:41:17 2023

https://towardsdatascience.com/diagrams-as-code-python-d9cbaa959ed5
https://diagrams.mingrammer.com/docs/getting-started/examples
https://www.digitalocean.com/community/tutorials/how-to-create-diagrams-in-python-with-diagram-as-code

install/setup 
1. (base) mike@hp:~$ pip3 install diagrams
2. sudo apt install -y graphviz
"""
from diagrams import Cluster, Diagram
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

# and then later open with firefox ->  file:///tmp/advanced_web_service_with_on-premise.png
with Diagram("/tmp/Advanced Web Service with On-Premise", show=False):
    ingress = Nginx("ingress")

    metrics = Prometheus("metric")
    metrics << Grafana("monitoring")

    with Cluster("Service Cluster"):
        grpcsvc = [
            Server("grpc1"),
            Server("grpc2"),
            Server("grpc3")]

    with Cluster("Sessions HA"):
        primary = Redis("session")
        primary - Redis("replica") << metrics
        grpcsvc >> primary

    with Cluster("Database HA"):
        primary = PostgreSQL("users")
        primary - PostgreSQL("replica") << metrics
        grpcsvc >> primary

    aggregator = Fluentd("logging")
    aggregator >> Kafka("stream") >> Spark("analytics")

    ingress >> grpcsvc >> aggregator