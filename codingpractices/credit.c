#include <cs50.h>
#include <stdio.h>
#include <math.h>

//please don't laugh at me I'm still working on it :/

int count(long num);
int getFirstTwo(long num);
int checksum(long num);
long power(long a, int b);

int main(void)
{
    int cnt, total, i;
    int tmp = 0;
    long num = 4003600000000014;
    int numbers[0];

    cnt = count(num);
    tmp = total = 0;

    for (i = 1; i <= cnt; i += 1) {
        //12345678
        //i=7
        //...i=1
        //num % 10^7 = 8
        tmp = num % power(10, i);
        printf("%i time loop: %li divided by %li remains %i\n", i, num, power(10,i), tmp);
        //0 + 8 * 2
        total += tmp * 2;
    }

    printf("%i\n", total);

}


long power(long a, int b) {
    int mult = a, i = 0;
    //a ^ b
    while (i < b-1) {
        //10^2
        a *= mult;
        i += 1;
        //1
        //10 . 10
    }

    return a;
}

int count(long num) {
    int count = 0;

    while (num != 0) {
        num /= 10;
        count += 1;
    }

    return count;
}

/*

long num;
    int c, count, res;
    num = get_long("Input: ");

    res = checksum(num);
    printf("%i", res);


int getFirstTwo(long num) {

    while (num > 100) {
        num /= 10;
        //1300 / 10 = 130
        //gets first digit
    }

    return num;
}


int checksum(long num) {

    int c, tmp, total, i;

    c = count(num);
    tmp = total = 0;

    for (i = c - 1; i -= 2 ; i >= 0) {
        //12345678
        //i=7
        //...i=1
        //num % 10^7 = 8
        tmp = num % pow(10, i);
        //0 + 8 * 2
        total += tmp * 2
    }

    return total;
}
*/
