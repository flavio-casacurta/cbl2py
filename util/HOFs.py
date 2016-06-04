from HOFsGenericas import *


isCopy = lambda line: 'COPY' in words(line)[1]
isInclude = lambda line: ('INCLUDE' in words(line)[1] and 'SQLCA' not in words(line)[1])
isLink = lambda line: 'LINK' in words(line)[1]
isXctl = lambda line: 'XCTL' in words(line)[1]
isCall = lambda line: 'CALL' in words(line)[1]
l672 = lambda line: line[6:72].rstrip()
workingRe =re.compile(r'WORKING-STORAGE\s+SECTION', re.UNICODE)
isWorking = lambda line: truth(workingRe.search(line))
linkageRe =re.compile(r'LINKAGE\s+SECTION', re.UNICODE)
isLinkage = lambda line: truth(linkageRe.search(line))
procRe = re.compile(r'PROCEDURE\s+DIVISION', re.UNICODE)
isProcedure = lambda line: truth(procRe.search(line))

