## Classification of arXiv papers using titles and abstracts

The general goal of this project is to automatically classify research 
articles by assigning them to one or more of 
the arXiv [1] subject categories. The training data consist 
of a collection of titles and abstracts from a representative sample of 
articles, downloaded using the arXiv API [2] (or, alternatively, one of the related services 
described at [3]).

### Questions

- Which classification methods provide the greatest accuracy for this problem?
- How many articles from each subject area are needed to train the classifier?
- How much does the date range of the training set matter (due to e.g. 
  changes in subjects being studied and terminology used over time)?
- Does additional article metadata such as the authors' names improve the 
  accuracy of the classification algorithm?
- Are certain subjects more difficult to identify than others?
- Is there any evidence that some of the existing arXiv subject classes are 
  either too narrowly defined (e.g. if articles from two different classes 
  tend to get grouped together often) or too broad (may need to use 
  unsupervised categorization to determine this)?

### Future extensions

- Experiment with unsupervised categorization of article abstracts, using 
  topic modeling methods like latent Dirichlet allocation. How closely do 
  the categories identified match up with the existing arXiv subject classes? 
  Does the analysis suggest a need for any new subject classes?
- Train the algorithm using full text from a selected set of articles [4] [5].
- Devise a measure of similarity between articles, and use this metric to 
  link articles together. Such a network could be useful for multiple 
  applications, e.g. suggesting new articles to read based on what a 
  researcher is currently reading, or helping authors and journal referees 
  identify articles that should have been cited by a new study but weren't.

[1]: http://arxiv.org/
[2]: http://arxiv.org/help/api/index
[3]: http://arxiv.org/help/bulk_data
[4]: http://www.cs.cornell.edu/projects/kddcup/datasets.html
[5]: http://arxiv.org/help/bulk_data_s3
