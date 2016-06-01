from HOFs import *
lines = open(r'..\example.cbl').readlines()
clearLines = map(l672, filter(all3(isNotRem, isNotBlank, isNotEjectOrSkip), lines))
