Playlist
========

Generates an M3U playlist file from the contents of a folder.

Command-line arguments:

    python playlist.py from_glob to_outfile order

* `from_glob`, a glob string which describes the files you want to include
* `to_outfile`, the file string to open as your output file. Will append .m3u if not present.
* `order`, how to sort the file names. Does not read metadata. Defaults to arbitrary ordering (often alphanumeric).
 * `sorted`, sort by alphanumeric ordering
 * `reverse`, sort by reverse alphanumeric ordering
 * `random`, sort by random ordering

Usage example:

    python playlist.py "\my files\music\*.mp3" playlist.m3u random


