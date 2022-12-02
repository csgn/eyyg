from apachelogs import LogParser

parser = LogParser(
    '%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-agent}i" %O')
