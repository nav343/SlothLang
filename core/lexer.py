class SLexer:
    def __init__(self, data):
        self.data     = data
        self.token    = []
        self.keywords = [
            'printout',
            'break',
            'skip',
            'inp'
        ]
    
    def tokenizer(self):
        for loc in self.data:
            temp   = []
            tempid = ''

            for l in loc:
                if l == '"' and tempid == '':
                    tempid = "char"
                    temp   = []
                
                elif l == '"' and tempid == 'char':
                    self.token.append({'id': tempid, 'value': ''.join(temp)})
                    temp = []
                
                elif l == ":":
                    self.token.append({'id': "label", "value": ''.join(temp)})
                    temp = []

                elif ''.join(temp) in self.keywords:
                    self.token.append({'id': 'keyword', 'value': ''.join(temp)})
                    temp = []
                
                elif l == "\n":
                    if len(temp) > 0:
                        self.token.append({'id': "atom", 'value': ''.join(temp)})
                        temp = []
                        
                elif l == ' ' and tempid != 'char':
                    continue
                else:
                    temp.append(l)
