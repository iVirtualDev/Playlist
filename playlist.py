import glob
import codecs
import random


def write_playlist(from_glob, to_outfile, order=None):
    if '.m3u' not in to_outfile:
        to_outfile = to_outfile + u'.m3u'

    items = glob.glob(from_glob)
    if order == 'random':
        random.shuffle(items)
    elif order == 'sorted':
        items = sorted(items)
    elif order == 'reverse':
        items = sorted(items, reverse=True)

    playlist = u'#EXTM3U\n' + u'\n'.join(items) + u'\n'
    with open(to_outfile, 'w') as f:
        f.write(codecs.encode(playlist, 'utf8'))


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    write_playlist(unicode(args[0]), unicode(args[1]), None if len(args) < 3 else args[2])
