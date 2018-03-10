# sopel-linktitle

Link title script for Sopel IRC bot.

## Installation

Tested on Ubuntu 1604LTS. Requires bs4, requests
```
sudo pip3 install requests bs4
```

In your ~/.sopel/default.cfg or similar disable the url module:
```
[core]
exclude = url
```

## Configuration

Works the same as the url module. `exclude` is a list of regular expressions to
not gather the title of.
```
[linktitle]
exclude = ^https?://.*example.com,https?://www.python.org
exclusion_char = !
...
```

## Testing

```
$ python3 sopel-linktitle/linktitle.py https://github.com/
$ python3 sopel-linktitle/linktitle.py http://www.example.com
$ python3 sopel-linktitle/linktitle.py https://example.com
$ python3 sopel-linktitle/linktitle.py http://www.python.org
$ python3 sopel-linktitle/linktitle.py http://docs.python.org
```

