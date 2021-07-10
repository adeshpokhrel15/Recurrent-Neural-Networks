# Recurrent-Neural-Networks <br>
RNNs introduce state variables to store past information, together with the current inputs, to determine the current outputs.RNNs are designed to better handle sequential information. Many of the examples for using recurrent networks are based on text data.

### 1. Sequence Models <br>
There is quite a difference in difficulty between interpolation and extrapolation. Consequently, if you have a sequence, always respect the temporal order of the data when training, i.e., never train on future data. Sequence models require specialized statistical tools for estimation. Two popular choices are autoregressive models and latent-variable autoregressive models. For causal models (e.g., time going forward), estimating the forward direction is typically a lot easier than the reverse direction. For an observed sequence up to time step  t , its predicted output at time step  t+k  is the  k -step-ahead prediction. As we predict further in time by increasing  k , the errors accumulate and the quality of the prediction degrades, often dramatically.

### 2. Text Preprocessing <br>
Text Preprocessing is the process of bringing the text into a form that is predictable and analyzable for a specific task. A task is the combination of approach and domain. For example, extracting top keywords with TF-IDF (approach) from Tweets (domain) is an example of a task. Following steps is done in text preprocessing: <br>

<li>Load text as strings into memory.

<li>Split strings into tokens (e.g., words and characters).

<li>Build a table of vocabulary to map the split tokens to numerical indices.

<li>Convert text into sequences of numerical indices so they can be manipulated by models easily.

