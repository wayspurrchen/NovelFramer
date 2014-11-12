import praw

subreddits = [
	'AskReddit',
	'relationships',
	'Showerthoughts',
	'science',
	'tifu',
	'explainlikeimfive',
	'interestingasfuck',
	'HistoryPorn',
	'bestof',
	'space',
	'dataisbeautiful',
	'nottheonion',
	'mildlyinfuriating',
	'books',
	'Art'
]

r = praw.Reddit(user_agent='wayspurrchen_nanogenmo')

for sr in subreddits:
	print('Crawling ' + sr + '...')
	sub = r.get_subreddit(sr)
	sub_comments = []
	threads = sub.get_hot(limit=10)
	for t in threads:
		cmnts = praw.helpers.flatten_tree(t.comments)
		# Get only highly voted comments
		comments = [el.body for el in cmnts if hasattr(el, 'score') and el.score > 100]
		sub_comments.extend(comments)
	f = open('corpora/' + sr + '.txt', 'w')
	f.write(' '.join(sub_comments))
	f.close()

# print([str(x) for x in submissions])