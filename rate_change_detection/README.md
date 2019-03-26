# Rate Change Detection

 A similar version of this task is described in detail by [Schuman, et al](http://neuromorphic.eecs.utk.edu/publications/2013-06-10-variable-structure-dynamic-artificial-neural-networks/). For this task, the goal of the spiking neuromorphic system is to detect when a substantial change in the arrival of spikes has occurred.  This task relates to potential applications in network traffic analysis, where one may want to monitor patterns in packet arrival rates.  We specify as the training set 60 random traffic patterns, each of which occurs over the course of 10,000 time steps with labeled points where the rate changes occur. We specify another 40 random traffic patterns as the testing set.  Both the training and testing sets are available in this repository.  Each of the training and testing instances are in a particular format:  

```
# HEADER
# syntax: header number_of_event_types number_of_attributes_per_record number_of_records
header 2 1 10001

# EVENT TYPES
# syntax: event_info event_id string_describing_event
# note: event_info 0 is reserved to represent normal data
event_info 1 increased_rate
event_info 2 decreased_rate

# ATTRIBUTE INFORMATION
# syntax: attribute_info attribute_index min_value max_value string_describing_attribute
attribute_info 0 0 1 magnitude

# EVENTS
# syntax: event event_id start_time stop_time
event 1 371 471
event 2 869 969
event 1 1090 1190
event 2 1533 1633
event 1 2181 2281
...
...
...
# RECORDS
# syntax: rec time(sec) attribute0_value attribute1_value 
rec 0 0
rec 1 0
rec 2 0
rec 3 0
rec 4 0
rec 5 0
...
```

In this example, we have two events types, `increased_rate` (type 1) and `decreased_rate` (type 2).  When the events are specified, the type of the event is specified (type 1 -- increasing and type 2 -- decreasing), and the time the event starts is also specified (when the rate increases or decreases).  We allow that the neuromorphic detector must report the change in rate of arrival within 100 time steps, and must specify that the rate change either increased or decreased.  Because we allow for a 100 time step window to detect the event, the event "starts" at the real start time and "ends" 100 time steps later.   

Rather than specifying a specific time value associated with the time step (e.g., milliseconds, seconds, etc.), we leave it in time step units to accommodate neuromorphic implementations with different clock rates.

## Metrics to Report

When reporting results for this task, the following metrics should be reported:
- True positive rate (number of true positives over total number of rate changes) on the training set.
- False discovery rate (number of false positives over sum of false positives and true positives) on the training set.
- Missed detection rate (number of missed detections over total number of rate changes) on the training set.
- True positive rate on the testing set.
- False discovery rate on the testing set.
- Missed detection rate on the testing set.
- Average energy per random traffic pattern on the testing set
