Experiment with gyp
====================

## About
Tiny http server which publishes current directory tree.

## Usage

### Build
```
# Downloads gyp
$ ./setup.sh

# ex. Xcode
$ ./tools/gyp/gyp -f xcode --depth=. myserver.gyp

# ex. Makefile
$ ./tools/gyp/gyp -f make --depth=. myserver.gyp --generator-output=./out/makefiles
```

### Run
```
$ /path/to/myserver
Ctrl + C to stop server.
```
The server listens on TCP port 8080.
