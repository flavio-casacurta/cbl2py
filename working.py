
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
        return False, [], [], 'Nao e um programa Cobol valido'

    try:
        line_fim = clearLines.index(filter(isLinkage, clearLines)[0])
    except IndexError:
        try:
            line_fim = clearLines.index(filter(isProcedure, clearLines)[0])
        except IndexError:
            return False, [], [], 'Nao e um programa Cobol valido'

    lines = homogenize(clearLines[line_ws + 1:line_fim])

    wstxt = 'ws = {'
    wsdic = {}

    for line in lines:
        match = CobolPatterns.row_pattern.match(line.strip())
        if not match:
            continue
        match = match.groupdict()

        if not match['level']:
            continue

        level = int(match['level'])

        if redefines:
            if level > lvlred:
                continue
        redefines = False
        lvlred = 0

        if match['redefines']:
            lvlred = level
            redefines = True
            continue

        if occurs:
            if level > lvlocc:
                if match['pic']:
                    locc += lenfield(match['pic'], match['usage'])
                continue
            lrecl += locc * occurs
        occurs = False
        lvlocc = 0

        if match['occurs']:
            lvlocc = level
            occurs = (int(nextWord('OCCURS', line)) if 'TO' not in wrds else
                      int(nextWord('TO', line)))

        if match['pic']:
            if occurs:
                locc += lenfield(match['pic'], match['usage'])
            else:
                lrecl += lenfield(match['pic'], match['usage'])



