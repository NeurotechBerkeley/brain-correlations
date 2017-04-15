# Measuring attention using cross-brain correlations in a real setting

### Introduction
In this lab, we will measure correlations across brains, as a measure of
attention.  The idea is that, the more people pay attention to a stimulus, the
more their brain is driven by a stimulus and not their internal thoughts. If it
is driven by the stimulus, then brain signals across different sessions should be similar.

### Setup

First, install the libraries:
``` bash
cd recording
npm install
pip install -r requirements.txt
```

(If you don't have `npm`, you can install by running `brew install node`. You can get `brew` from https://brew.sh/)

### Time sync

To make sure the timestamps are synced across computers, run this to sync to Apple time servers: ``ntpdate -s time.apple.com`` 

### Stimulus Presentation + Recording

- Attach electrodes to participant's head, 2 on the frontal cortex (on forehead) and 2 on temporal lobe (right above the ears).
- Connect to the ganglion and stream data: `cd recording; node ganglion-lsl.js`
- Run lsl-viewer to check connections and stream: `cd recording; python lsl-viewer.py`
- Record data: `cd recording; python lsl-record.py`
- Stop recording data by pressing Control-C in the `lsl-record.py` script

### Analysis
...will come in time
