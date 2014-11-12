from nltk.corpus import cmudict
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
import random
d = cmudict.dict()

def nsyl_sent(sentence):
  nsyl = 0
  tokens = word_tokenize(sentence)
  for t in tokens:
    if t.lower() in d:
      word_syl = [len(list(y for y in x if y[-1].isdigit())) for x in d[t.lower()]]
      nsyl += word_syl[0]
  return nsyl

def syl_frame(text):
  syllable_counts = []
  tokens = sent_tokenize(text)
  for t in tokens:
    syllable_counts.append(nsyl_sent(t))
  return syllable_counts

def build_syl_dict(text):
  syl_dict = {}
  sent_tokens = sent_tokenize(text)
  for sent in sent_tokens:
    count = nsyl_sent(sent)
    if count in syl_dict:
      syl_dict[count].append(sent)
    else:
      syl_dict[count] = [sent]
  return syl_dict

def merge_syl_dicts(target, addition):
  for integer in addition:
    if integer in target:
      target[integer].extend(addition[integer])
    else:
      target[integer] = addition[integer]
  return target

def construct_corpora_syl_dict(corpora):
  first_dict = None
  for c in corpora:
    f = open(c, 'r')
    contents = f.read()
    syl_dict = build_syl_dict(contents)
    if first_dict is None:
      first_dict = syl_dict
    else:
      first_dict = merge_syl_dicts(first_dict, syl_dict)
  return first_dict

def build_to_frame(frame, corpus):
  build = []
  for nsyl in frame:
    if nsyl in corpus:
      ran_sen = random.choice(corpus[nsyl])
      build.append(ran_sen)
    else:
      print('MISSING SYL COUNT ' + str(nsyl))
  return build

def main(argv):
  opts, args = getopt.getopt(argv, "")

if __name__ == "__main__":
  main(sys.argv([1:]))

# Set up frame
f = open('frame.txt', 'r')
text = f.read()
f.close()
frame = syl_frame(text)

# Load corpora
corpora = [
  'corpora/Art.txt',
  'corpora/AskReddit.txt',
  'corpora/bestof.txt',
  'corpora/books.txt',
  'corpora/dataisbeautiful.txt',
  'corpora/explainlikeimfive.txt',
  'corpora/HistoryPorn.txt',
  'corpora/interestingasfuck.txt',
  'corpora/mildlyinfuriating.txt',
  'corpora/nottheonion.txt',
  'corpora/relationships.txt',
  'corpora/science.txt',
  'corpora/Showerthoughts.txt',
  'corpora/space.txt',
  'corpora/tifu.txt'
]
united_corpus = construct_corpora_syl_dict(corpora)

# Build corpora against frame
framed = build_to_frame(frame, united_corpus)

f = open('result.txt', 'w')
f.write(' '.join(framed))
f.close()