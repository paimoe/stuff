"""
Works with pretty simple solutions
@todo:
    - check diagonals
    - check each square
"""

def printer(full):
    line = '+---+---+---+'
    i = 0
    for k,l in full.items():
        if i % 3 == 0:
            print(line)

        first = ''.join([str(l) for l in l][0:3])
        second = ''.join([str(l) for l in l][3:6])
        last = ''.join([str(l) for l in l][6:9])

        line2 = '|'
        line2 += '|'.join([first, second, last])
        line2 += '|'
        print(line2)
        i += 1
    print(line)

demo = """xxx26x7x1
68xx7xx9x
19xxx45xx
82x1xxx4x
xx46x29xx
x5xxx3x28
xx93xxx74
x4xx5xx36
7x3x18xxx"""

demo = """1xx26xxx4
6x7xxxxx2
xxxxxx5xx
2x8xxxx37
7xx6x94xx
xxxx8xx9x
xxx9xx8xx
9x3xx6xxx
xxxx7xx1x"""

chars = [1,2,3,4,5,6,7,8,9]
def rest(used):
    return [x for x in chars if x not in used]

assert len(demo) == 89, len(demo)

p = {'r': [], 'c': []}

rows = {}
cols = {}

lines = demo.split("\n")
row = 0
for line in lines:
    sp = list(line)
    chars_used = []
    col = 0
    for char in sp:
        if char != 'x':
            thischar = int(char)
            chars_used.append(thischar)
        else:
            thischar = 0

        try:
            rows[row].append(thischar)
        except:
            rows[row] = [thischar]

        #print('cols', cols)
        try:
            cols[col].append(thischar)
        except:
            cols[col] = [thischar]

        col += 1
    row += 1

#print(cols, rows)

while True:
    for rnum in rows:
        row = rows[rnum]
        s = sum(row)
        if s == 45:
            print('row complete')
            continue
        #print(row)
        needed = rest(row)

        col = 0
        for ch in row:
            if ch == 0:
                # triangulate
                needed_this = rest(row + cols[col])
                print('needed this', needed_this, '{}:{}'.format(rnum, col))

                if len(needed_this) == 1:
                    # 
                    print('updating {}:{} with a {}'.format(rnum, col, needed_this[0]))
                    rows[rnum][col] = needed_this[0]
                    cols[col][rnum] = needed_this[0]
            col += 1

    full_rows = sum([sum(row) for k, row in rows.items()]) == 45 * 9
    full_cols = sum([sum(col) for k, col in cols.items()]) == 45 * 9
    complete = full_rows and full_cols
    
    if complete:
        break

printer(rows)