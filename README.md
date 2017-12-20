# What is Storm?

![image not available](http://vishnuviswanath.com/img/storm_blog_header.png)

Apache-Storm is a free and open source distributed realtime computation system. The system processes large volumes of high-velocity data, which requires Storm to be extremely fast, scalable, fault-tolerant, reliable and easy to operate. Storm has the ability to process over a million records per second per node on a cluster, with parallel calculations that run across a cluster of machines. It automatically restarts workers or nodes when they die to stay fault-tolerant. Storm guarantees that each unit of data is processed at least once or exactly once and stays reliable. 

Storm uses custom created “spouts” and “bolts” to define information sources and manipulations to allow batch, distributed processing of streaming data. With sprouts and bolts acting as the graph vertices, Storm application is designed as a “topology” in the shape of a directed acyclic graph. Together, the topology serves the role of data transformation pipeline. When the data comes in, it is processed and the results are passed into Hadoop.
We will look into the topology of the system more in-depth later on in this tutorial.

Storm was written predominantly in the Clojure programming language, but can be used with any programming language and many use cases. Lately, it is popular for realtime analytics, online machine learning, continuous computation, data monetization, operational dashboards and cyber security analytics and threat detection. Recent progress in Storm includes, adding reliable realtime data processing capabilities to Enterprise Hadoop, integrates with YARN by Apache Slider for YARN to manage Storm while considering cluster resources for data governance, security and operations components of a modern big data architecture such as Lambda Architecture. 

# How does Storm work?

## 1. Components

![picture2](https://user-images.githubusercontent.com/33638238/34182295-a41f3ffa-e4e3-11e7-93e0-8860fda6169e.png)

A Storm cluster is superficially similar to a Hadoop cluster. Whereas on Hadoop you run "MapReduce jobs", on Storm you run "topologies". "Jobs" and "topologies" themselves are very different -- one key difference is that a MapReduce job eventually finishes, whereas a topology processes messages forever (or until you kill it).

There are two kinds of nodes on a Storm cluster: the master node and the worker nodes. The master node runs a daemon called "Nimbus" that is similar to Hadoop's "JobTracker".
 
- Nimbus: It sends codes to workers. Nimbus is also responsible for detecting when workers die and reassigning them to other machines when necessary.

- Supervisors: Each worker in the Storm clusters has Supervisor daemon that executes tasks as directed the location of other worker tasks.

- Zookeepers: Coordinate between Nimbus and the Supervisors. Storm uses Zookeeper to track configuration information about the topology; Additionally, the Nimbus daemon and Supervisor daemons are fail-fast and stateless; all state is kept in Zookeeper or on local disk. This means you can kill -9 Nimbus or the Supervisors and they'll start back up like nothing happened. This design leads to Storm clusters being incredibly stable.

## 2. Topologies
 
 ![picture1](https://user-images.githubusercontent.com/33638238/34181883-fdeb9a58-e4e1-11e7-8b29-1382ad415ac5.png)
  
A topology is a graph of computation. Each node in a topology contains processing logic, and links between nodes indicate how data should be passed around between nodes.

- The work is delegated to different types of components that are each responsible for a simple specific processing task.
- The input stream of a Storm cluster is handled by s component called Spout.
- The sprout passes the data to a component called a Bolt, which transforms it in some way.
- A bolt either persists the data in some sort of storages, or passes it to some other bolt. 

# How can I use Storm on my computer?

## Installation Process:

(We used "Ubuntu VirtualBox" for this project)
1. Install java for storm dependencies: 
```
    sudo apt-get install default-jdk
``` 
2. Download Zookeeper and Extract tar File:
```  
   wget http://apache.claz.org/zookeeper/zookeeper-3.4.11/zookeeper-3.4.11.tar.gz
   tar -zxf zookeeper-3.4.11.tar.gz
```   
3. Create configuration file and set all the parameters:
```   
   nano conf/zoo.cfg
   tickTime=2000
   dataDir=/home/kouys/zookeeper-3.4.11/data
   clientPort=2181
   initLimit=5
   syncLimit=2
```
4. Start ZooKeeper server:
```
    bin/zkServer.sh start
```   
5. Start CLI:
```
   bin/zkCli.sh
```   
   After executing the above command, we will be connected to the ZooKeeper server

6. Download Storm and Extract tar File
```
   wget http://apache.mirrors.hoobly.com/storm/apache-storm-1.1.1/apache-storm-1.1.1.tar.gz
   tar -xvf apache-storm-1.1.1.tar.gz
```
7. Edit Configuration File:
   
   Local Host
```
   nano conf/storm.yaml
   storm.zookeeper.servers:
   - "localhost"
   storm.local.dir: “/home/kouys/apache-storm-1.1.1/data”
   nimbus.host: "localhost"
   supervisor.slots.ports:
    - 6700
    - 6701
    - 6702
    - 6703
```  
   Storm Cluster
   - The main idea behind clustering storm is simply to have the ```conf/storm.yaml``` file replace localhost with IP address of the different components on the cluster.
   - Every worker node will also have storm installed and a similar set of ```conf/storm.yaml``` files setup.
```  
   storm.zookeeper.servers:
   - "10.216.93.44"
   storm.local.dir: “/home/jason/apache-storm-1.1.1/data”
   nimbus.host: "10.216.90.224"
   nimbus.seeds: ["10.216.93.44"]
   supervisor.slots.ports:
   - 6700
   - 6701
   - 6702
   - 6703
```
8. Start the Nimbus:
```
   bin/storm nimbus
```   
9. Start the Supervisor:
```
   bin/storm supervisor
```   
10. Start the UI:
```
   bin/storm ui
   ```  
   ![qq 20171219174135](https://user-images.githubusercontent.com/33636455/34182522-a16d2500-e4e4-11e7-9c3e-d9e32add520e.png)

# What can I do with Storm? - Storm Application 

We chose to implement a marketing tool using Storm that creates a real-time notification system which informs subscribed companies of new discussions about them. 

An overview of our topology is shown below:
```python
class WordCount(Topology):
	redditStream_spout = streamRedditSpout.spec()
	titleAnalysis_bolt = titleAnalysisBolt.spec(inputs = {
		redditStream_spout: Grouping.fields('redditTitle')}, par = 4)
	matchKeywords_bolt = matchKeywordsBolt.spec(inputs = {
		titleAnalysis_bolt: Grouping.fields('splitTitle')}, par = 2)
	notifyCompany_bolt = notifyCompanyBolt.spec(inputs = {
		matchKeywords_bolt: Grouping.fields('companyName')}, par = 2)
	storeData_bolt = storeDataBolt.spec(inputs = {
		matchKeywords_bolt: Grouping.fields('redditTitle')}, par = 1)
```

1. Streams new post on reddit in real-time.
  - Implemented “redditStream” as a spout
2. Categorize the post based on its title.
  - Implemented “titleAnalysis” as a bolt
3. Process data and decides if the subscribed companies are being discussed.
  - Implemented “matchKeywords”as a bolt
4.   Push notification sent to companies including post title and post link.
  - Implemented “notifyCompany” as a bolt
5.  Save the relevant data 
  - Implemented “storeData” as a bolt

## How to code a Storm Application - "Python Edition" featuring "Streamparse"

There is an awesome python package called [Streamparse](https://streamparse.readthedocs.io/en/stable/index.html),
it's dependency are "JDK", "lein" and of-course Apache-Storm

To install streamparse, simply use:
```
pip install streamparse
```
*one thing to note, you should place storm into system path, so it can be reached by streamparse.*

Once this is setup and installed let's get into coding.
We saw earlier the idea behind topology, bolts and spouts, now we will look at how to implement it in code.

### First we have the topology:
```python
from streamparse import Grouping, Topology
```
Import methods from the streamparse class: Grouping and Topology.
Grouping is the way in which storm determines how to distrubute the data. We have:
- Shuffle grouping: Tuples are randomly distributed across the bolt’s tasks in a way such that each bolt is guaranteed to get an equal number of tuples. This is the default grouping if no other is specified.
- Fields grouping: The stream is partitioned by the fields specified in the grouping. For example, if the stream is grouped by the “user-id” field, tuples with the same “user-id” will always go to the same task, but tuples with different “user-id”’s may go to different tasks.

### Then we have to import bolts and spouts into our topology:
```python
from bolts.titleAnalysis import titleAnalysisBolt
from bolts.matchKeywords import matchKeywordsBolt
from spouts.redditStream import streamRedditSpout
```

### Finally we have to setup the topology:
- First, we create a class object that takes Topology as a paramenter
- Then we specify the flow of data (Tuples), the grouping and ```par = 2``` which is the number of parallel processes each bolt will be run on.
- Data will always start from a Spout, but bolts can also get data from other bolts.
```python
class redditProject(Topology):
	redditStream_spout = streamRedditSpout.spec()
	titleAnalysis_bolt = titleAnalysisBolt.spec(inputs = {
		redditStream_spout: Grouping.fields('redditTitle')}, par = 4)
	matchKeywords_bolt = matchKeywordsBolt.spec(inputs = {
		titleAnalysis_bolt: Grouping.fields('splitTitle')}, par = 2)
```

### Now let's move onto the Spout:
```python
from streamparse.spout import Spout
```
- After importing the Spout method from streamparse, we create a Spout class object, that takes Spout as a paramenter
- We must also declare the output Tuples of the Spout:
```python
class streamRedditSpout(Spout):
    outputs = ['redditTitle', 'redditLink']
```
### Once the class is setup, two critical methods are called and implemented:
- ```def initialize(self, stormconf, context):```, where you setup the parameter for the next method ```next_tuple```, 
*do not make the same mistake I did by think this is where you setup your initial data stream structure, it can be used simply for a basic generator that can looped later*
- ```def next_tuple(self):```, is where you would iterate through the stream of data that is coming from your generator. We send the data to the bolts by: ```self.emit([redditTitle, redditLink])```
- Two other methods are called too ```def ack(self, tup_id):``` and ```def fail(self, tup_id):```, these are mostly used for error handling, and some basic error is already predefined for you, however if you would like to further customize it, feel free to do so.

### Finally we move onto the Bolt:
```python
from streamparse import Bolt
```
- Bolts are pretty straight forward, it's where you process the tuples that come from your Spouts.
- Once we import the Bolt method from streamparse, we create the Bolt class object, that takes Bolt as a parameter
- For the outputs, it is up to you if want there to be any, since some bolts simply handle a process while others may need to pass tuples onto another bolt.
```python
class titleAnalysisBolt(Bolt):
    outputs = ['redditTitle', 'redditLink']
```
- Then we create the ```def process(self, tup):``` method with an input parameter of tup. This is the data that may have come from a Spout or Bolt. 
- We extract the tuple by: ```variable = tup.values[0]```
- Here since output is opional based on design, so is ```self.emit()```.

*That wraps it up. Thank you for reading, and happy coding!*

# Reference
1] (https://hortonworks.com/apache/storm/)
2] "A Storm is coming: more details and plans for release". Engineering Blog. Twitter Inc. Retrieved 29 July 2015.
3] (https://hortonworks.com/apache/storm/#section_4)
4] (http://storm.apache.org/releases/current/Tutorial.html)
5] (http://storm.apache.org/releases/current/Tutorial.html)
6] (https://www.youtube.com/watch?v=E25MGixBlBI)
7] (http://streamparse.readthedocs.io/en/stable/quickstart.html)










