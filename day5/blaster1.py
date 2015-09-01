
class BLASTER(object):

    def __init__(self, file):
        self.file = file
        self.last_ident = None
        self.current_line = "initialize"
        self.fetch_counter = 0
        
        
    def fetch_next_line(self):
        while (True):
            self.current_line = self.file.readline()
            if (self.current_line.startswith(">")):
                break
            if (len (self.current_line) == False):
                raise StopIteration
#            self.fetch_counter += 1
#            if (self.fetch_counter > 1000000):
#                raise StopIteration
        
    def next(self):
        if self.last_ident == None:
            self.fetch_next_line()
            ident = self.current_line.rstrip("\r\n")
        else:
            ident = self.current_line.rstrip("\r\n")
            self.fetch_next_line()
        identities = ""
        gaps = ""
        
        ### THE FOLLOWING BLOCKS ASSUME THAT SCORES COME BEFORE IDENTITIES
        ### THE FOLLOWING BLOCKS ASSUME THAT A SCORE AND AN IDENTITY OCCUR FOR EACH ENTRY OR (!!!!!!!!!) SOMEWHERE IN THE FILE (!!!!!!!!!!!)


        while True:
            line = self.file.readline()
            if len (line ) == False:
                raise StopIteration
            if not "Score" in line:
                continue
            else:
                scores = line[line.find("Score") + 8 : line.find(",")] 
                expects = line[line.find("Expect") + 9 :].rstrip("\r\n")
                break
        
        while True:
            line = self.file.readline()
            if len (line) == False:
                raise StopIteration
            if not "Identities" in line:
                continue
            else:
                identities = line[line.find("Identities") : line.find(",")] 
                gaps = line[line.find("Gaps") :].rstrip("\r\n")
                break
        
        self.last_ident = self.current_line
        
        if len (self.current_line) == 0:
            raise StopIteration
            

        return (ident, scores, expects, identities, gaps)
        
        
    
    
    def __iter__(self):
        return self