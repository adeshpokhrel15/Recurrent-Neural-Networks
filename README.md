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
  
 ### 3. Language Models <br>
Language models are key to natural language processing. n -grams provide a convenient model for dealing with long sequences by truncating the dependence. Long sequences suffer from the problem that they occur very rarely or never. There is a lot of structure but not enough frequency to deal with infrequent word combinations efficiently via Laplace smoothing. The main choices for reading long sequences are random sampling and sequential partitioning. The latter can ensure that the subsequences from two adjacent minibatches during iteration are adjacent on the original sequence.

### 4. Recurrent Neural Networks from Scratch <br>
We can train an RNN-based character-level language model to generate text following the user-provided text prefix. A simple RNN language model consists of input encoding, RNN modeling, and output generation. RNN models need state initialization for training, though random sampling and sequential partitioning use different ways. When using sequential partitioning, we need to detach the gradient to reduce computational cost. A warm-up period allows a model to update itself (e.g., obtain a better hidden state than its initialized value) before making any prediction.

### 5.  Concise Implementation of Recurrent Neural Networks <br>
 High-level APIs of the deep learning framework provides an implementation of the RNN layer. The RNN layer of high-level APIs returns an output and an updated hidden state, where the output does not involve output layer computation. Using high-level APIs leads to faster RNN training than using its implementation from scratch.
 
### 6. Backpropagation Through Time <br>
Backpropagation through time is merely an application of backpropagation to sequence models with a hidden state. Truncation is needed for computational convenience and numerical stability, such as regular truncation and randomized truncation. High powers of matrices can lead to divergent or vanishing eigenvalues. This manifests itself in the form of exploding or vanishing gradients. For efficient computation, intermediate values are cached during backpropagation through time.
  
### 7.Gated Recurrent Units (GRU) <br>
Gated RNNs can better capture dependencies for sequences with large time step distances. Reset gates help capture short-term dependencies in sequences. Update gates help capture long-term dependencies in sequences. GRUs contain basic RNNs as their extreme case whenever the reset gate is switched on. They can also skip subsequences by turning on the update gate.
  
### 8. Long Short-Term Memory (LSTM) <br>
LSTMs have three types of gates: input gates, forget gates, and output gates that control the flow of information. The hidden layer output of LSTM includes the hidden state and the memory cell. Only the hidden state is passed into the output layer. The memory cell is entirely internal. LSTMs can alleviate vanishing and exploding gradients.
  
### 9. Deep Recurrent Neural Networks <br>
  In deep RNNs, the hidden state information is passed to the next time step of the current layer and the current time step of the next layer.There exist many different flavors of deep RNNs, such as LSTMs, GRUs, or vanilla RNNs. Conveniently these models are all available as parts of the high-level APIs of deep learning frameworks.Initialization of models requires care. Overall, deep RNNs require considerable amount of work (such as learning rate and clipping) to ensure proper convergence.
                                                               

