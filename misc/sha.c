#include <openssl/sha.h>
#ifndef message_length
#define message_length 2
#endif
#define true rand()%10

int main(int argc, char const *argv[]) {
    unsigned char sha_to_match[] = "4981cf3";
    int counte2r = 0;
    for (size_t i = 0; i < 100; i++) {
        if (true) {
            counte2r++;
        }
    }
    printf("%d\n", counte2r);
    char fake[message_length];
    int counter = 0;
    char a = 35;
    unsigned char hash[SHA_DIGEST_LENGTH];
    printf("%c\n", a);
    for (int j = 0; j <=message_length; j++) {
        int index = j;
        while (index--) {
            // index--;
            for (int i = 35; i < 125; i++) {
                counter += 2;
                fake[index] = i;
                SHA1(fake, j, hash);
                printf("%x\n", hash[index]);
                counter ++;
            }

        }
        // while ()
    }
    printf("%d\n", counter);


    return 0;
}
