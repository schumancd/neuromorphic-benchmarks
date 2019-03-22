# Network of Oscillators

In this task, we construct a frequency oscillator consisting of recurrent loops. This task serves as an interesting method to examine characteristics of differing systems because the activity pattern within the oscillator may be matched across varying hardware implementations.

We use a small network of 4-stage oscillators that are tiled in a 5x5 arrangement:


Oscillators in a row are chained together with one intermediate neuron between each. Each neuron should have a low threshold and each synapse should have a strong enough positive weight that it can trigger its post-synaptic neuron to fire. Delays (synaptic and/or neuronal) should be such that, once stimulated, one neuron in each 4-stage oscillator should fire every time step.  With a network of this structure, a single input spike should be applied on each input neuron at time 0.  The task is to generate 10 spikes on each output neuron; in particular, once the first output fire occurs, the remaining output fires should occur every fourth time step. 

