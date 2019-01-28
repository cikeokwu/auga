import math
import utils

def lineFinder(Point1, Point2):
    slope = (Point2[1] - Point1[1]) / (Point2[0] - Point1[0])
    intercept = Point1[1] - slope * Point1[0]
    return [slope, intercept]


def residualArray(xaxis, Line, Pricelist):
    residualArray = []
    for i in range(0, len(Pricelist)):
        residualArray.append(Pricelist[i] - (Line[0] * xaxis[i] + Line[1]))
    return residualArray


def volatilityFinder(PriceList):
    xaxis = []
    for i in range(0, len(PriceList)):
        xaxis.append(i)
    Line = lineFinder([xaxis[0], PriceList[0]], [xaxis[len(xaxis) - 1], PriceList[len(PriceList) - 1]])
    ResidArray = residualArray(xaxis, Line, PriceList)
    return math.sqrt(utils.var(ResidArray))