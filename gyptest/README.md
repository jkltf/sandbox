Experiment with gyp
====================

## Usage
```
# Downloads gyp
$ ./setup.sh

# ex. Xcode
$ ./tools/gyp/gyp -f xcode --depth=. myserver.gyp

# ex. Makefile
$ ./tools/gyp/gyp -f make --depth=. myserver.gyp --generator-output=./out/makefiles
```
