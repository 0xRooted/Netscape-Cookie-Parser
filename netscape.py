'''
@Use Example

netscape_parser = netscape('cookie.txt')
all_cookies = netscape_parser.parse_and_return()
print(all_cookies)
'''
class netscape:
    
    def __init__(self, file:str):
        self.file = file
        self.all_lines = []
        self.final_cookies = []
        with open(self.file, "r+") as f:
            temp_lines = f.readlines()
            for line in temp_lines:
                self.all_lines.append(line.strip())
    
    def parse_and_return(self):
        if len(self.all_lines) == 0:
            return False
        else:
            for line in self.all_lines:
                try:
                    line = ' '.join(line.split())
                    data = line.split(' ')
                    self.final_cookies.append({
                        'domain': data[0],
                        'path': data[2],
                        'name': data[5],
                        'value': data[6],
                    })
                except:
                    continue
            return self.final_cookies
