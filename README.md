# NovelFramer - [NaNoGenMo 2014](https://github.com/dariusk/NaNoGenMo-2014)

Working repository for my NaNoGenMo 2014 project.

This script "frames" a piece of text by counting the syllables in each sentence and constructing a list of those syllable counts. Then it skims a variety of reddit subreddits for comments and matches sentences with the same syllables into the "syllable frame".

## Input frame

This sentence has five words. Here are five more words. Five-word sentences are fine. But several together become monotonous. Listen to what is happening. The writing is getting boring. The sound of it drones. Itâ€™s like a stuck record. The ear demands some variety. Now listen. I vary the sentence length, and I create music. Music. The writing sings. It has a pleasant rhythm, a lilt, a harmony. I use short sentences. And I use sentences of medium length. And sometimes, when I am certain the reader is rested, I will engage him with a sentence of considerable length, a sentence that burns with energy and builds with all the impetus of a crescendo, the roll of the drums, the crash of the cymbalsâ€“sounds that say listen to this, it is important.

## Output content:

Damn, I still love that song. He currently outranks me. Well, almost no one. Sure, women retire earlier in most countries. Edit #2: No, you can't eat with your butthole. I am freaking LOSING IT, MAN! 2D does this much better. -  Brought his own aces. Why does a minor quirk of pronounciation matter? Yes, my dear Redittors. When the lost ones show up I put them back in the tin. This sucks. "Where's Steward." We rip our masks off and breath in that sweet hookah from hell. Washingtonian here. No joy, no crying, no anger, no nothing. What's an even bigger mystery to me is that his wife now is one of the prettiest blondes I have ever seen (not only was he dumber than a rusty bucket, he also had a face only his mother could love), and what's worse is that he has been passing on his genes with her.

# Order of Operations

1. scan in a large corpus
2. tokenize the sentences in it
3. extract the syllable count for each token
4. construct a "frame" from that corpus -- a list of integers that represent how many syllables each token has
5. scan some data source for sentences
6. get syllable count for each sentence
7. create a dict where keys are syllable count and values are each sentence matching that syllable count
8. iterate through the frame and substitute a random sentence with a matching syllable count