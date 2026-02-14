import requests
import json
import hashlib
import re
import random 


joke_url = "https://bootlegfish.pythonanywhere.com/api/random/joke"
quote_url = "https://bootlegfish.pythonanywhere.com/api/random/quote"
fish_url = "https://bootlegfish.pythonanywhere.com/api/random/fish"

def GetR(url):
	r = requests.get(url)
	return r.text, r.status_code

def joke():
	Joke, Status = GetR(joke_url)
	if 200 == Status:
		return str(Joke)
	else:
		return f"Error {Status} Unavailable To Get Joke"

def quote():
	Quote, Status = GetR(quote_url)
	if 200 == Status:
		return str(Quote)
	else:
		return f"Error {Status} Unavailable To Get Quote"

def fish():
	Fish, Status = GetR(fish_url)
	if 200 == Status:
		return str(Fish)
	else:
		return f"Error {Status} Unavailable To Get Quote"


meme_api = "https://meme-api.com/gimme"

def GetJson(url):
    r = requests.get(meme_api)
    return r.json()

def get_meme():
    try:
        r = requests.get(meme_api)
        r.raise_for_status()
        meme_data = r.json()
        if 'url' and 'title' in meme_data:
            meme_url = meme_data['url']
            meme_title = meme_data['title']
            return str(meme_url), str(meme_title)
    except requests.exceptions.HTTPError as http_err:
        return http_err
    except requests.exceptions.RequestException as req_err:
        return req_err
    except ValueError as json_err:
        return json_err

def hash(text):
	encoded_text = text.encode('utf-8')
	sha256_hash = hashlib.sha256(encoded_text)
	return str(sha256_hash.hexdigest())

def shakespearify(text):
    translations = {
        "away": "hence",
        "be": "art",
        "before": "ere",
        "believe": "credence",
        "big": "stout",
        "boy": "lad",
        "call": "beseech",
        "can": "canst",
        "come": "cōme",
        "dance": "gambol",
        "dear": "dost",
        "did": "didst",
        "do": "do",
        "feel": "fain",
        "find": "discover",
        "for": "for",
        "friend": "cousin",
        "go": "gō",
        "good": "goodly",
        "great": "marvelous",
        "happy": "blithe",
        "have": "hast",
        "hear": "hearken",
        "here": "hither",
        "hope": "trust",
        "I": "I",
        "is": "be",
        "it": "’tis",
        "know": "wot",
        "like": "liken",
        "love": "fain",
        "make": "do",
        "man": "fellow",
        "more": "more",
        "much": "many a",
        "new": "newe",
        "no": "nay",
        "not": "not",
        "now": "now",
        "old": "auld",
        "one": "ones",
        "play": "play",
        "post": "haste",
        "pretty": "fair",
        "put": "lay",
        "read": "red",
        "right": "aright",
        "run": "run",
        "say": "speak",
        "see": "see",
        "skill": "cunning",
        "smile": "smirk",
        "so": "so",
        "some": "some",
        "speak": "utter",
        "tell": "telest",
        "thank": "give thanks",
        "that": "that",
        "the": "thee",
        "then": "thence",
        "there": "there",
        "these": "those",
        "they": "they",
        "think": "thinketh",
        "this": "this",
        "to": "to",
        "try": "assay",
        "understand": "wot",
        "use": "employ",
        "want": "lack",
        "we": "we",
        "will": "wilt",
        "with": "with",
        "yes": "aye",
        "you": "thee",
        "young": "youthful"
    }

    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in translations.keys()) + r')\b', re.IGNORECASE)

    def replace_match(match):
        word = match.group(0)
        replacement = translations[word.lower()]
        if word.istitle():
            return replacement.capitalize()
        return replacement

    result = pattern.sub(replace_match, text)
    return f"{result}"


def get_user_data(user_id):
    with open("economy.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    return data.get(str(user_id), {"balance": 0})

def save_user_data(user_id, balance):
    with open("economy.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    data[str(user_id)] = {"balance": balance}
    with open("economy.json", "w") as f:
        json.dump(data, f)

def getComic(number=0):
    # set number to None if you want the current comic
    if number is None or number == 0:
        r = requests.get("https://xkcd.com/info.0.json")
    else:
        r = requests.get(f"https://xkcd.com/{number}/info.0.json")
        
    return r.json()

def getdata(object):
    return object.get('safe_title'), object.get('img'), object.get('alt'), object.get('num')

def getrmeme():
    url = "https://www.reddit.com/r/memes/top/.json"
    headers = {
        "User-Agent": "CyberFish/1.0",
        "Accept": "application/json"
    }

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        thumbnails = []
        for post in data['data']['children']:
            thumbnail = post['data'].get('thumbnail')
            if thumbnail:
                thumbnails.append(thumbnail)
    
        return random.choice(thumbnails)
    else:
        return "Error"


def getswmeme():
    url = "https://www.reddit.com/r/prequelmemes/top/.json"
    headers = {
        "User-Agent": "CyberFish/1.0",
        "Accept": "application/json"
    }

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        thumbnails = []
        for post in data['data']['children']:
            thumbnail = post['data'].get('thumbnail')
            if thumbnail:
                thumbnails.append(thumbnail)
    
        return random.choice(thumbnails)
    else:
        return "Error"
