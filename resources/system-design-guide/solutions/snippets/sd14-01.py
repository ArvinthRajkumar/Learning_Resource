from collections import defaultdict
followers = {"alice": ["bob", "carol"], "star": ["bob", "carol", "dave"]}
CELEB = 2                       # followers above this count are not pushed
feeds = defaultdict(list)       # precomputed feed list per user (post ids, newest last)
posts, celeb_posts = {}, defaultdict(list)

def post(author, pid, ts):
    posts[pid] = (author, ts)
    if len(followers.get(author, [])) > CELEB:
        celeb_posts[author].append(pid)          # pull later
    else:
        for f in followers.get(author, []):
            feeds[f].append(pid)                 # push now

def read_feed(user, follows_celebs):
    ids = list(feeds[user])
    for c in follows_celebs:
        ids += celeb_posts[c]
    return sorted(ids, key=lambda p: -posts[p][1])

post("alice", "p1", 1); post("star", "p2", 2); post("alice", "p3", 3)
print(read_feed("bob", ["star"]))
