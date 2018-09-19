# Pic2NewickTree
This is a research collaboration between Luna(Ecology Evolutionary Biology Lab, UTK) and Moon(Computational Biology Lab, UTK).

## Final product
A database for managing and retireveing published phylogenetic tree. To this aim, several steps will be done:

1. A collection of candidate publications(PDF) with phylogenetic tree figures.
2. All figures are identified, cropped out from the original paper and converted into picture in a unified format(PNG).
3. All tree images need to be converted into a coding format(Newick).
4. All the above informations are organized into a database.

![pic2newickerdiagram](https://user-images.githubusercontent.com/20075487/45761609-92911580-bbfa-11e8-993d-b955037f0d7b.png)

## Approche A: Manually-engineered steps for pictures with standard presentations
### design phase
1. synthesize data
2. design model (attention mechanism with simple filters)
3. test accuracy on synthesized data

### test phase
(0. label data manually)
1. test accurcy on real data
2. analyze error case by case
3. add variations to the model

### evaluate prediction confidence
***the evaluation of prediction accuracy for unlabel data is needed so that we can pick out those problematic pictures and improve the database mannully.***

1. find out features that prediction performence are sensitive to (***for example, to predict age of a person, it's easier to tell if the person is a female rather than male. Another example, it's easier to predict between Chinese and British, but harder for Chinese and Japanese***)
2. design model specific for the above features
3. softmax and cross-entropy may be helpful to evaluate the prediction confidence
4. compare the unsupervised clustering results of raw picutures and extracted code or generated pictures may be helpful

## Approche B: Deep learning model with standard presentations
Deep learning method for this project is mainly based on image caption archetecture which is a hybrid betwee CNN(convolutional neural network) for image feature extraction and a RNN(recurrent neural network) for generating language which is newick code here. 

### acquire data
(0. same labeled data)
1. list of candidate papers
2. number of phylogenetic tree figures in each candidate paper
3. coordinates and size of each figure (x, y, h, w)
4. list of extracted images

### model construction
1. preprocess data: get grayscale and extract species names with 100% accuracy
2.1 build archetecture
2.2 design cost function
3. train and fine tune

### presentation
1. generate standard pictures with predicted newick code
