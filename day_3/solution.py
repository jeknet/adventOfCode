from statistics import mean

class Part:
    def __init__(self, value, row, start, end):
        self.value = value
        self.row = row
        self.start = start
        self.end = end

    def __str__(self):
        return "{row} - {value} [{start}:{end}]".format(row=self.row, value=self.value, start=self.start, end=self.end)

    def __repr__(self):
        return "{row} - {value} [{start}:{end}]".format(row=self.row, value=self.value, start=self.start, end=self.end)

class Solution:
    total = 0

    def __init__(self, path):
        with open(path) as file:
            self.lines = file.readlines();

    def isSymbol(self, val):
        if val.isnumeric() or val == ".":
            return False;
        return True
    
    def symbolExists(self, row, start, end):
        iFrom = start - 1 if start > 0 else start
        iTo = end + 2 if end + 1 <= len(self.lines[row]) else end + 1

        # print(self.lines[row][iFrom:iTo])
        for val in self.lines[row][iFrom:iTo]:
            if self.isSymbol(val):
                return True
            
        return False
        

    def isEnginePart(self, part):
        if part.row - 1 >=0 and self.symbolExists(part.row -1 , part.start, part.end):
            return True
        if part.row + 1 <= len(self.lines) - 1 and self.symbolExists(part.row + 1, part.start, part.end):
            return True
        if part.start - 1 >= 0 and self.isSymbol(self.lines[part.row][part.start - 1]):
            return True
        if part.end + 1 <= len(self.lines[part.row]) and self.isSymbol(self.lines[part.row][part.end + 1]):
            return True 

        return False
            
    
    def processLine(self, line: str, index: int):
        parts = []
        val = ""
        for i in range(len(line)): 
            if line[i].isnumeric():
                val += line[i]
            elif len(val) > 0:
                start = i - len(val)
                end = i - 1
                parts.append(Part(int(val), index, start, end))
                val = ""
        
        total = 0
        count = 0
        for part in parts:
            if self.isEnginePart(part): 
                # print("IsPart", part)
                total += part.value
                count += 1
        # print(index + 1, count, len(parts))

        return total 

    def process(self):
        response = 0 
        res = []
        for i in range(len(self.lines)):
            partial = self.processLine(self.lines[i], i)
            res.append(partial)
            # print(i+1, partial)
            response += partial

        print(mean(res))
        print(sum(res))

        return response


sol = Solution("challenge3.txt")
print(sol.process())
