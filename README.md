ORDER OF OPERATIONS

1. scan in a large corpus
2. tokenize the sentences in it
3. extract the syllable count for each token

3. construct a "frame" from that corpus -- a list of integers that represent how many syllables each token has

4. scan some data source for sentences
5. get syllable count for each sentence
6. create a hash (dict in python?) where keys are syllable count and values are each sentence matching that syllable count
7. iterate through the list and substitute a random matching data source