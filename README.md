# Channel Processor
A Python based implementation of a flexible and generic channel processing system processing channel data based on predefined functions to augment measured data and to calculate metrics to understand the performance of a car. The system has a mechanism for reading and writing channels and metrics, and a mechanism for reading parameters. The functions that process the channel data have the form outputs = function(parameters, inputs).

Based on the functions defined in the next section and the provided `channels.txt` and `parameters.txt` input files, the program calculates and prints the value of the metric _**`b`**_. From the  files provided, what is the value of the metric _**`b`**_?

## Function Definitions
### Function 1: 
  - _`Y = mX + c`_
### Function 2: 
  - _`B = A + Y`_
  - _`b = mean(B)`_
### Function 3:
  - _`A = 1 / X`_
### Function 4:
  - _`C = X + b`_

## Channels, Metrics and Parameters
Channels are arrays of data and are denoted with a capital letter, e.g. _**`Y`**_.  Metrics and parameters are scalars and are denoted with a lowercase letter, e.g. _**`m`**_.  Note that b is the only metric in the above example.  _**`X`**_, _**`m`**_ and _**`c`**_ are known.
