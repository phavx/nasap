TODO
====

This is a list of TODOs for _nasap_.

Only two categories exist:
- **Yes**: is planned, execution in no particular order
- **Maybe**: might be done if considered useful, lowest prioriy. If some of
these things are interesting to you _and_ you can come up with a patch, a quick
implementation is much more likely.

### Yes

- [x] handle "/" in titles so they don't end up in a filename and give an error
- [ ] more and better error handling, both of user's faults and malformed feeds
- [ ] currently we use the time of retrieval for a post, which isn't ideal. We
    should pick the time out of the feed item itself, but making sure to have a
    backup for feeds not providing it.
- [ ] introduce a config file for common settings
  - [ ] configurable base folder
  - [ ] configurable output format
    - [ ] plain text
    - [ ] markdown
  - [ ] configurable naming of files

- [ ] support for a list of feeds getting passed to _nasap_
  - [ ] feed urls
    - [ ] making sure https errors are no problem (self-signed certs f.e.)
  - [ ] override a feed's title

- [ ] speed it all up: right now all items are processed one after the other,
    which is slow and doesn't make proper use of available bandwith and CPUtime.
    Feeds should be processed in parallel, either limited by X per domain or
    X general threads. Question is, do it in Python or make use of tools such as
    f.e. GNU parallel?

- [x] speed up the processing by having a system which automatically skips
    already seen posts. Could rely on the feed items id or it's link, f.e.

- [X] move all internal links to the bottom

### Maybe

- [ ] create some hooks to automate post-processing
    - [ ] f.e. automatically symlink
    - [ ] initiate syncing to some other system
    - [ ] filter (f.e. kill everything containing _keyword_)
    - [ ] tag new posts via symlinking

- [ ] support libnotify/notify-send to inform the user about new feed items
    based on some criteria(f.e. "new posts from your favorite author", "new post
    containing _keyword_", etc).

- [ ] support enclosures like images, audiofiles, etc

All of the above should be done in a way so that the user can easily write some
scripts to achieve the task. It shouldn't be core functionality, but it's ok to
add such tools to the repo for the convenience or inspiration of others.