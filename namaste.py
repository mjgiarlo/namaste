from __future__ import with_statement
import os
import glob

import re

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
    elif cmd == 'gettypes':
        get_types(d)
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
    
def get_types(d, verbose=True):
    type_tags = _get_namaste(d, 0)
    types = {}
    if type_tags:
        p = re.compile(r"""0=
                       (?P<name>[^_]+)_
                       (?P<major>\d+)\.
                       (?P<minor>\d+)""", re.VERBOSE)
        for t in type_tags:
            m = p.match(t)
            if m != None:
                g = m.groupdict()
                if verbose:
                    print "namaste - directory type %(name)s - version %(major)s.%(minor)s" % (g)
                types[g['name']] = g
    return types

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
    
def _get_namaste(d, tag):
    if not os.path.isdir(d):
        raise Exception("directory %s does not exist" % d)
    namaste = filter(lambda x: x.startswith('%s=' % tag), os.listdir(d))
    if namaste:
        return namaste
    return None

def _make_namaste(tag, value):
    return "%s=%s" % (tag, value)
