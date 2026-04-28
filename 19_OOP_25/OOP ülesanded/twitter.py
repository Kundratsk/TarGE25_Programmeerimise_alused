"""Twitter algorithm implementations."""


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets

    def __repr__(self):
        """
        Tweet representation.

        :return: Tweet representation.
        """
        return f"{self.user} ({self.retweets} retweets)"


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    """
    if not tweets:
        return None

    # Kasutame max() funktsiooni, et leida kiireim jagatise põhjal
    return max(tweets, key=lambda t: t.retweets / t.time)


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet (smaller time) is the more popular one.
    """
    if not tweets:
        return []

    # -tweet.retweets sorteerib kahanemise järjekorras
    # tweet.time sorteerib kasvamise järjekorras (väiksem/uuem aeg ettepoole)
    return sorted(tweets, key=lambda t: (-t.retweets, t.time))


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.
    """
    if not tweets:
        return []

    filtered_tweets = []
    for tweet in tweets:
        # Jagame sisu tühikute põhjal ja kontrollime, kas hashtag on listis olemas
        # See on kindlam kui split()[-1], juhuks kui hashtag pole päris viimane
        if hashtag in tweet.content.split():
            filtered_tweets.append(tweet)

    return filtered_tweets


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z.
    """
    if not tweets:
        return []

    # 1. Kogume kokku hashtagid ja nende summaarsed retweetid
    hashtag_data = {}
    for tweet in tweets:
        words = tweet.content.split()
        for word in words:
            if word.startswith('#'):
                if word not in hashtag_data:
                    hashtag_data[word] = 0
                hashtag_data[word] += tweet.retweets

    # 2. Sorteerime võtmed
    # -hashtag_data[h] -> populaarsus kahanemas
    # h -> tähestik kasvamas (A-Z)
    return sorted(hashtag_data.keys(), key=lambda h: (-hashtag_data[h], h))


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    # Testime kiireimat kasvu
    print(f"Fastest growing: {find_fastest_growing(tweets).user}")  # -> @elonmusk

    # Testime populaarsust
    sorted_p = sort_by_popularity(tweets)
    print(f"Most popular: {sorted_p[0].user}")  # -> @CIA

    # Testime hashtagide populaarsust
    print(f"Sorted hashtags: {sort_hashtags_by_popularity(tweets)}")
    # -> ['#heart', '#bigsmart'] (Sest heartil on 284k ja bigsmartil 54k+166k=220k)
