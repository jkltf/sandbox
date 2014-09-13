#include <myserver.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    myserver *ms = myserver_create(".", "8080");
    if (!ms) {
      puts("Error.");
      return 1;
    }

    puts("Ctrl + C to stop server.");
    for (;;) {
        myserver_poll_request(ms, 1000);
    }
    puts("Stopping ...");

    myserver_free(ms);
    return 0;
}
