#include <mongoose.h>
#include <myserver.h>
#include <stdlib.h>
#include <string.h>

typedef struct server_impl {
    myserver mys;
    struct mg_server *mgs;
} server_impl;

myserver * myserver_create(const char *doc_root, const char *port) {
    server_impl *impl = 0;
    myserver *x = 0;

    if (!(impl = (server_impl *)malloc(sizeof(server_impl)))) {
        return 0;
    }
    memset(impl, 0, sizeof(server_impl));

    x = &impl->mys;
    x->doc_root = (char *)malloc(strlen(doc_root) + 1);
    if (!x->doc_root) goto error;
    strncpy(x->doc_root, doc_root, strlen(doc_root) + 1);

    x->port = (char *)malloc(strlen(port) + 1);
    if (!x->port) goto error;
    strncpy(x->port, port, strlen(port) + 1);

    impl->mgs = mg_create_server(0, 0);
    if (!impl->mgs) goto error;
    mg_set_option(impl->mgs, "document_root", x->doc_root);
    mg_set_option(impl->mgs, "listening_port", x->port);

    return (myserver *)impl;

error:
    if (impl->mgs) mg_destroy_server(&impl->mgs);
    if (x) {
      if (x->port) free(x->port);
      if (x->doc_root) free(x->doc_root);
    }
    free(impl);
    return 0;
}

void myserver_free(myserver *x) {
    server_impl* impl = (server_impl *)x;

    if (!impl) return;
    if (impl->mgs) mg_destroy_server(&impl->mgs);
    if (x->port) free(x->port);
    if (x->doc_root) free(x->doc_root);
    free(impl);
}

int32_t myserver_poll_request(myserver *x, int32_t msec) {
    server_impl *impl = (server_impl *)x;
    return mg_poll_server(impl->mgs, msec);
}
