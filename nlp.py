# coding=utf8
from snownlp import sentiment
from snownlp import SnowNLP

s = SnowNLP(u"这个东西真赞")

print(s.sentiments)
