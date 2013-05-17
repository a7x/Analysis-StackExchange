def getUserInfo(elem):
    ''' id, upvotes, downvotes, views, reputation
    '''
    return (getId(elem), getupvotes(elem), getdownvotes(elem), getViews(elem),\
    getReputation(elem))

def getViews(elem):
    return elem.get("Views")

def getAcceptedId(elem):
    return elem.get("AcceptedAnswerId")

def getReputation(elem):
    return elem.get("Reputation")

def getId(elem):
    return elem.get("Id")

def getCreationDate(elem):
    return elem.get("CreationDate")

def getParent(elem):
    return elem.get("ParentId")

def getPostTypeId(elem):
    return elem.get("PostTypeId")

def getOwner(elem):
    return elem.get("OwnerUserId")

def getViewCount(elem):
    return elem.get("ViewCount")

def getupvotes(elem):
    return elem.get("UpVotes")

def getdownvotes(elem):
    return elem.get("DownVotes")

def getTitle(elem):
    return elem.get("Title")

def getBody(elem):
    return elem.get("Body")

def getScore(elem):
    return elem.get("Score")

def getFavoriteCount(elem):
    return elem.get("FavoriteCount")

def getCommentCount(elem):
    return elem.get("CommentCount")

def getAnswerCount(elem):
    return elem.get("AnswerCount")

def getTags(elem):
    return elem.get("Tags")

def clearElem(elem):
    elem.clear()
    if elem.getprevious() is not None:
        del elem.getparent()[0]
