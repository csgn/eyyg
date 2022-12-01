from apachelogs import LogParser

PARSER = LogParser(
    '%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-agent}i" %O')
