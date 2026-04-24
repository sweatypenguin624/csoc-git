#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){

    srand(time(NULL));

    int min = 50;
    int max = 100;

    int ranum1 = (rand() % (max - min + 1)) + min;
    int ranum2 = (rand() % (max - min + 1)) + min;
    int ranum3 = (rand() % (max - min + 1)) + min;

    printf("%d %d %d", ranum1, ranum2, ranum3);

    return 0;
}