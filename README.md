nasap ***(news as simple as possible)***
========================================

* [What is nasap?](https://github.com/phavx/nasap/blob/master/README.md#what-is-nasap)
* [Why yet another feedreader?](https://github.com/phavx/nasap/blob/master/README.md#why-yet-another-feedreader)
* [Still, why?](https://github.com/phavx/nasap/blob/master/README.md#still-why)
* [Things I don't like in existing readers:](https://github.com/phavx/nasap/blob/master/README.md#things-i-dont-like-in-existing-readers)
* [How does nasap work?](https://github.com/phavx/nasap/blob/master/README.md#how-does-nasap-work)
* [How can I do things my current/some reader does?](https://github.com/phavx/nasap/blob/master/README.md#how-can-i-do-things-my-currentsome-reader-does)
* [What do I need to use it?](https://github.com/phavx/nasap/blob/master/README.md#what-do-i-need-to-use-it)
* [How do I use it?](https://github.com/phavx/nasap/blob/master/README.md#how-do-i-use-it)
* [Contributions](https://github.com/phavx/nasap/blob/master/README.md#contributions)
* [Future](https://github.com/phavx/nasap/blob/master/README.md#future)
* [Authors, Copyright &amp; License](https://github.com/phavx/nasap/blob/master/README.md#authors-copyright--license)

********************************************************************************

### What is nasap?

nasap is a simple tool which fetches RSS/Atom feeds and turns the entries into a
logical structure of plain text files.


### Why yet another feedreader?

nasap itself isn't a reader, it's just a tool to give you content you can
easily read with every viewer you like. Use your favorite text editor (vim,
emacs, ...), a pager (less, most, ...), browser, filemanager (ranger, mc, ...)
or just `cat`.


### Still, why?

Because I think all feedreaders suck and nasap's approach enables pretty much
all of their features by combining standard system tools in a clever way, if and
how you like it.

####Things I don't like in existing readers:

* you need an account on some website (f.e. with Feedly), which enables them
and others behind it (think three letter agencies, marketing companies, etc) to
create a profile of your personal interests, political views and other stuff the
things you're reading are giving away. In my opinion, only the actual source
should be able to know that you are reading it, if at all(use Tor if you don't
like this).

* for most content, the actual text is the most important part, yet crappy
layouts often make it hard to read.

* webinterfaces often are slow and overloaded with distracting crap and they
usually don't work well with text-based browsers (lynx, w3m, ...) - yes, people
still use those.

* you often don't get the full text of a post, so you've got to click through,
which - at it's best - is just an inconvenience.

* often there's no client available for your prefered platform.

* syncing, if at all available, is often done in an intransparent or propriatory
way.

* export/import is sometimes unavailable.

* data is stored in SQL or proprietary formats locally(if at all), which makes
it hard/impossible to use in a way the developers didn't think of - good luck
getting support for a niche feature.

* social experience, it seems it's more about sharing content than actually
reading and making use of it


### How does nasap work?

You pass nasap the URL to a feed, the links to the actual source get extracted,
downloaded and turned into a plain text copy of the full source(so no excerpts).

So f.e., pass "http://blog.example.com/rss.xml" to nasap, it grab's the title
and the links and stores them in

```
"${HOME}/news/blogtitle/[YYYY-MM-DD]-[HH:MM] post title"
```


### How can I do things my current/some reader does?

* **archiving**: create a tarball or some other compressed format of the posts
you need

* **sharing**: addtionally to the full text, the files also contain the
original URL of a post. Pick the parts you need and send them via mail, irc,
instant message, some social media thingy or whatever you want, it's just text.

* **search**: use `grep` (or similar) to search the contents of files, use
`find` or similar to search by time stamps. Or use a desktop search engine like
recoll, strigi or tracker.

* **tagging**: use symlinks, extended attributes (xattr), a tagging filesystem.

* **basic syncing**: copy from device to device using your prefered methods, rsync,
scp, ftp.

* **status syncing**: if you need that, you'll figure it out. Maybe symlinks
with a read/unread folder, access times, ...


### What do I need to use it?

A Linux distribution (OSX probably, but has not been tested by the author)
with the following installed:

* **Python**: currently only 2.{6,7} is supported, Python3 is planned with no
ETA as of right now

* ***other dependencies***:
 - feedparser:  https://pypi.python.org/pypi/feedparser
 - html2text: https://pypi.python.org/pypi/html2text
 - readability: http://github.com/buriy/python-readability


### How do I use it?

For now there is very few documentation as this is still in it's infant stages,
so have a look at the code if it's not obvious(it's pretty simple and
everything configurable is in the top part).

Copy the script to somewhere in your **${PATH}**, then run it with

```shell
nasap "protocol://some.domain.tld/my/feed.xml"
```


### Contributions

All help is welcome, feel free to submitch patches and file bugs. If you'd like
to be credited for your contributions, please also state in which way(realname,
github nick, ...).


### Future

Quite a few things aren't yet working properly or are planned to make it a
better experience, please see the [TODO](https://github.com/phavx/nasap/blob/master/TODO.md) file for details.


### Authors, Copyright & License

The creator and main author is [_avx_](https://github.com/phavx/), contributors
are listed in the [AUTHORS](https://github.com/phavx/nasap/blob/master/AUTHORS) file.

Licensed under [MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2015, avx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
