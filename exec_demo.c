#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Executing ls command using execvp...\n");

    char *args[] = {"ls", "-l", NULL};
    execvp(args[0], args);

    printf("Exec failed!\n");
    return 0;
}
