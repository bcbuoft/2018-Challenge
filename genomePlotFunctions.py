# genomePlotFunctions.R
#
# Functions for genome plot starter code.
#
# License: GPL-3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
#
# Dependencies:
#           os, pandas, math, svgwrite
#
# Author:  where not otherwise stated:
#          Modified from R code by
#          Boris Steipe <boris.steipe@utoronto.ca>
#==========================================================================


#TOC> ==========================================================================
#TOC>
#TOC>   Section  Title                                            Line
#TOC> ----------------------------------------------------------------
#TOC>   1        DEPENDENCIES                                       33
#TOC>   2        FUNCTIONS TO INITIALIZE DATA STRUCTURES            42
#TOC>   2.01       chrSetUp()                                       44
#TOC>   3        ANNOTATION FUNCTIONS                               66
#TOC>   4        LAYOUT FUNCTIONS                                   68
#TOC>   4.01       category2colour()                                90
#TOC>   4.02       ang2rad()                                        93
#TOC>   4.02       lin2arc()                                       114
#TOC>   5        PLOTTING FUNCTIONS                                137
#TOC>
#TOC> ==========================================================================


# =    1  DEPENDENCIES  ============================================================
import os
import pandas as pd
import svgwrite
from math import pi, cos, sin
from numpy import mean

COLFILE = "svgCols.txt" #the provided svgCols file contains a list of svg colours
                        #that excludes very pale and hard to see colours

# =    2  FUNCTIONS TO INITIALIZE DATA STRUCTURES  =============================

# ==   2.01  chrSepUp()  ========================================================

# There are many possibilities to store the data for the objects we will analyze
# and draw. Here we take a very simple approach and store gene-level data in one
# data frame.

def chrSetUp(fileName):
    '''Return a dataframe holding chromosome information read from provided file

    @:type fileName: str, file name of chromosome data file
    @:rtype pd.DataFrame, chromosome dataframe
    '''

    #load in data
    chrfile = os.path.abspath(fileName)
    chr = pd.read_table(chrfile, header=0)

    #make rows selectable based on HUGO symbol
    chr = chr.set_index("sym")

    return chr

# =    3  ANNOTATION FUNCTIONS  ================================================

# =    4  LAYOUT FUNCTIONS  ====================================================

# ==   4.01  category2colour()  ========================================================
def category2colour(chr, cat):
    '''Associate a column of categories with a colour, and add a column of colours to the chromosome dataframe.

    @type chr: pd.DataFrame, chromosome dataframe
    @type cat: str, name of column to use as categories to colour by
    @:rtype  pd.DataFrame, augmented chromosome dataframe
    '''

    #assign different colours to each unique category
    categories = pd.DataFrame()
    categories[cat] = chr[cat].unique()

    #get colours
    colfile = os.path.abspath(COLFILE)
    cols = pd.read_table(colfile, header=None)

    #assign colours and place into chr dataframe
    categories["colour"] = cols[0:len(categories[cat])]
    chr = chr.join(categories.set_index(cat), on=cat)

    return chr

# ==   4.02  ang2rad()  ========================================================

def ang2rad(theta):
    '''Convert a rotation angle theta from degrees to radians
    (theta starts from vertical and rotates in clockwise direction)

    @type theta: num, rotation angle in degrees from 0 at (0, 1), clockwise.
    @:rtype num, an angle in radians
    '''

    #degrees to radians
    x = ((2 * theta) / 360) * pi

    #change direction of roatation
    x = -x

    #add 90 degrees
    x = x + (pi / 2)
    return x

# ==   4.03  lin2arc()  ========================================================

def lin2arc(coord, l , ori, r):
    '''Convert linear coordinates on a line of length l to arc positions on a circle centered at ori with radius r.
    Return the coordinates of where to draw an arc and the rotation angle. We define the start to be at the top,
    and the positive direction is clockwise

    @:type coord: num, linear coordinate
    @:type l: num, chromosome length
    @:type ori: num, (x,y) coordinates of the circle center
    @:type r: num, circle radius
    @:rtype list, three element list of (x,y) coordinates on the circle and the rotation angle in degrees, where 0 is
                  a vertical line and the direction of rotation is clockwise
    '''

    #find the rotation in radians
    degRot = (coord/l) * 360
    radRot = ang2rad(degRot)
    x = (cos(radRot) * r) + ori[0]
    y = (sin(radRot) * r) + ori[1]

    return [x, y, degRot]

# =    5  PLOTTING FUNCTIONS  ==================================================

#see documentation for svgwrite

#[END]


