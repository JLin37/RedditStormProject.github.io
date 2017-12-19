# RedditStormProject

# What is Storm?

Apache-Storm is a free and open source distributed realtime computation system. The system processes large volumes of high-velocity data, which requires Storm to be extremely fast, scalable, fault-tolerant, reliable and easy to operate. Storm has the ability to process over a million records per second per node on a cluster, with parallel calculations that run across a cluster of machines. It automatically restarts workers or nodes when they die to stay fault-tolerant. Storm guarantees that each unit of data is processed at least once or exactly once and stays reliable. 

Storm uses custom created “sprouts” and “bolts” to define information sources and manipulations to allow batch, distributed processing of streaming data. With sprouts and bolts acting as the graph vertices, Storm application is designed as a “topology” in the shape of a directed acyclic graph. Together, the topology serves the role of data transformation pipeline. When the data comes in, it is processed and the results are passed into Hadoop.
We will look into the topology of the system more in-depth later on in this tutorial.

Storm was written predominantly in the Clojure programming language, but can be used with any programming language and many use cases. Lately, it is popular for realtime analytics, online machine learning, continuous computation, data monetization, operational dashboards and cyber security analytics and threat detection. Recent progress in Storm includes, adding reliable realtime data processing capabilities to Enterprise Hadoop, integrates with YARN by Apache Slider for YARN to manage Storm while considering cluster resources for data governance, security and operations components of a modern big data architecture such as Lambda Architecture. 

# How does Storm work?



Components


![picture2](https://user-images.githubusercontent.com/33638238/34182295-a41f3ffa-e4e3-11e7-93e0-8860fda6169e.png)


A Storm cluster is superficially similar to a Hadoop cluster. Whereas on Hadoop you run "MapReduce jobs", on Storm you run "topologies". "Jobs" and "topologies" themselves are very different -- one key difference is that a MapReduce job eventually finishes, whereas a topology processes messages forever (or until you kill it).[1]

There are two kinds of nodes on a Storm cluster: the master node and the worker nodes. The master node runs a daemon called "Nimbus" that is similar to Hadoop's "JobTracker".
 

§  Nimbus: It sends codes to workers. Nimbus is also responsible for detecting when workers die and reassigning them to other machines when necessary.

§  Supervisors: Each worker in the Storm clusters has Supervisor daemon that executes tasks as directed the location of other worker tasks.

§  Zookeepers: Coordinate between Nimbus and the Supervisors. Storm uses Zookeeper to track configuration information about the topology; Additionally, the Nimbus daemon and Supervisor daemons are fail-fast and stateless; all state is kept in Zookeeper or on local disk. This means you can kill -9 Nimbus or the Supervisors and they'll start back up like nothing happened. This design leads to Storm clusters being incredibly stable.



Topologies
 
 ![picture1](https://user-images.githubusercontent.com/33638238/34181883-fdeb9a58-e4e1-11e7-8b29-1382ad415ac5.png)
 
 
A topology is a graph of computation. Each node in a topology contains processing logic, and links between nodes indicate how data should be passed around between nodes.[2]

1.   The work is delegated to different types of components that are each responsible for a simple specific processing task.
2.   The input stream of a Storm cluster is handled by s component called Spout.
3.   The sprout passes the data to a component called a Bolt, which transforms it in some way.
4.   A bolt either persists the data in some sort of storages, or passes it to some other bolt. [3]

