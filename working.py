
import os
import re
from util.HOFs import *
from util.homogenize import homogenize
from util.Constantes_Figurativas import *
from util.CobolPatterns import *


def working(lines):
    clearLines =  filter(isNotRem, lines)

    try:
        line_ws = clearLines.index(filter(isWorking, clearLines)[0])
    except IndexError:
        return False, [], [], 'Nao e um programa'

    try:
        line_fim = clearLines.index(filter(isLinkage, clearLines)[0])
    except IndexError:
        try:
            line_fim = clearLines.index(filter(isProcedure, clearLines)[0])
        except IndexError:
            return False, [], [], 'Nao e um programa'

    ws = homogenize(clearLines[line_ws + 1:line_fim])

    wstxt = 'ws = {'
    wsdic = {}



