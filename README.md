# Google Hash Code 2019
## About
This repo contains the Python code written to compete in Google's Hash Code 2019 team coding competition. The coding challenge is described in the file challenge.pdf document. Various solutions that were taken are described below.

## Solutions
Various approaches were taken to solve the challenge based on data analysis of the various features of the provided input datasets: length, vocab size, image type, etc. Determined features of the data are located in the analysis.txt file.

### One-Hot Vectors
This approach takes its inspiration from a common NLP machine learning approach of using one hot vectors to represent words. This solution first involved creating a bag-of-words representation of the entire vocab of image tags for a given dataset and then creating a one hot vector for each image in the data set in which each tag corresponds to a 1 in the vector. Effectively if the vocab size was 50, each image would have a 50 size length vector filled in with 0s with inactive tags and 1s for the active tags. This solution involves matrix multiplying the vector representation of each image with a matrix made up of the vectors for all other images in the dataset. The output is then sorted to determine the middle point of similarity and dissimilarity to create the most "interesting" slideshow order as described in the challenge.pdf document.

### Tag Length
This approach makes use of the fact that certain datasets have low vocabulary size. The solution is to match images solely based on the number of tags that each poses.

### Vertical Tag Length
This approach is an extension of the Tag Length approach but first pairs adjacent vertical images together.

### Intersect
This approach makes use of the fact that many of the datasets have a large number of photos. The approach merely tries to achieve a score of at least 1 point per image in the datasets by matching images based on having at least 1 common tag.