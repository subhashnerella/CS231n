import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  
  for i in range(X.shape[0]):
    margin = X[i].dot(W)
    margin -= np.max(margin)
    p = lambda k: np.exp(margin[k]) / np.sum(np.exp(margin))
    loss += -np.log(p(y[i]))
    for j in range(W.shape[1]):
        dW[:,j]+= X[i]*(p(j)-(j==y[i]))
  loss/=X.shape[0]
  loss += 0.5*reg*np.sum(W*W)
  dW/=X.shape[0]
  dW += reg*W
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  margin = X.dot(W)
  margin -= np.max(margin,axis =1,keepdims=True)
  margin = np.exp(margin)
  margin = margin/np.sum(margin,axis=1,keepdims=True)
  correct = margin[np.arange(X.shape[0]),y]
  loss = np.sum(-np.log(correct))
  loss/=X.shape[0]
  loss += 0.5*reg*np.sum(W*W)
  margin[np.arange(X.shape[0]),y]-=1
  dW = X.T.dot(margin)
  dW/=X.shape[0]
  dW += reg*W
  
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

