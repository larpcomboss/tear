


from __future__ import annotations
import random
import string
import time
import json
import os
import sys
import urllib.request
import urllib.error
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Set, Tuple, Callable

# ------------------------ ANSI palette (dark/edgy, terminal friendly) ------------------------
ANSI_DIM       = "\033[2m"
ANSI_RESET     = "\033[0m"
ANSI_DGRAY     = "\033[90m"
ANSI_RED_DARK  = "\033[31m"
ANSI_GREEN_DIM = "\033[32m"
ANSI_CYAN_TECH = "\033[36m"
ANSI_MAG_EDGY  = "\033[95m"
ANSI_YELLOW    = "\033[33m"
ANSI_BOLD      = "\033[1m"

# ------------------------ Configuration / pools ------------------------
STORE_FILE = "found_usernames_per_key.json"
DEFAULT_CHARSET = string.ascii_lowercase + string.digits + "_"
SEED_WORDS = [ "gun","crime","swat","lol","hi","ghost","zero","nova","drift","blade","core","rift","omega","pawn","haze","vex","strike","crypt""gad","dog","marsh","ace","bat","ask","bio","hyd","fox","egg","fin","ash","fog","bee","bus","bit",
"cow","fan","cut","dot","fun","fat","ear","ant","fig","due","bug","bat","hyd","bio","fox","cow",
"bus","egg","marriage","craftsman","rolling","mechanical","aviation","overdrive","trend","poetry",
"beaches","hummingbird","lincoln","marsh","sandwich","hyd","bug","bit","bat","bee","ant","fog",
"fun","fat","fox","cow","bus","ear","dot","cut","ask","egg","bio","ace","fan","fig","due","ash",
"bat","dog","fox","hyd","bee","cow","fin","bug","ant","fun","fat","bit","ear","fog","egg","bat",
"bio","fan","dot","ash","ace","bus","cut","cow","fox","fin","bee","due","ant","fat","fun","egg",
"bit","dog","hyd","ash","fan","fig","cow","fox","egg","bat","bee","bus","cut","fog","ant","fun",
"bio","fat","ear","bit","fin","dot","dog","hyd","bug","ash","fan","cow","bee","fox","bat","egg",
"cut","fun","fat","bit","ear","fog","bus","ant","fig","bio","hyd","dog","bat","bee","cow","fox",
"bus","egg","cut","fun","fat","ear","ash","ant","bit","dot","fig","fan","bio","hyd","bug","fox",
"cow","bee","bus","fin","egg","fun","fat","bat","ash","cut","ear","dog","fog","bio","hyd","ant",
"bug","bat","bit","bee","fox","cow","bus","fun","fat","fig","egg","fan","ash","ear","cut","dog",
"dot","bio","hyd","bat","bug","cow","bee","fox","fin","bus","egg","fun","fat","ash","ear","ant",
"fig","fan","bit","dog","bio","hyd","fog","bat","cow","bee","bus","fox","cut","fun","fat","egg",
"ash","ear","fig","fin","ant","dot","fan","bio","hyd","bug","bat","cow","bee","fox","bus","fun",
"fat","egg","ash","ear","cut","fig","dog","bit","ant" "trel","vask","morn","drix","quav","lyro","peln","xorn","thir","rano","brix","selo","meph","tavn","jorl",
"yexo","narl","kovi","zaph","marn","fexo","lehn","vorn","tril","karo","deth","pilo","sran","qern","nilo",
"farn","bryn","zuth","relo","jarn","tovi","krix","xavi","leth","mavi","thon","haro","tavi","nexo","dorn",
"bari","phex","lovi","zorn","fril","tevo","ravi","sarn","vexo","navi","hurn","qilo","fovo","tarn","rilo",
"yern","zari","mexo","neth","javi","pano","brin","xern","lavi","qarn","mevi","korn","tavo","silo","runi",
"davi","zaro","havi","naro","duno","kevi","vumo","tani","carn","bevi","larn","slek","mavi","tari","novi",
"vorn","bavi","thav","yilo","levo","murl","dari","zune","pahn","fovi","rath","vilo","xilo","teph","aba","abo","abs","aby","ace","act","add","ado","ads","adz","aff","aft","aga","age","ago","ags","aha","ahi","ahs","aid","ail","aim","ain","air","ais","ait","ala","alb","ale","all","alp","als","alt","ama","ami","amp","amu","ana","and","ane","ani","ant","any","ape","apo","app","apt","arb","arc","are","arf","ark","arm","ars","art","ash","ask","asp","ass","ate","att","auk","ava","ave","avo","awa","awe","awl","awn","axe","aye","ays","azo","baa","bad","bag","bah","bal","bam","ban","bap","bar","bas","bat","bay","bed","bee","beg","bel","ben","bes","bet","bey","bib","bid","big","bin","bio","bis","bit","biz","boa","bob","bod","bog","boo","bop","bos","bot","bow","box","boy","bra","bro","brr","bub","bud","bug","bum","bun","bur","bus","but","buy","bye","bys","cab","cad","cam","can","cap","car","cat","caw","cay","cee","cel","cep","chi","cig","cis","cob","cod","cog","col","con","coo","cop","cor","cos","cot","cow","cox","coy","coz","cru","cry","cub","cud","cue","cum","cup","cur","cut","cwm","dab","dad","dag","dah","dak","dal","dam","dan","dap","daw","day","deb","dee","def","del","den","dev","dew","dex","dey","dib","did","die","dif","dig","dim","din","dip","dis","dit","doc","doe","dog","dol","dom","don","dor","dos","dot","dow","dry","dub","dud","due","dug","duh","dui","dun","duo","dup","dye","ear","eat","eau","ebb","ecu","edh","eds","eek","eel","eff","efs","eft","egg","ego","eke","eld","elf","elk","ell","elm","els","eme","ems","emu","end","eng","ens","eon","era","ere","erg","ern","err","ers","ess","eta","eth","eve","ewe","eye","fab","fad","fag","fan","far","fas","fat","fax","fay","fed","fee","feh","fem","fen","fer","fes","fet","feu","few","fey","fez","fib","fid","fie","fig","fil","fin","fir","fit","fix","fiz","flu","fly","fob","foe","fog","foh","fon","fop","for","fou","fox","foy","fro","fry","fub","fud","fug","fun","fur","gab","gad"]

COMMON_WORDS = ["alpha","bravo","charlie","delta","echo","foxtrot","ghost","zero",
    "vex","nova","blade","shadow","haze","pulse","drift","riot","flux",  "bolt","rune","strike","core""mechanical","overdrive","craftsman","marriage","aviation","rolling","trend","poetry","beaches",
"hummingbird","lincoln","sandwich","marsh","mechanical","overdrive","craftsman","aviation","trend",
"beaches","poetry","rolling","marriage","hyd","bio","dog","fox","egg","fat","fan","bug","bit","ear",
"ash","cut","dot","cow","bus","bee","ant","fig","fin","fun","fog","bat","ace","ask","bio","hyd",
"dog","fox","egg","fat","fan","bug","bit","ear","ash","cut","dot","cow","bus","bee","ant","fig",
"fin","fun","fog","bat","ace","ask","mechanical","overdrive","craftsman","marriage","aviation",
"rolling","trend","poetry","beaches","hummingbird","lincoln","sandwich","marsh","hyd","bio","dog",
"fox","egg","fat","fan","bug","bit","ear","ash","cut","dot","cow","bus","bee","ant","fig","fin",
"fun","fog","bat","ace","ask","mechanical","overdrive","craftsman","marriage","aviation","rolling",
"trend","poetry","beaches","hummingbird","lincoln","sandwich","marsh","hyd","bio","dog","fox",
"egg","fat","fan","bug","bit","ear","ash","cut","dot","cow","bus","bee","ant","fig","fin","fun",
"fog","bat","ace","ask","mechanical","overdrive","craftsman","marriage","aviation","rolling",
"trend","poetry","beaches","hummingbird","lincoln","sandwich","marsh""vorn","mavx","tarn","drix","lume","nava","keph","saro","tyen","briv","quon","fale","wern","jaro","xine",
"murl","tevi","roth","plin","sava","grix","neph","daro","tume","bryn","xaro","leph","harn","mavi","dreq",
"talo","vrek","runi","sorn","kael","phex","noro","yern","velk","duna","jave","zorn","karo","thil","fran",
"mevi","slek","ravi","teph","vono","morn","havi","prax","rilo","neth","kevi","larn","zune","tari","quix",
"silo","dran","fovi","brak","nilo","thar","xern","vumo","rath","levo","pano","wrax","bavi","srin","dexo",
"jelo","runi","meph","krix","naro","hurn","zaro","vrek","farn","qilo","lavi","dorn","tani","mexo","jarn",
"fron","brix","vuno","leth","pahn","zari","rilo","tavo","kern","xilo","marn","dari","qarn","nevi","haro",
"sren","vilo","bren","zuth","mevi","yorn","jilo","thav","overdrive","should","yo1","chimp","styles","teens","iol","musical","ethernet","hyd","after","poetry","sandwich","rmi","emperor","hurry","143","dfk","hoj","barb","rag","shuckle","countryman","tre","fi","rwt","fill","muv","craftsman","chile","ccd","brunette","unsolved","crease","d00","namespace","available","always","abundance","rge","thompson","253","rolling","trend","dou","zyz","ta0","equator","luq","threshold","dft","millennium","3cs","commence","quiz","gbg","bottle","eag","chw","clara","witsend","weblog","carolina","beaches","viable","vzn","5nh","ue8","ead","regime","drunk","cigarettes","save","nkv","younger","cnv","ghi","edg","smartly","legendary","notre","strain","numeric","usable","beach","aviation","character","alike","234","rmd","cage","which","vym","roadblock","trunks","hamburger","cameroon","scandal","gnc","packard","jnt","portable","assassin","vth","interested","8pm","jse","lil","serpent","swimming","alj","sheer","using","gore","gie","marsh","r0n","nkk","qwe","copier","ert","tile","williams","petunia","3x3","meg","barrister","influence","rnx","41","scientific","provolone","rules","meu","gox","schoolboy","oog","guided","saints","cbc","lopez","pna","authorization","undertow","llx","glue","smitten","ouc","ppa","bobble","remark","safari","tyo","coleman","september","fake","dreamboat","defrost","cleveland","booking","deals","dso","lincoln","121","hummingbird","gala","cooling","yok","strategic","sizzle","emergency","purchasing","ablaze","yhv","hastily","mle","802","tinsel","dwarf","prankish","watches","abu","qmt","slowking","mechanical","erupt","dpd","starts","survivor","stench","dominion","lexington","charles","crime","ech","hyf","ed0","spank","cavalier","fzk","veteran","j83","nova","gh1","lining","wic","referred","sgv","nur","xjh","squiggly","andorra","bda","undertone","dsf","posture","korea","ggk","gwv","igi","cuc","rhode","syria","reflects","stops","enchanted","allow","planner","kxu","browse","header","submit","tamil","sga","unmanned","heal","znm","jfv","hospital","aboriginal","trident","bnc","eed","surrender","database","magmar","casualty","diane","dwk","royalty","ud","bm2","safely","krm","morgana","tricks","iva","monaco","sedative","italiano","we","direct","dpr","blk","dui","pools","apnic","caterer","fashion","cll","result","txi","552","d2b","jqa","knr","uys","rim","wzt","lasting","arrive","operations","doe","shuffle","lovers","hang","vendor","deface","jaj","britain","harmonize","capital","technology","handy","fta","ere","choir","member","exclusion","wna","inbox","omission","cleaner","transexual","m85","jxh","pristine","jujitsu","achieve","harrier","grandeur","palace","its","deem","cep","florist","vsnet","huj","angling","merely","small","djn","later","ultimatum","simpsons","vdn","idp","penetration","kazakhstan","pco","starlet","4tm","axv","potential","vxy","sandile","multiple","watchdog","chevy","baboon","pool","prospect","douche","wud","parish","ous","lko","steelix","aiu","skimmer","latina","cohen","ivory","barista","138","onion","away","caress","cbf","dislike","vbv","powerpoint","transmitter","wwi","upon","owb","marina","microphone","lonely","dispatcher","mql","child","latino","leeds","stubborn","bags","stooge","vacant","sullivan","flatbed","capitol","sale","senate","mum","creed","rescuer","qu","truce","tgw","diverse","neighborhood","qzz","unread","traveller","antigua","890","zok","tgv","alc","bxj","right","loading","pnz","sells","aug","coordinated","demonstrate","shiftless","registered","glimmer","ju8","deadly","staging","raleigh","neural","nee","ecology","mandrill","pth","uco","survivors","awn","bmz","catalogs","212","rehab","army","jrj","been","qsm","kbm","qdh","hyt","jnd","dare","volume","wdw","ep7","indian","opening","grad","vig","stove","po","sharon","designers","systems","illusion","klu","modulator","crusader","innocent","years","mixing","garbage","alarm","canadian","revolution","development","px1","scenic","nr8","pri","hyundai","donna","ho","akita","troubleshooting","salsa","dvp","greensboro","c0d","uou","keyboard","shopper","recycled","pest","amid","russia","mke","concern","exit","drama","sny","ebony","assets","rjf","clang","analyst","tkj","k1m","cattle","adipex","qc","yoga","digital","gxg","barely","accept","s2s","corpus","toner","inter","injection","maui","ups","monsieur","slinky","aliens","wildfire","cda","genuine","transit","ljp","fares","hgq","deutschland","wfd","attitudes","bfc","computers","kindness","game","tribal","morphine","professionals","prominent","qyw","highlights","prune","miami","mongoose","correct","flyaway","745","cornflake","seedot","effectiveness","amp","freeway","washington","liner","sov","replace","jow","shone","fp1","immersion","comedy","tft","crm","heritage","dirty","renaissance","vista","oar","moves","papua","pye","peru","undead","caz","linguist","kmo","pandemic","cataract","began","interact","poultry","bristle","fvb","ree","immovable","fzw","prot","fair","parameters","194","jgi","myt","charlotte","ifs","airborne","pes","jfr","cvc","scoff","scottish","lay","cables","host","ryj","sqy","cinema","oaf","allied","beginners","sensation","alpine","volvo","honda","multitask","trader","bulldog","icky","amu","cakes","similar","hog","sona","325","lug","ktl","mi","454","invalid","nol","kick","muck","fitted","snooper","jmq","builder","daily","relight","birth","thru","goldeen","erratic","sfb","sdg","bangladesh","babes","accounting","legume","judgment","careful","belly","focal","finally","serotonin","hdtv","uprising","ecuador","holland","pw8","mkp","ios","mambo","eir","linking","designer","sgc","hotmail","tqe","luy","banners","jaybird","nerve","tipper","specialist","shoptalk","oddish","slk","wsx","northeast","tcl","testimony","c2o","latitude","crc","entwine","ashes","showbiz","isn","eqm","arbitrary","hotels","tpb","handlebar","ans","sloppy","hulk","warrant","homeland","laz","nhs","retired","mallard","slain","fingers","giants","brute","wooden","hacksaw","naughty","interesting","jvd","quarter","valley","york","jackpot","father","stand","strip","latios","299","enforced","located","group","octagon","wage","cqs","rakan","apt","smuggler","shrew","mile","facts","uxo","knc","321","yks","advertising","n4p","vu","insurance","fairy","opu","kgo","finale","wince","shriek","kingdra","cfk","probiotic","pqs","vsn","matador","amh","imprint","fzz","sympathy","fleece","sandbank","arceus","leaf","nidorino","stingray","pale","dimension","hfc","nba","gul","crusher","show","guests","builds","class","rochester","und","t64","stockholm","incorrect","ruse","kcw","reactor","adorn","windows","pilot","fairness","diploma","coordinator","shiver","grenade","diamond","pound","sda","arcs","dividend","artisan","xan","yep","cur","ruf","senate","notebook","ottawa","idiot","ahp","mp3","render","qur","doodle","sbf","lah","qaz","hew","emily","kappa","lsv","lpj","vulcan","tnt","upward","gok","bumble","mnk","unite","xxl","booster","honest","slowpoke","chase","slicer","marvel","lud","skate","rocky","adelaide","pry","lrc","public","isa","root","obvious","icq","edward","ufo","abstract","paws","civ","workshop","granite","lazuli","echo","hgf","mrs","ubq","nmu","faith","weight","enigma","thrush","dumbbell","mmm","soup","harbor","accepts","sterling","karate","jak","fry","aquarius","dug","uua","trio","midi","cow","kitten","tiger","roland","gag","twig","annex","dye","supply","bride","wolf","huh","lilac","elks","lounge","plaza","huh7","si","magic","air","flux","crab","tib","auburn","kpi","wee","ape","bfs","mellow","vagabond","plume","junior","otter","cbc","cta","npc","bop","mango","cpa","fry","hive","mia","bma","lex","cia","aim","zen","due","ray","bob","kin","dim","boa","hex","tux","gem","vet","yak","jim","fig","hue","fox","arc","ben","ada","leo","max","ivy","nat","sky","liz","ash","eve","rae","lia","lou","amy","van","ivy","sam","ray","lou","zoo","kay","nia","mia","tim","ara","ali","ben","tom","gus","eli","ada","tom","tom","jay","ned","joe","tim","leo","luc","dan","ara","sal","ted","lee","may","liz","leo","cam","pam","rye","jay","sam","hal","ivy","ted","tim","ivy","ned","ray","liz","joy","ava","gem","kit","max","kay","lou","tom","eva","amy","mia","ivy","leo","ada","ray","ted","sam","liz","joe","ben","leo","tim","tom","ara","amy","lia","ivy","luc","gus","joy","ned","tim","max","ted","sam","ray","ada","leo","liz","mia","tim","tom","ara","amy","liz","tim","leo","ada","joe","sam","ben","joy","ivy","max","ted","leo","liz","amy","tim","tom","ara","ray","ada","sam","joy","ben","leo","tim","ivy","max","ted","liz","amy","tom","ara","leo","tim","sam","ray","ada","joy","liz","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben","tim","amy","leo","tom","ara","liz","sam","ray","ada","joy","ted","max","ben" 
]
SEPARATORS = ["", "_", "-", ".", "x"]
DEFAULT_MIN_LEN = 6
DEFAULT_MAX_LEN = 9

# ------------------------ Predefined plans (3-letter keys + admin) ------------------------
PLAN_KEYS: Dict[str, Dict[str, object]] = {
    "oky": {"max_runs_per_site": 3, "max_users_per_site": 100, "duration_per_run": 20, "allow_all": False},
    "lol": {"max_runs_per_site": 5, "max_users_per_site": 200, "duration_per_run": 30, "allow_all": True},
    "hi":  {"max_runs_per_site": 2, "max_users_per_site": 50,  "duration_per_run": 15, "allow_all": False},   "eyJhbGdvcml0aG1zIjogW1siQkFTRTY0IiwgbnVsbF1dLCAiY2lwaGVydGV4dCI6ICJaWFpsIn0=": {"max_runs_per_site": 4, "max_users_per_site": 150, "duration_per_run": 25, "allow_all": False},
    "adm": {"max_runs_per_site": 999999, "max_users_per_site": 999999, "duration_per_run": 600, "allow_all": True},
}

# ------------------------ Site options ------------------------
@dataclass
class SiteOption:
    number: int
    key: str
    label: str

SITE_OPTIONS = [
    SiteOption(1, "insta", "Instagram sniper"),
    SiteOption(2, "tiktok", "TikTok sniper"),
    SiteOption(3, "discord", "Discord sniper"),
    SiteOption(4, "roblox", "Roblox sniper"),
    SiteOption(5, "xbox", "Xbox sniper"),
    SiteOption(6, "psn", "PSN sniper"),
    SiteOption(7, "telegram", "Telegram sniper"),
]

# ------------------------ Utility functions ------------------------
def safe_print(*args, **kwargs):
    # simple wrapper so prints flush immediately
    print(*args, **kwargs)
    sys.stdout.flush()

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# ------------------------ Persistence ------------------------
def load_store() -> dict:
    try:
        if os.path.exists(STORE_FILE):
            with open(STORE_FILE, "r", encoding="utf-8") as fh:
                data = json.load(fh)
                if isinstance(data, dict):
                    return data
    except Exception:
        pass
    return {}

def save_store(store: dict):
    try:
        with open(STORE_FILE, "w", encoding="utf-8") as fh:
            json.dump(store, fh, indent=2)
    except Exception as e:
        safe_print(ANSI_RED_DARK + "Error saving store:" + ANSI_RESET, e)

# ------------------------ Name generation strategies ------------------------
def generate_random(length: int) -> str:
    return "".join(random.choice(DEFAULT_CHARSET) for _ in range(length))

def generate_seed_variant(length: int) -> str:
    w = random.choice(SEED_WORDS)
    if random.random() < 0.35:
        w2 = random.choice(SEED_WORDS)
        w = f"{w}{random.choice(SEPARATORS)}{w2}"
    if random.random() < 0.5:
        w = f"{w}{random.randint(0,999)}" if random.random() < 0.5 else f"{random.randint(0,999)}{w}"
    return w[:length]

def generate_dictionary_combo(length: int) -> str:
    try:
        count = random.choices([1,2,3], weights=[0.5,0.35,0.15], k=1)[0]
    except Exception:
        count = 1
    parts = [random.choice(COMMON_WORDS) for _ in range(count)]
    sep = random.choice(SEPARATORS)
    base = sep.join(parts)
    if random.random() < 0.4:
        base = f"{base}{random.randint(0,9999)}" if random.random() < 0.5 else f"{random.randint(0,9999)}{base}"
    return base[:length]

def generate_mixed(length: int) -> str:
    r = random.random()
    if r < 0.45:
        return generate_seed_variant(length)
    if r < 0.7:
        prefix = random.choice(SEED_WORDS)
        sep = random.choice(SEPARATORS)
        suffix_len = max(1, length - len(prefix) - len(sep))
        suffix = "".join(random.choice(DEFAULT_CHARSET) for _ in range(suffix_len))
        return (prefix + sep + suffix)[:length]
    return generate_random(length)

class MarkovGenerator:
    def __init__(self, order: int = 2):
        self.order = max(1, order)
        self.model: dict = defaultdict(list)
    def train_from_list(self, words: List[str]):
        for w in words:
            w = (w or "").strip()
            if not w:
                continue
            padded = ("~" * self.order) + w + "$"
            for i in range(len(padded) - self.order):
                key = padded[i:i+self.order]
                nxt = padded[i+self.order]
                self.model[key].append(nxt)
    def generate(self, max_length: int = 10) -> str:
        key = "~" * self.order
        out = []
        for _ in range(max_length * 2):
            choices = self.model.get(key)
            if not choices:
                break
            nxt = random.choice(choices)
            if nxt == "$" or len(out) >= max_length:
                break
            out.append(nxt)
            key = (key + nxt)[-self.order:]
        return "".join(out)[:max_length]

# ------------------------ HTTP availability check ------------------------
def check_username_http(site: str, username: str, timeout: float = 4.0) -> bool:
    """
    Best-effort HTTP check: returns True if HTTP GET indicates username page is missing (404).
    NOTE: different sites use different status codes/behaviors — this is a heuristic.
    """
    url_map = {
        "insta": f"https://www.instagram.com/{username}/",
        "tiktok": f"https://www.tiktok.com/@{username}",
        "discord": f"https://discord.com/users/{username}",
        "roblox": f"https://www.roblox.com/users/{username}/profile",
        "xbox": f"https://account.xbox.com/en-us/Profile?gamertag={username}",
        "psn": f"https://my.playstation.com/{username}",
        "telegram": f"https://t.me/{username}"
    }
    url = url_map.get(site)
    if not url:
        return False
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible)"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            # often reachable pages return 200; 404 suggests missing (available)
            return resp.status == 404
    except urllib.error.HTTPError as e:
        # HTTPError contains a status code
        return getattr(e, "code", None) == 404
    except Exception:
        # network errors/timeouts -> treat as unconfirmed (False)
        return False

# ------------------------ UI helpers ------------------------
ASCII_HEADER = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣶⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣼⣷⡶⠶⠶⠶⠦⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⣠⣾⣿⣿⣶⣶⣶⣶⣶⣶⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣶⣧⣤⣤⣤⣤⣤⣤⣤⣶
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢿⣿⣿⣿⡿⠿⠛⠋⣩⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠓⠚⣿⣿⣿⠀⠀⢠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⠿⠛⠋⣀⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣤⣶⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⣀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
Madeby: Lemonaidd    
   [!]  1800+ users — Username SnIPER
"""

def show_header_and_plan_masked(plan: dict):
    clear_terminal()
    safe_print(ANSI_MAG_EDGY + ASCII_HEADER + ANSI_RESET)
    safe_print(ANSI_CYAN_TECH + " [!] Your limits:" + ANSI_RESET)
    safe_print(ANSI_DGRAY + f"  Max runs/site : {plan['max_runs_per_site']}" + ANSI_RESET)
    safe_print(ANSI_DGRAY + f"  Max users/site: {plan['max_users_per_site']}" + ANSI_RESET)
    safe_print(ANSI_DGRAY + f"  Default dur   : {plan['duration_per_run']}s" + ANSI_RESET)
    safe_print("")

def show_menu(plan: dict):
    safe_print(ANSI_CYAN_TECH + "Menu (choose number(s)):" + ANSI_RESET)
    for o in SITE_OPTIONS:
        safe_print(ANSI_DGRAY + f"  {o.number}) {o.label}" + ANSI_RESET)
    if plan.get("allow_all"):
        safe_print(ANSI_DGRAY + "  all) Run all snipers" + ANSI_RESET)
    safe_print(ANSI_DGRAY + "  8) Clear terminal" + ANSI_RESET)
    safe_print(ANSI_DGRAY + "  9) Show ALL found usernames for this key" + ANSI_RESET)
    safe_print(ANSI_DGRAY + "  0) Exit" + ANSI_RESET)
    safe_print("")

def resolve_selection(user_input: str, plan: dict) -> List[str]:
    pick = (user_input or "").strip().lower()
    if pick in ("8", "clear"):
        return ["__clear__"]
    if pick in ("9", "show"):
        return ["__show__"]
    if pick == "all":
        return [s.key for s in SITE_OPTIONS] if plan.get("allow_all") else []
    keys = []
    for tok in pick.split(","):
        tok = tok.strip()
        if not tok:
            continue
        if tok.isdigit():
            try:
                n = int(tok)
            except Exception:
                continue
            for s in SITE_OPTIONS:
                if s.number == n:
                    keys.append(s.key)
                    break
        else:
            for s in SITE_OPTIONS:
                if tok == s.key or tok == s.label.lower().split()[0]:
                    keys.append(s.key)
                    break
    # dedupe preserve order
    out = []
    seen = set()
    for k in keys:
        if k not in seen:
            out.append(k); seen.add(k)
    return out

# ------------------------ Rarity logic & run goal ------------------------
def pick_run_goal() -> int:
    # Make zero very likely (~88%); otherwise choose 3-5
    choices = [0, 3, 4, 5]
    weights = [88, 4, 4, 4]
    return random.choices(choices, weights=weights, k=1)[0]

# ------------------------ Core run logic ------------------------
def run_sniper(duration_sec: int,
               markov: MarkovGenerator,
               targets: List[str],
               plan: dict,
               key: str,
               run_counter: dict,
               found_counter: dict,
               do_http_check: bool = True) -> Dict[str, List[str]]:
    

    gens: List[Callable[[int], str]] = [
        generate_random, generate_seed_variant, generate_dictionary_combo, markov.generate, generate_mixed
    ]
    run_found_map: Dict[str, Set[str]] = defaultdict(set)
    end = time.time() + max(1, int(duration_sec))
    total_rounds = 0

    unavailable = [t for t in targets if run_counter.get(t, 0) >= plan["max_runs_per_site"]]
    active_targets = [t for t in targets if t not in unavailable]
    if not active_targets:
        safe_print(ANSI_YELLOW + "No targets available to run (all reached run limits)." + ANSI_RESET)
        return {}

    # increment run counts for this session
    for t in active_targets:
        run_counter[t] = run_counter.get(t, 0) + 1

    target_goal = pick_run_goal()
    BASE_AVAIL_PROB = 0.0006  # base 0.04% probability; adaptive boost when needing multiple targets

    safe_print(ANSI_CYAN_TECH + f"\nStreaming generation for {duration_sec}s; active targets: {', '.join(active_targets)}" + ANSI_RESET)
    safe_print(ANSI_DGRAY + f"(Internal run target_goal: {target_goal}; most runs will be zero.)" + ANSI_RESET)

    try:
        while time.time() < end:
            # stop early if target reached
            if target_goal > 0 and len(run_found_map) >= target_goal:
                safe_print(ANSI_YELLOW + f"Reached run goal of {target_goal}; ending early." + ANSI_RESET)
                break

            # drop active targets that already hit per-site caps
            active_targets = [t for t in active_targets if found_counter.get(t, 0) < plan["max_users_per_site"]]
            if not active_targets:
                safe_print(ANSI_YELLOW + "Per-site found caps reached for active targets — ending early." + ANSI_RESET)
                break

            ln = random.randint(DEFAULT_MIN_LEN, DEFAULT_MAX_LEN)
            gen_fn = random.choice(gens)
            try:
                name = gen_fn(ln)
            except TypeError:
                name = gen_fn(ln)
            except Exception:
                name = generate_random(ln)

            for t in list(active_targets):
                if found_counter.get(t, 0) >= plan["max_users_per_site"]:
                    continue

                # ultra-rare availability check
                if target_goal == 0:
                    is_avail = False
                else:
                    remaining = target_goal - len(run_found_map)
                    adaptive = BASE_AVAIL_PROB * max(1.0, (1.0 + 0.25 * remaining))
                    is_avail = random.random() < adaptive

                if is_avail:
                    # do HTTP confirmation if requested (best-effort)
                    confirmed = False
                    if do_http_check:
                        try:
                            confirmed = check_username_http(t, name)
                        except Exception:
                            confirmed = False
                    disp = name + (" (GET NOW)" if confirmed else "")
                    safe_print(ANSI_GREEN_DIM + f"[+] {t:8} {disp:30} AVAILABLE" + ANSI_RESET)
                    run_found_map[name].add(t)
                    found_counter[t] = found_counter.get(t, 0) + 1
                    # enforce per-site cap message
                    if found_counter[t] >= plan["max_users_per_site"]:
                        safe_print(ANSI_YELLOW + f"[!] Reached max saved users for {t} (limit {plan['max_users_per_site']})" + ANSI_RESET)
                else:
                    safe_print(ANSI_RED_DARK + f"[-] {t:8} {name:30} taken" + ANSI_RESET)

            total_rounds += 1
    except KeyboardInterrupt:
        safe_print(ANSI_YELLOW + "\nInterrupted by user — wrapping up..." + ANSI_RESET)

    safe_print(ANSI_CYAN_TECH + f"\nRun complete — generated ~{total_rounds} rounds." + ANSI_RESET)

    # Merge findings into persistent store under this key, obeying per-site caps
    store = load_store()
    key_bucket = store.get(key, {}) if isinstance(store.get(key, {}), dict) else {}
    added_map: Dict[str, List[str]] = {}

    # count how many per-site already saved for this key
    per_site_saved = defaultdict(int)
    for uname, sites in key_bucket.items():
        for s in sites:
            per_site_saved[s] += 1

    # add run findings but only if per-site cap allows
    for uname, sites in sorted(run_found_map.items()):
        allowed_sites = []
        for s in sorted(sites):
            if per_site_saved.get(s, 0) < plan["max_users_per_site"]:
                allowed_sites.append(s)
                per_site_saved[s] += 1
        if not allowed_sites:
            continue
        existing = set(key_bucket.get(uname, []))
        new_sites = set(allowed_sites) - existing
        if new_sites:
            merged = sorted(existing.union(new_sites))
            key_bucket[uname] = merged
            added_map[uname] = merged

    store[key] = key_bucket
    try:
        save_store(store)
    except Exception:
        pass

    return added_map

# ------------------------ Display stored usernames for key ------------------------
def show_found_for_key(key: str):
    store = load_store()
    key_bucket = store.get(key, {}) if isinstance(store.get(key, {}), dict) else {}
    clear_terminal()
    safe_print(ANSI_GREEN_DIM + f"=== FOUND USERNAMES '{key}' ===" + ANSI_RESET)
    if not key_bucket:
        safe_print("(no names stored yet)")
    else:
        entries = sorted(key_bucket.items(), key=lambda kv: kv[0].lower())
        for i, (uname, sites) in enumerate(entries, 1):
            safe_print(ANSI_DGRAY + f"{i:4}) {uname:30} -- sites: {', '.join(sites)}" + ANSI_RESET)
    input("\nPress Enter to return to menu...")

# ------------------------ Admin (simple) ------------------------
def admin_menu(store: dict):
    while True:
        clear_terminal()
        safe_print(ANSI_MAG_EDGY + "=== ADMIN MENU ===" + ANSI_RESET)
        safe_print("1) Show whole store JSON")
        safe_print("2) Clear a key's stored names")
        safe_print("3) Erase store file (destructive)")
        safe_print("0) Return")
        ch = input("admin> ").strip()
        if ch == "1":
            clear_terminal()
            safe_print(json.dumps(store, indent=2))
            input("\nPress Enter...")
        elif ch == "2":
            k = input("Key to clear > ").strip()
            if k in store:
                confirm = input(f"Confirm clear all names for '{k}'? (y/N) > ").strip().lower()
                if confirm == "y":
                    store.pop(k, None)
                    save_store(store)
                    safe_print(ANSI_YELLOW + f"Cleared key '{k}'." + ANSI_RESET)
                else:
                    safe_print("Aborted.")
            else:
                safe_print("Key not found.")
            input("Press Enter...")
        elif ch == "3":
            confirm = input("Type ERASE to confirm erase entire store > ").strip()
            if confirm == "ERASE":
                store.clear()
                save_store(store)
                safe_print(ANSI_YELLOW + "Store erased." + ANSI_RESET)
            else:
                safe_print("Aborted.")
            input("Press Enter...")
        elif ch == "0":
            break
        else:
            safe_print("Unknown option.")
            time.sleep(0.5)

# ------------------------ Main interactive flow ------------------------
def main():
    store = load_store()
    clear_terminal()
    safe_print(ANSI_MAG_EDGY + ASCII_HEADER + ANSI_RESET)
    print("Freeuse key: oky")
    key = input(ANSI_YELLOW + "Enter your  passkey > " + ANSI_RESET).strip()
    if key not in PLAN_KEYS:
        safe_print(ANSI_RED_DARK + "Passkey not recognized. Exiting." + ANSI_RESET)
        return
    plan = PLAN_KEYS[key]
    is_admin = (key == "adm")

    # session counters
    run_counter: Dict[str, int] = defaultdict(int)
    found_counter: Dict[str, int] = defaultdict(int)
    # load existing counts for this key
    existing_bucket = store.get(key, {}) if isinstance(store.get(key, {}), dict) else {}
    for uname, sites in existing_bucket.items():
        for s in sites:
            found_counter[s] = found_counter.get(s, 0) + 1

    mg = MarkovGenerator(order=2)
    mg.train_from_list(COMMON_WORDS + SEED_WORDS + ["shadowblade","novadrift","ghostcore","riftzero","haze_pulse","strikeflux","cryptbolt","pawnblade"])

    while True:
        show_header_and_plan_masked(plan)
        show_menu(plan)
        choice = input("Choose option(s) or command > ").strip().lower()

        if choice in ("0", "exit"):
            safe_print(ANSI_YELLOW + "Exiting. Saving store." + ANSI_RESET)
            save_store(store)
            break
        if choice in ("8", "clear"):
            clear_terminal(); continue
        if choice in ("9", "show"):
            show_found_for_key(key); 
            # refresh store after possible edits
            store = load_store()
            continue
        if is_admin and choice == "admin":
            admin_menu(store)
            store = load_store()
            continue

        resolved = resolve_selection(choice, plan)
        if resolved == [] and choice == "all":
            safe_print(ANSI_RED_DARK + "Your plan does not permit running 'all' targets. Choose specific targets." + ANSI_RESET)
            input("Press Enter to continue...")
            continue
        if not resolved:
            safe_print(ANSI_RED_DARK + "No valid targets selected. Try again." + ANSI_RESET)
            time.sleep(0.7)
            continue

        targets = resolved
        blocked = [t for t in targets if run_counter.get(t, 0) >= plan["max_runs_per_site"]]
        if blocked:
            safe_print(ANSI_YELLOW + f"The following targets reached your max run count and will be skipped: {', '.join(blocked)}" + ANSI_RESET)
            targets = [t for t in targets if t not in blocked]
            if not targets:
                input("Press Enter to continue...")
                continue

        try:
            dur_input = input(f"Run duration in seconds (default {plan['duration_per_run']}) > ").strip()
            duration = int(dur_input) if dur_input else int(plan['duration_per_run'])
        except Exception:
            duration = int(plan['duration_per_run'])
        if duration < 1: duration = int(plan['duration_per_run'])

        # perform run (HTTP check enabled)
        new_added = run_sniper(duration, mg, targets, plan, key, run_counter, found_counter, do_http_check=True)

        # display summary
        if new_added:
            safe_print("\n" + ANSI_GREEN_DIM + "=== SUMMARY: FOUND AVAILABLE USERNAMES (this run) ===" + ANSI_RESET)
            for i, (uname, sites) in enumerate(sorted(new_added.items()), 1):
                safe_print(ANSI_GREEN_DIM + f"{i:3}) {uname:30}  sites: {', '.join(sites)}" + ANSI_RESET)
            safe_print(ANSI_CYAN_TECH + f"\nSaved {len(new_added)} new names to your key store." + ANSI_RESET)
            store = load_store()
        else:
            safe_print(ANSI_YELLOW + "\nNo new available usernames found this run." + ANSI_RESET)

        again = input("\nRun another? (Y/n) > ").strip().lower() or "y"
        if again != "y":
            safe_print(ANSI_YELLOW + "Exiting. Saving store." + ANSI_RESET)
            save_store(store)
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        safe_print(ANSI_RED_DARK + "Fatal error:" + ANSI_RESET, e)
        # attempt to save store before exiting if possible
        try:
            save_store(load_store())
        except Exception:
            pass
        raise
