from __future__ import with_statement
import os
import glob

def main():
    import optparse    
    parser = optparse.OptionParser("Usage: %prog [options] <cmd> [<value>]")
    parser.add_option("-d", dest="directory", default=os.getcwd(), 
                      help="directory")
    options, args = parser.parse_args()
    
    if len(args) == 0:
        parser.print_help()
        return 

    d = options.directory
    cmd = args[0]
    value = None
    try:
        value = args[1]
    except IndexError:
        pass

    if cmd == 'type':
        dirtype(d, value)
    elif cmd == 'who':
        who(d, value)
    elif cmd == 'what':
        what(d, value)
    elif cmd == 'when':
        when(d, value)
    elif cmd == 'where':
        where(d, value)
    elif cmd == 'get':
        get(d)
    else: 
        print "unknown command: %s" % cmd

def dirtype(d, value, verbose=True):
    namaste =  _set_namaste(d, 0, value)
    if verbose:
        print "created namaste %s" % namaste
    return namaste

def who(d, value, verbose=True):
    namaste = _set_namaste(d, 1, value)
    if verbose: 
        print "created namaste %s" % namaste
    return namaste

def what(d, value, verbose=True):
    namaste = _set_namaste(d, 2, value)
    if verbose:
        print "created namaste %s" % namaste
    return namaste

def when(d, value, verbose=True):
    namaste = _set_namaste(d, 3, value)
    if verbose:
        print "created namaste %s" % namaste
    return namaste

def where(d, value, verbose=True):
    namaste = _set_namaste(d, 4, value)
    if verbose:
        print "created namaste %s" % namaste
    return namaste

def get(d, verbose=True):
    tags = []
    for namaste in glob.iglob(os.path.join(d, "[0-4]=*")):
        tags.append(namaste)
    if tags and verbose:
        print "namastes: %s" % ", ".join(tags)
    return tags

def _set_namaste(d, tag, value):
    if not value:
        return None
    if not os.path.isdir(d):
        raise Exception("directory %s does not exist" % d)
    namaste = os.path.join(d, _make_namaste(tag, value))
    with open(namaste, 'w') as f:
        f.write(value)
        f.write("\n")
    return namaste

def _make_namaste(tag, value):
    return "%s=%s" % (tag, value)
