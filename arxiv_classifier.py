from textblob.classifiers import NaiveBayesClassifier
import codecs

training_month = '1401'
test_month = '1402'

# currently coded for only 2 subjects (see n_train loop)
subjects = ['astro-ph.CO', 'astro-ph.GA']

for month in [training_month, test_month]:
    documents = []
    correct_subjects = []
    n_per_class = []

    for i_s, s in enumerate(subjects):
        reader = codecs.open(training_month + '.' + s + '.100.txt',
            'r', 'utf-8')
        new_documents = reader.readlines()[2:]
        documents += new_documents
        n_per_class.append(len(new_documents))
        #correct_subjects += len(new_documents)*(s + ' ').split()
        correct_subjects += len(new_documents)*[i_s]

    set = zip(documents, correct_subjects)
    if month == training_month:
        full_training_set = set
    else:
        test_set = set

training_set = []
for n_train in range(10, 40, 10):
    # >> would be faster to add training data to the classifier
    # >> instead of retraining on all samples each iteration
    print 'Training classifier with {0:d} examples...'.format( \
        2*n_train)
    new_training_data = full_training_set[0:n_train] + \
        full_training_set[n_per_class[0]:n_per_class[0]+n_train]
    if len(training_set) == 0:
        cl = NaiveBayesClassifier(new_training_data)
    else:
        cl.update(new_training_data)
    training_set += new_training_data
    print 'train accuracy: {0:f}, test accuracy: {1:f}'.format(
        cl.accuracy(training_set), cl.accuracy(test_set))

cl.show_informative_features(30)
print '\nKey:'
for i_s, s in enumerate(subjects):
    print str(i_s) + ': ' + s

