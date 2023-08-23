def get_words_more_than_once(sentence):
    sentence = sentence.lower() # convert to lowercase
    sentence = sentence.replace('.', '') # remove full stops
    words = sentence.split() # split into words

    mydict ={i:words.count(i) for i in words}

    return(mydict)
    # returns the dictionary with the words that appear more than once in the sentence


sentence = '''
Once upon a time in a small town, there lived a mischievous little cat named Whiskers. Whiskers had a fluffy white coat with adorable black patches on his ears and a tiny pink nose that twitched with curiosity. He loved exploring the neighborhood and was known for his playful antics.

One sunny morning, Whiskers discovered a hidden garden filled with vibrant flowers and enchanting butterflies. The garden was a secret paradise for all the cats in the town. Whiskers couldn't believe his luck! He spent his days chasing butterflies and basking in the warm sunlight.

One afternoon, as Whiskers napped under a shady tree, he noticed a shy little kitten peeking out from behind a bush. The kitten had a soft gray coat and bright green eyes that sparkled with innocence. Whiskers approached the kitten with a friendly purr.

The kitten introduced herself as Lily, and she had just moved to the town with her human family. She was nervous about making new friends, but Whiskers reassured her with his warm purrs and playful demeanor. They became fast friends and spent hours exploring the garden together.

As time went by, Whiskers and Lily's friendship grew stronger. They became inseparable, always on new adventures, from climbing trees to chasing shadows. They even had their secret hideout in an old shed filled with cushions and toys.

Their playful escapades brought joy to the entire neighborhood. Children would gather to watch Whiskers and Lily perform acrobatic jumps and chase their tails. The cats had become local celebrities, spreading laughter and smiles wherever they went.

One rainy day, Whiskers and Lily sat by the window, watching the raindrops dance on the glass. They longed for some excitement, even in the gloomy weather. Whiskers had an idea and dashed away, only to return moments later with a ball of yarn.

They batted the yarn back and forth, turning their little corner of the house into a fun-filled playground. The rainy day turned into a memorable adventure filled with laughter and cheer. Whiskers and Lily realized that as long as they were together, even the rainiest days could be delightful.

As the years went by, Whiskers and Lily remained the best of friends. They grew older and wiser, but their playful spirits never faded. They continued to explore the town, bringing joy to everyone they encountered.

Their story of friendship and mischief became a legend, passed down from one generation of cats to another. Whiskers and Lily's bond reminded everyone that true friendship knows no boundaries and that life is always more enjoyable when shared with someone special.

And so, the mischievous adventures of Whiskers and Lily continued, spreading love, happiness, and countless smiles to all who crossed their path. They taught the world that even the tiniest creatures can leave the biggest pawprints on our hearts.
'''

count = get_words_more_than_once(sentence)
print("These are the words that appear more than once in the paragraph: ")
for i in count:
    print('word: ', i, ' count: ', count[i])