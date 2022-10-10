class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

ranks = [
    {"text": " 2", "high": False},
    {"text": " 3", "high": False},
    {"text": " 4", "high": False},
    {"text": " 5", "high": False},
    {"text": " 6", "high": False},
    {"text": " 7", "high": False},
    {"text": " 8", "high": False},
    {"text": " 9", "high": False},
    {"text": "10", "high": False},
    {"text": " J", "high": True},
    {"text": " Q", "high": True},
    {"text": " K", "high": True},
    {"text": " A", "high": True}
]

suits = [
    {"icon": "♠️", "color": "black"},
    {"icon": "♣️", "color": "black"},
    {"icon": "♦️", "color": "red"},
    {"icon": "♥️", "color": "red"}
]