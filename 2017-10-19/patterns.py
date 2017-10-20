from bottery.conf.patterns import Pattern
from bottery.views import pong
from views import hello 

patterns = [
    Pattern('ping', pong),
    Pattern('hello', hello),
]



