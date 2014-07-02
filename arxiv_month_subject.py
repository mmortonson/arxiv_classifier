"""
query arXiv API to get metadata for all articles
from a single month (based on date submitted) 
and subject class

based on example code at 
http://arxiv.org/help/api/examples/python_arXiv_parsing_example.txt
and
http://arxiv.org/help/api/examples/python_arXiv_paging_example.txt
"""

import time
import urllib
import feedparser

"""
full query example:
http://export.arxiv.org/api/query?search_query=all:1401+AND+cat:astro-ph.CO&start=20&max_results=20
"""

base_url = 'http://export.arxiv.org/api/query?'

# month and subject class
# >> make these command line arguments
month = '1402' # YYMM format
# add check against full subject list or choose subject from menu
subject = 'astro-ph.CO'
#subject = 'cond-mat.mtrl-sci'
max_results = 100
# >> make optional command line arg. for output
output_file = month + '.' + subject + '.' + \
    str(max_results) + '.txt'

writer = open(output_file, 'w')
writer.write('# ' + subject + '\n# ' + month + '\n')

search_query = 'all:' + month + '+AND+cat:' + subject
results_per_page = 20 # increase this?
wait_time = 3 # time between requests in seconds

print 'Searching for articles from month ' + month + \
    ' in subject class ' + subject

for i in range(0, max_results, results_per_page):
    print 'Results {0:d}-{1:d}:'.format(i+1, i+results_per_page)
    query_format = 'search_query={0:s}&start={1:d}&max_results={2:d}'
    query = query_format.format(search_query, i, results_per_page)
    
    # GET request to arXiv API
    response = urllib.urlopen(base_url + query).read()

    # parse response
    feed = feedparser.parse(response)
    if len(feed.entries) == 0:
        print 'No results found.'
        break
    for entry in feed.entries:
        id = entry.id.split('/abs/')[-1]
        id_month = id.split('.')[0]
        primary_subject = entry.tags[0]['term']
        if id_month == month and primary_subject == subject:
            title_and_abstract = ' '.join(entry.title.split('\n') + 
                entry.summary.split('\n')).encode('UTF-8')
            print title_and_abstract + '\n'
            writer.write(title_and_abstract + '\n')

    # wait before calling the API again
    if i+results_per_page < max_results:
        print 'Waiting {0:d} seconds...'.format(wait_time)
        time.sleep(wait_time)

writer.close()
