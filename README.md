# Pic2NewickTree
This is a research collaboration between Luna (B. O'Meara lab, Ecology Evolutionary Biology Department, UTK) and Moon (Computational Biology Lab, UTK).

## Final product
A database for managing and retrieving published phylogenetic trees. To this aim, several steps are needed:

1. A collection of candidate publications (in PDF format) with phylogenetic tree figures.
2.1 All figures are identified, cropped out from the original paper and converted into picture in a unified format(PNG).
2.2 Figures with no phylogenetic trees are discarded.
3. Information from tree images is extracted and stored into a computer-readable format (Newick).
4. All the above information is organized into a database.

![pic2newickerdiagram](https://user-images.githubusercontent.com/20075487/45761609-92911580-bbfa-11e8-993d-b955037f0d7b.png)

## Approach A: Manually-engineered steps for pictures with standard presentations
### design phase
1. synthesize data
2. design model (attention mechanism with simple filters)
3. test accuracy on synthesized data

### test phase
(0. label data manually)
1. test accuracy on real data
2. analyze error case by case
3. add variations to the model

### evaluate prediction confidence
***the evaluation of prediction accuracy for unlabeled data is needed so that we can pick out problematic pictures and manually improve the database.***

1. find out features which prediction performence is sensitive to (***for example, to predict age of a person, it's easier to tell if the person is a female rather than male. Another example, it's easier to predict nationality between Chinese and British, but harder between Chinese and Japanese***)
2. design a specific model for the above features
3. softmax and cross-entropy may be helpful to evaluate the prediction confidence
4. comparing the unsupervised clustering results of raw picutures and the extracted code or generated pictures might be helpful

## Approach B: Deep learning model with standard presentations
Deep learning method for this project is mainly based on image caption architecture which is a hybrid between CNN (convolutional neural network) for image feature extraction and RNN (recurrent neural network) for generating language which is newick code here.

### acquire data
(0. same labeled data)
1. list of candidate papers
2. number of phylogenetic tree figures in each candidate paper
3. coordinates and size of each figure (x, y, h, w)
4. list of extracted images

### model construction
1. preprocess data: get grayscale and extract species names with 100% accuracy
2.1 build architecture
2.2 design cost function
3. train and fine tune

### presentation
1. generate standard pictures with predicted newick code
