#_*_ coding:utf-8_*_
import json
user_info='{"quote":"方式","ranges":[{"start":"/p[10]","startOffset":111,"end":"/p[10]","endOffset":113}],"text":"","date":"2018-09-28 10:56:30","tags":["entityType:Protein"],"id":2,"_local":{"highlights":[{"jQuery11120186217326714591":77}]}}'

temp = '[{"start":"/p[10]","startOffset":111,"end":"/p[10]","endOffset":113}]'

if temp in user_info:
    print "aaaaaaaaaaaaaaaaaaaaaaaa"

