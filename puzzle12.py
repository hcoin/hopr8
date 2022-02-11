'''
Created on Dec 30, 2021

@author: Harry Coin

When Steve and Katherine and Stephan arrived just after Christmas,
Steve brought this puzzle along.
https://forum.hoprnet.org/t/the-resistance-hopr-hunt-puzzle-8/3446
I'll print it out for you.  It was a 'massive' effort we all
undertook.  Steven's ideas were to consider the colorful squares
in combination within a frame.  Stephan took more of a 
'literary analysis' approach. I took more of a 'information
theoretic' approach.

You'll notice this file is titled puzzle12.py.  Each of the
previous attempts exhausted an approach to the problem,
and a few of them had versions a, b and c.  All failures
in that they were not the answer, but sucesses as well because:
as they were exhaustive in their exploration of an approach,
I could go on to another approach knowing I hadn't overlooked
the answer.  Twice I ran out of approach ideas, and almost
quit.  The next day I would think of another view on the problem
and so, more like a dog with a bone, worried on it until it finally
cracked. 

So the solutions to the puzzle are in the two tables below,
a result of copying and pasting a bit out of the program 
output run.

I've enclosed a copy of the puzzle, this program, and the
parts of the program output that are not repetitive.

Hope you have fun trying to crack it and following the logic.
My key to understanding the solution was to notice 'resistance'
could refer to the electrical components 'resistors' which have
performance ratings indicated on the little tube-shaped parts in
the form of colored rings.  I recalled the colors were exactly the
colors that appeared in the puzzle, and no others, with none left over.
I'll print out a page that describes how those parts are labelled 
(Ohm's law Voltage(volts) = current(amps) * resistance(ohms)
The habit there is the first two colored rings are digits 0..99
while the next is a power of 10 to multiply the first two, followed
by further colors to indicate accuracy and power handling detail.
I did come by this idea late, and initially had the computer just
try permutations on [0,1,..9]. 

It wasn't obvious at the outset which colorful frame was meant to
combine with which less colorful frame, and not obvious that
the upper left square of one ought be joined to its mate on 
the other, or perhaps flipped as in a mirror or rotated, etc.
likewise which maze-part was meant to go with what combination.
I saw early on that the only way to get a maze with but one
path through was to combine the two 'partial' mazes, and thought
that had to be significant.  I lost a whole lot of time thinking
there was information in maze 'walls' as they were duplicated
for no obvious reason in the partial mazes. Likewise I noticed
the number of steps through the 'official' solution maze was 16
and could be used to offset the letters.  All much too complex
for what the final answer was, but I did try them.  You'll notice
this file is named 'puzzle12'... and many earlier attempts had
3a and 3b, etc. 

Anyhow all that allowed me assign a number to each square.  The
numbers had to have a range of at least 26, because there are that
many letters and the phrases were made up of letters.   However,
the color system produced values that ranged from 0 to 29 -- more
than needed.  So, 0, 1, 2..6 could all have meant 'A' with still
enough left over so 29 could be 'Z'.  When I tried A starting at 1 (not
0), the result created lots of short English words, so then the
project was to assemlble the letters into proper sentences instead
of a mishmash of short words and misspellings.

Then I noticed a sort of dirty trick, the author purposely
used the code for the letter J to mean T. After all that there
are 26 letters didn't mean the author had to use them all.  Also,
the author appears to embrace misspellings, as there are two in the
text of the puzzle, so 'laire' was the answer instead of 'lair' which
is the proper spelling.

Then I looked at the 'maps with more than one path through' and
instead of choosing the best path, examined all paths
and used that to pick letters out of the combined graph to test.  Those
are the 'phrases' they were looking for.  But even those were
dirty tricks, since when you thought you got to the exit of the
maze you were done... no... you had to keep going picking squares
until you were boxed in and could make no legal moves.

Then I noticed that if you overlaid each 'bad half maze' upon the 
other, you got one good maze with just one way through.  Turns
out if you follow that path against each of the two phrase solutions
(not necessarily the letters that got used in those answers) you 
get the letters to the password.  

I cleaned up the program file a trace, removing many analysis
directions that were different than the puzzle author's.  I left
a few statements and comments from failed approaches out of interest.
Most of my failures were because of following hints that maybe it wasn't correct
to match the 10 colors frames from left to right, top to bottom
against the three color frames in the same order.  So I 
tried all of the orderings.  It was remarkable how I got
sort-of valid english out of many of the failed attempts. 
Probably an information theory paper in there somewhere.

I enjoyed getting re-aquainted with python's library of
permutations and combinations, lambda functions, and 
a nearly built-in set of all English words.

These are the solutions as produced by the run below.
I thought disused letters might be of interest, so I left 
them.

Ten color frame f2, Three color frame f1

longlear  11, 14, 13, 06, 11, 04, 00, 17, 
ARCHivai  00, 17, 02, 07, 08, 21, 00, 08, ARCH
siRAredn  18, 08, 17, 00, 17, 04, 03, 13,   RA
tseEphde  09, 18, 04, 04, 15, 07, 03, 04,    E
aNryrina  00, 13, 17, 24, 17, 08, 13, 00,  N
nDEcavSP  13, 03, 04, 02, 00, 21, 18, 15,  DE   SP
cemachiH  02, 04, 12, 00, 02, 07, 08, 07,        H
INtRALne  08, 13, 09, 17, 00, 11, 13, 04, IN RAL


Ten color frame f5, Three color frame f4

lookforF  11, 14, 14, 10, 05, 14, 17, 05, 
AYERORdL  00, 24, 04, 17, 14, 17, 03, 11, 
suladeaY  18, 20, 11, 00, 03, 04, 00, 24, 
butbewar  01, 20, 09, 01, 04, 22, 00, 17, 
MINERIFE  12, 08, 13, 04, 17, 08, 05, 04, 
EtOSLAAt  04, 09, 14, 18, 11, 00, 00, 09, 
HAUROGIH  07, 00, 20, 17, 14, 06, 08, 07, 
tDNAtHNE  09, 03, 13, 00, 09, 07, 13, 04,


'''

from english_words import english_words_lower_alpha_set
from multiprocessing import Process, Pipe
from itertools import permutations  # ,combinations
from puzzle2 import three_color_frame

p = permutations([0, 1, 2, 3], 2) 
mazewallpicks_2 = list(p)
p = permutations([0, 1, 2, 3], 3) 
mazewallpicks_3 = list(p)
p = permutations([0, 1, 2, 3])
mazewallpicks_4 = list(p)

frame_names = {0:"maze-long-col0", 1:"tri-color-brownT", 2:"10color-rgl", 3:"maze-long-row-0",
                  4:"tri-color-redT", 5:"10color-rgg", 6:"resistx4",
                  7:"Combined maze" , 8:"Duplicate maze"}
#              "half black and white maze",3 color, brown/black/red,10 color,       half black and white maze,3 color, brown/black/red",  "10 color",  "resist/resistx2"        

# Each maze wall is either [a]bsent, [t]hin or [f]at. Listed LRTB so atft would be left absent, right thin, top fat, bottom thin
f3 = [['ttft', 'ttff', 'ttff', 'ttff', 'ttff', 'ttff', 'tfft', 'ftft'],  # note 00 is 'wrong'
      ['tttf', 'ttff', 'ttft', 'tfft', 'ffft', 'ffft', 'fttt', 'tttt'],
      ['ttft', 'ttff', 'tttf', 'tttt', 'tttf', 'tttf', 'tftf', 'fttf'],
      ['tttf', 'ttff', 'ttff', 'tttt', 'ttff', 'ttff', 'ttft', 'ttft'],
      ['ttft', 'ttff', 'ttft', 'tttf', 'ttff', 'ttft', 'tftt', 'fttt'],
      ['tftt', 'ftft', 'tftf', 'ftft', 'ttft', 'tftf', 'fttf', 'tttt'],
      ['tftt', 'fttt', 'ttff', 'tftf', 'fftt', 'ftft', 'ttft', 'tttt'],
      ['tttt', 'tttt', 'ttft', 'ttft', 'tttt', 'tftt', 'fttt', 'ttta']
      # ['tttf','tttf','ttff','ttff','tttf','tftf','fttf','ttta']      
      ] 

f0 = [['ttft', 'ttff', 'ttff', 'ttff', 'tfft', 'ftft', 'ttff', 'ttft'],  # note 00 is 'wrong'
      ['tttt', 'ttff', 'ttft', 'ttft', 'tttf', 'tftf', 'ftft', 'tttf'],
      ['tttt', 'ttft', 'tftf', 'fttt', 'ttft', 'tfft', 'fttf', 'ttft'],
      ['tftt', 'fttf', 'tfft', 'fftt', 'fftt', 'fttf', 'tfft', 'fttt'],
      ['tttt', 'tfft', 'fttf', 'tttt', 'tttf', 'ttft', 'tttt', 'tttf'],
      ['tftt', 'fttf', 'tfft', 'fttf', 'ttff', 'tftf', 'fttf', 'ttft'],
      ['tttf', 'ttft', 'tttf', 'ttft', 'ttff', 'ttff', 'ttft', 'tttf'],
      ['ttft', 'tttt', 'ttft', 'tttt', 'ttft', 'tfft', 'fttt', 'ttfa'],
      # ['ttff','tttf','ttff','tttf','ttff','tfff','fttf','ttfa']      
      ]

colormap = {0:'red', 1:'green', 2:'brown', 3:'blue', 4:'grey', 5:'yellow', 6:'white', 7:'black', 8:'orange', 9:'purple'}
resistor_colormap = {0:'black', 1:'brown', 2:'red', 3:'orange', 4:'yellow', 5:'green', 6:'blue', 7:'purple', 8:'grey', 9:'white'}
spectrum_colormap = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
unordered_colors = ['black', 'brown', 'grey', 'white']

inverted_resistor = {}
for k, v in resistor_colormap.items():
    inverted_resistor[v] = k

diag_walk = [
    [ 1, 2, 6, 7, 15, 16, 28, 29],
    [ 3, 5, 8, 14, 17, 27, 30, 43],
    [ 4, 9, 13, 18, 26, 31, 42, 44],
    [10, 12, 19, 25, 32, 41, 45, 54],
    [11, 20, 24, 33, 40, 46, 53, 55],
    [21, 23, 34, 39, 47, 52, 56, 61],
    [22, 35, 38, 48, 51, 57, 60, 62],
    [36, 37, 49, 50, 58, 59, 63, 64]
    ]
  
inverted_diag_walk_dict = {}
for row in range(0, 8):
    for col in range(0, 8):
        inverted_diag_walk_dict[diag_walk[row][col] - 1] = (row, col)  
inverted_diag_walk = [ inverted_diag_walk_dict[i] for i in range(0, 64) ]
assert(inverted_diag_walk[4] == (1, 1)) 
     
f5 = [[0, 1, 1, 2, 3, 1, 4, 3],
    [2, 1, 1, 4, 1, 4, 5, 0],
    [6, 2, 0, 2, 5, 1, 2, 1],
    [0, 2, 7, 0, 1, 8, 2, 4],
    [8, 6, 5, 1, 4, 6, 3, 1],
    [1, 7, 1, 6, 0, 2, 2, 7],
    [4, 2, 2, 4, 1, 9, 6, 4],
    [7, 5, 5, 2, 7, 4, 5, 1]
    ]

scalemap = {0:'brown', 1:"black", 2:'red'}

f4 = [[0, 0, 0, 0, 1, 0, 0, 1],
    [1, 2, 1, 0, 0, 0, 1, 0],
    [0, 2, 0, 1, 1, 1, 1, 2],
    [1, 2, 0, 1, 1, 2, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 2, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1]
    ]

f1 = [[0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 2, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 2, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 2, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1]
    ]
#
f2 = [[0, 1, 5, 9, 0, 1, 2, 4],
    [2, 4, 8, 4, 6, 0, 2, 6],
    [6, 6, 4, 2, 4, 1, 5, 5],
    [7, 6, 1, 1, 3, 4, 5, 1],
    [2, 5, 4, 1, 4, 6, 5, 2],
    [5, 5, 1, 8, 2, 0, 6, 3],
    [8, 1, 8, 2, 8, 4, 6, 4],
    [6, 5, 7, 4, 2, 0, 5, 1]
    ]

bright_colormap = {0:'yellow', 1:'purple', 2:'red', 3:'ltblue', 4:'dkblue', 5:'green'}
fbright = [[0, 0, 1, 1, 2, 2, 2, 2],
           [2, 2, 2, 2, 1, 1, 1, 1],
           [3, 3, 3, 3, 3, 3, 3, 3],
           [4, 4, 4, 4, 0, 0, 0, 0],
           [5, 5, 5, 5, 5, 2, 2, 2],
           [0, 0, 0, 4, 4, 4, 0, 0],
           [0, 0, 0, 0, 0, 1, 5, 1],
           [5, 5, 5, 5, 5, 5, 1, 5]]

            
class maze(object):

    def __init__(self, m, framen):
        self.maze = m
        self.framenumber = framen
        self.check_maze_consistency()
        self.shortname = 'Maze frame ' + str(self.framenumber) + " " + frame_names[self.framenumber]
        self.arrow_list = []
        self.solutions = []
        
    def check_maze_consistency(self):
        for r in range(0, 8):
            for c in range(0, 8):
                left, right, up, down = self.maze[r][c]
                if c < 7: assert(right == self.maze[r][c + 1][0]), str(r) + " " + str(c)  # my right is next col's left.
                if c > 0: assert(left == self.maze[r][c - 1][1]), str(r) + " " + str(c)  # my left is prev col's right.
                if r < 7: assert(down == self.maze[r + 1][c][2]), str(r) + " " + str(c)  # my down is next row's up.
                if r > 0: assert(up == self.maze[r - 1][c][3]), str(r) + " " + str(c)  # my up is above row's down.
        
    def __str__(self):
        s = self.shortname + '\n'
        topbot = {'f':'=', 't':' ', 'a':'v', '?':'?'}
        for r in range(0, 8):
            for c in range(0, 8):
                s += '+' + topbot[self.maze[r][c][2]]
            s += '+\n'
            for c in range(0, 8):
                left = self.maze[r][c][0]
                if left == '?':
                    s += '??' 
                else:
                    s += "I " if left == 'f' else '  ' if c in range(1, 8) else '| '
                if c == 7:
                    right = self.maze[r][c][1]
                    if right == '?': s += '?'
                    else:
                        s += "I" if right == 'f' else '|'
            s += '   '
            for c in range(0, 8):
                s += '0,' if self.maze[r][c][0] == 't' else 'L,'
            s += '   '
            for c in range(0, 8):
                s += '0,' if self.maze[r][c][1] == 't' else 'R,'
            s += '   '
            for c in range(0, 8):
                s += '0,' if self.maze[r][c][2] == 't' else 'U,'
            s += '   '
            for c in range(0, 8):
                s += '0,' if self.maze[r][c][3] == 't' else 'D,'
    
            s += '\n'
            if r == 7:
                for c in range(0, 8):
                    s += '+' + topbot[self.maze[r][c][3]]
                s += '+\n'
        return s
    
    def solve_maze(self, strict_solutions=True, row=0, col=0, path=[]):
        ''' If strict_solutions, only count paths that lead to the exit.
            otherwise, count exit paths, but add all paths that start
            at the beginning, that lead to no unvisited legal next
            steps.'''
        if row == 0 and col == 0: 
            self.solutions = []
        path = path.copy() + [[row, col]]
        blocked = True
        left, right, up, down = self.maze[row][col]
        if (left == 't') and (col > 0):
            if not [row, col - 1] in path:
                blocked = False
                self.solve_maze(strict_solutions, row, col - 1, path)
        if (right == 't') and (col < 7):
            if not [row, col + 1] in path:
                blocked = False
                self.solve_maze(strict_solutions, row, col + 1, path)
        if (up == 't') and (row > 0):
            if not [row - 1, col] in path:
                blocked = False
                self.solve_maze(strict_solutions, row - 1, col, path)
        if (down == 't') and (row < 7):
            if not [row + 1, col] in path:
                blocked = False
                self.solve_maze(strict_solutions, row + 1, col, path)
        if ('a' in self.maze[row][col]) or (blocked and not strict_solutions):
            self.solutions += [path]
                
    def find_best_solutions(self):
        self.scores = []
        for sols in self.solutions:
            self.scores += [(len(sols), sols)]
        self.scores = sorted(self.scores)
        self.best_path = self.scores[0][1]
        self.shortest_walk = self.scores[0][0]
        
    def compute_solution_directions(self):
        self.arrow_list = []
        for sol in self.solutions:
            deltas = []
            for i in range(0, len(sol) - 1):
                deltas += [(sol[i + 1][0] - sol[i][0], sol[i + 1][1] - sol[i][1])]
            self.arrow_list += [deltas]

                    
class ten_color_frame(object):

    def __init__(self, fr, name):
        self.frame = fr
        self.name = name
        self.shortname = "Ten color frame " + name
        self.color_array = []
        self.resistor_array = []
        for row in range(0, 8):
            r = []
            r2 = []
            for col in range(0, 8):
                c = colormap[fr[row][col]]
                r += [c]
                r2 += [inverted_resistor[c]]
            self.color_array += [r]
            self.resistor_array += [r2]
        
    def __str__(self):
        s = self.shortname + '\n'
        for row in range(0, 8):
            for col in range(0, 8):
                e = self.color_array[row][col] + ", "
                s += e.ljust(15)
            s += '  '
            for col in range(0, 8):
                s += '{:d}, '.format(self.resistor_array[row][col])
            s += '\n'
        return s + '\n'

    
class three_color_frame(object):

    def __init__(self, fr, name):
        self.frame = fr
        self.name = name
        self.shortname = "Three color frame " + name
        self.color_array = []
        self.resistor_array = []
        for row in range(0, 8):
            r = []
            r2 = []
            for col in range(0, 8):
                c = scalemap[fr[row][col]]
                r += [c]
                r2 += [inverted_resistor[c]]
            self.color_array += [r]
            self.resistor_array += [r2]
        
    def __str__(self):
        s = self.shortname + '\n'
        for row in range(0, 8):
            for col in range(0, 8):
                e = self.color_array[row][col] + ", "
                s += e.ljust(10)
            s += '  '
            for col in range(0, 8):
                s += '{:d}, '.format(self.resistor_array[row][col])
            s += '\n'
        return s + '\n'
    

class combined_color_frame(object):

    def __init__(self, ten_c, three_c):
        self.shortname = ten_c.shortname + ", " + three_c.shortname
        self.resistor_array = []
        for row in range(0, 8):
            r = []
            for col in range(0, 8):
                v = ten_c.resistor_array[row][col] + 10 * three_c.resistor_array[row][col] - 1
                r += [v]
            self.resistor_array += [r]
        
    def __str__(self):
        s = self.shortname + '\n'
        for row in range(0, 8):
            for col in range(0, 8):
                c = chr(self.resistor_array[row][col] + ord('A'))
                if c == 'J': c = 't'
                s += c
            s += '  '
            for col in range(0, 8):
                s += '{:02d}, '.format(self.resistor_array[row][col])
            s += '\n'
        return s + '\n'
    

def this_is_a_lowercase_word_we_recognize(s):
    ''' Return a tuple: (x,is_special) where x=0 if no match, otherwise
        len(s) and true if we give the word priority recognition. '''
    special_words = ['ariadne', 'daedalus', 'resistance']
    l = len(s)
    if l == 1: 
        if s in ['a', 'i']:  # the set of english words has too many one letter elements.
            return(l, False)
    else:
        if s in special_words: 
            return(l, True)
        if s in english_words_lower_alpha_set:
            return(l, False)
    return (0, False)


def find_longest_recognized_word(s):
    max_wordlength = 15
    len_s = len(s)
    results = []
    for wordlength in range(min(len_s, max_wordlength), 0, -1):
        r = this_is_a_lowercase_word_we_recognize(s[0:wordlength])
        if r[0] > 0: 
            results += [r]
    return results
    

def count_consecutive_letters_in_english_words(s, clean=False, uncommon_word_allowance=0):
    # Don't count words shorter than min_wordlength or longer than 20 letters.
    max_wordlength = 15
    if not clean:
        sl = s.lower()
        s = ''
        for i in range(0, len(sl)):
            if sl[i].isalpha(): s += sl[i]
        uncommon_word_allowance = 1  # max(1,int(len(s)/5))

    trials = []
    result = 0
    found_word_list = find_longest_recognized_word(s)
    while True:
        for recognized_length, isspecial in found_word_list:
            r2 = result + recognized_length * recognized_length
            if isspecial: r2 += 20000
            r3, winners3 = count_consecutive_letters_in_english_words(s[recognized_length:], True, uncommon_word_allowance)
            trials += [(r2 + r3, [s[0:recognized_length]] + winners3)]
        if (len(found_word_list) == 0) and (uncommon_word_allowance > 0) and (len(s) > 0):
            for i in range(1, min(len(s), max_wordlength)):
                found_word_list = find_longest_recognized_word(s[i:])
                if len(found_word_list) > 0:  # there are 'real' words later on in the string.
                    r3, winners3 = count_consecutive_letters_in_english_words(s[i:], True, uncommon_word_allowance - 1)
                    trials += [(r3 + i, [s[0:i]] + winners3)]
                    s = s[i:]
                    break
            else:
                break
        else:
            break            
    if len(trials) > 0:
        trials = sorted(trials, reverse=True)
        return trials[0]
    return [0, []]


def sublevel_1_study(ten_1, _ten_2, ten_primary_order, three_1, _three_2, three_primary_order,
                    maze_1, _maze_2, maze_primary_order, top_score_and_discussion, pipe):
    # This version of the study does not use xxx_2 
    # if not (ten_primary_order and three_primary_order and maze_primary_order): return []

    picklist = [lambda row, col: (row, col, "row,col"),
                 # lambda row,col : (7-row,col,"7-row,col"),lambda row,col : (row,7-col,"row,7-col"),lambda row,col : (7-row,7-col,"7-row,7-col")
                 ]
    # picklist += [lambda row,col  : (col,row,"col,row"),lambda row,col : (7-col,row,"7-col,row"),lambda row,col : (col,7-row,"col,7-row"),lambda row,col : (7-col,7-row,"7-col,7-row")]

    info = ten_1.shortname + ", " + three_1.shortname + ", " + maze_1.shortname
    # if not 'Combined' in maze_1.shortname:  
    #    pipe.send(top_score_and_discussion)
    #    return
    for tencolorpick in picklist[0:1]:
        for threecolorpick in picklist[0:1]:
            for path_length, path in maze_1.scores:
                s = ''
                for row, col in path:

                    c_row, c_col, c_style = tencolorpick(row, col)
                    color_v = ten_1.resistor_array[c_row][c_col]
                    assert(color_v >= 0 and color_v <= 9)
                    
                    s_row, s_col, s_style = threecolorpick(row, col)
                    scale_v = three_1.resistor_array[s_row][s_col]
                    assert(scale_v >= 0 and scale_v <= 2)
                            
                    x = color_v + [0, 10, 20][scale_v]  # 0<=c<=29
                    x -= 1  # don't even ask how long it took to figure that one out...
                            
                    if x < 0 or  x > 25: 
                        s += ' '
                    else:
                        c = chr(x + ord('A'))
                        if c == 'J': c = 't'  # Which, really, ought obligate the puzzle author to buy many rounds of drinks.
                        s += c

                score, winners = count_consecutive_letters_in_english_words(s)
                if score > top_score_and_discussion[0][0]:
                    style = '\n  ' + s
                    style += '\n  '
                    for r, _c in path:
                        style += str(r)
                    style += '\n  '
                    for _r, c in path:
                        style += str(c)
                    style += '\n  '
                    style += str(winners) + "\n  path_length:" + str(path_length) + " c: " + c_style + " s: " + s_style + " " + info + "\n"  #  Studying combination msb: "+commentary0 +" lsb: "+commentary1+", "+style
                    top_score_and_discussion.pop(0)
                    top_score_and_discussion += [(score, style)]
                    top_score_and_discussion = sorted(top_score_and_discussion)
                # if score>5000:
                #    print(str(score)+": "+style,flush=True)
                        # except: 
                                #    pass
                                    
    pipe.send(top_score_and_discussion)
    # return top_score_and_discussion
                        
                
def global_study(f):
    keep_top_score_count = 10
    top_score_and_discussion = []
    for _i in range(0, keep_top_score_count):
        top_score_and_discussion += [(-1, "")]
    procs = {}
    pipes = {}
    count = 0
        
    for tenc_list in [[ten_color_frame_f5, ten_color_frame_f2, True], [ten_color_frame_f2, ten_color_frame_f5, False]]:
        ten_1, ten_2, ten_primary_order = tenc_list
        for threec_list in [[three_color_frame_f4, three_color_frame_f1, True], [three_color_frame_f1, three_color_frame_f4, False]]:
            three_1, three_2, three_primary_order = threec_list
            for mazec_list in [[maze_f3, maze_f0, True], [maze_f0, maze_f3, False], [maze_combined, None, True]]:
                maze_1, maze_2, maze_primary_order = mazec_list
                pipes[count] = Pipe()
                procs[count] = Process(target=sublevel_1_study,
                                     args=(ten_1, ten_2, ten_primary_order,
                                           three_1, three_2, three_primary_order,
                                           maze_1, maze_2, maze_primary_order,
                                           top_score_and_discussion, pipes[count][1]))
                procs[count].start()
                count += 1
        
    results = []
    for c2 in range(0, count):
        p_results = pipes[c2][0].recv()
        for score, discussion in p_results:
            results += [(score, "Process " + str(c2) + " " + discussion)] 
        procs[c2].join()

    results = sorted(results, reverse=True)

    for score, discussion in results:
        print(str(score) + ": " + discussion, file=f)
    print("\n\n", file=f)
    

if __name__ == '__main__':
    tl, tlist = count_consecutive_letters_in_english_words("argumentisjkgthree")
    assert(tl == 96 and tlist == ['argument', "is", 'jkg', 'three'])
    maze_f3 = maze(f3, 3)
    maze_f3.solve_maze(strict_solutions=False)
    maze_f3.find_best_solutions()                              

    # print(str(maze_f3))
    maze_f0 = maze(f0, 0)
    maze_f0.solve_maze(strict_solutions=False)
    maze_f0.find_best_solutions()                              
    # print(str(maze_f0))
    duplicates = []
    singletons = []
    combined = []
    for row in range(0, 8):
        rd = []
        rc = []
        rs = []
        for col in range(0, 8):
            s = ''
            d = ''
            n = []
            for side in range(0, 4):
                if f0[row][col][side] == f3[row][col][side]:  # A duplicate
                    s += f0[row][col][side]  # record the agreement.
                    d += f0[row][col][side]  # record the duplicate
                    n += ['  ']  # A duplicate is a no-match for singletons.
                elif f0[row][col][side] == 'f' or f3[row][col][side] == 'f':
                    s += 'f'  # if one or the other is fat, record the combined as fat.
                    d += '?'  # They do not agree, record a blank.
                    n += [f0[row][col][side] + f3[row][col][side]]
                else:
                    assert("Unexpected disagreement among mazes r" + str(row) + " c" + str(col))
                    # d+=f0[row][col][side].upper()
            rc += [s]
            rd += [d]
            rs += [n]
        combined += [rc]
        duplicates += [rd]
        singletons += [rs]
    maze_combined = maze(combined, 7)
    # print(str(maze_combined))
    maze_duplicates = maze(duplicates, 8)
    # print(str(maze_duplicates))

    ten_color_frame_f2 = ten_color_frame(f2, "f2")
    ten_color_frame_f5 = ten_color_frame(f5, "f5")
    three_color_frame_f1 = three_color_frame(f1, "f1")
    three_color_frame_f4 = three_color_frame(f4, "f4")
    
    with open("/tmp/hoprhunt.txt", "w") as f:
        cf1 = combined_color_frame(ten_color_frame_f2, three_color_frame_f1)
        print(str(cf1), file=f)
        cf2 = combined_color_frame(ten_color_frame_f5, three_color_frame_f4)
        print(str(cf2), file=f)
        print(str(maze_f0), file=f)
        print(str(three_color_frame_f1), file=f)
        print(str(ten_color_frame_f2), file=f)
        print(str(maze_f3), file=f)
        print(str(three_color_frame_f4), file=f)
        print(str(ten_color_frame_f5), file=f)
        print(str(maze_combined), file=f)
        maze_combined.solve_maze()
        maze_combined.find_best_solutions()                              
        print("Path through the maze:\n" + str(maze_combined.solutions), file=f)
        assert(len(maze_combined.solutions) == 1)
        print("Notice there are walls in one maze seemingly unnecessarily duplicated in the other.", file=f)
        print("The length of the solution path in the combined maze is " + str(len(maze_combined.solutions[0])), file=f)
        maze_combined.compute_solution_directions()
        print("Solution directions-- exactly 16: \n" + str(maze_combined.arrow_list[0][0:8]) + '\n' + str(str(maze_combined.arrow_list[0][8:])), file=f)
        print("Duplicate entries are:", file=f)
        print(str(maze_duplicates), file=f)
        
        print("\nSingle entries are:", file=f)
        for row in range(0, 8):
            for col in range(0, 8):
                print(str(singletons[row][col]), file=f, end='')
            print("", file=f)
            
        total_12_matches = 0
        for row in range(0, 8):
            tally = 0
            for col in range(0, 8):
                for side in range(0, 4):
                    if singletons[row][col][side] != '  ': tally += 1
            if tally == 12: 
                print("Row " + str(row) + " has exactly 12 mismatching walls", file=f)
                total_12_matches += 1
        for col in range(0, 8):
            tally = 0
            for row in range(0, 8):
                for side in range(0, 4):
                    if singletons[row][col][side] != '  ': tally += 1
            if tally == 12: 
                print("Col " + str(col) + " has exactly 12 mismatching walls", file=f)
                total_12_matches += 1
        print("Notice only the rightmost column has exactly 12 mismatching walls.", file=f)
        assert(total_12_matches == 1)
        
        s1 = ''
        s2 = ''
        for row, col in maze_combined.solutions[0]:
            c = chr(cf1.resistor_array[row][col] + ord('A'))
            if c == 'J': c = 't'
            s1 += c
            c = chr(cf2.resistor_array[row][col] + ord('A'))
            if c == 'J': c = 't'
            s2 += c
        print("Used to deduce the password: single path letters, cf1,cf2:\n" + s1 + "\n" + s2 + "\n\n", file=f)
        
        for m in [maze_f0, maze_f3]:
            print("Maze solutions for " + m.shortname, file=f)
            for l, sol in m.scores[-4:]:
                print(str(l) + ": " + str(sol), file=f)
        print("Study results using maze frames to pick content:\n\n", file=f)
        global_study(f)
        # print("\n",f)
        # global_study(maze_f3, f)
        # global_study(evaluator_2, f)
        
