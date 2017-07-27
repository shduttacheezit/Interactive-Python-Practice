movieViewCounts = {}
moviesRanked = []

def rearrangeMovieArray():
    """Compare movies array in right order

        >>>movieViewCounts = {'A': 2, 'B': 3, 'C': 1, 'D': 4}
        >>>rearrangeMovieArray()
        >>>moviesRanked
        >>>['D', 'B', 'A', 'C']

    """
    # using lambda to sort by values of dict and return list 
    new_ranked= sorted(movieViewCounts, key=lambda v:movieViewCounts[v], reverse=True)
    moviesRanked = new_ranked

def viewedVideo(videoId):
    """Add count to movies viewed dictionary

        >>>viewedVideo('A')
        >>>viewedVideo('B')
        >>>viewedVideo('C')
        >>>viewedVideo('C')
        >>>movieViewCounts
        >>>{'A':1, 'B':1, 'C': 2}
        >>>moviesRanked
        >>>['C', 'A', 'B']

    """

    if videoId in movieViewCounts:
        movieViewCounts['videoId'] += 1
        rearrangeMovieArray()
    else:
        movieViewCounts[videoId] = movieViewCounts.get(videoId, 0) + 1
        moviesRanked.append(videoId)

def getRanking(videoId):
    """get ranking of movie by ID

        >>>moviesRanked = ['B', 'A', 'C']
        >>>getRanking('B')
        >>>1
        >>>getRanking('D')
        >>>Movie not found
        >>>getRanking('C')
        >>>3

    """

    if videoId in moviesRanked:
        print moviesRanked.index('videoId') + 1
    else:
        print 'Movie not found'

def getTopTen():
    """get first ten movies from ranked movies list

        >>>moviesRanked = ['B', 'A', 'C']
        >>>getTopTen()
        >>>['B', 'A', 'C']
        >>>moviesRanked = ['B', 'A', 'C', 'D', 'J', 'K', 'L', 'M', 'P', 'F', 'G', 'H']
        >>>['B', 'A', 'C', 'D', 'J', 'K', 'L', 'M', 'P', 'F']

    """

    if moviesRanked > 10:
        return moviesRanked[0:10]
    else: 
        return moviesRanked

