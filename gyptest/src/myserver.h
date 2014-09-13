#ifndef MYSERVER_H_
#define MYSERVER_H_

#include <stdbool.h>
#include <stdint.h>

typedef struct myserver {
    char *doc_root;
    char *port;
} myserver;

extern myserver * myserver_create(const char *doc_root, const char *port);

extern int32_t myserver_poll_request(myserver *x, int32_t msec);

extern void myserver_free(myserver *x);

#endif
