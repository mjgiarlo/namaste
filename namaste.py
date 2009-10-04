def main():
    import optparse    
    parser = optparse.OptionParser()
    options, args = parser.parse_args()
    
    cmd = args[0]

    if cmd == 'type':
        dirtype()
    elif cmd == 'who':
        who()
    elif cmd == 'what':
        what()
    elif cmd == 'when':
        when()
    elif cmd == 'where':
        where()
    else: 
        print "unknown command: %s" % cmd

def dirtype():
    pass

def who():
    pass

def what():
    pass

def when():
    pass

def where():
    pass

