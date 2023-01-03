#include <cs50.h>
#include <stdio.h>
#include <math.h>

int count(long num);
int getFirstTwo(long num);
int checksum(long num);

int main(void)
{
    int c, rand;
    long num = get_long("Number: ");
    //4003600000000014

    rand = checksum(num);
    if (rand != 1) {
        printf("INVALID\n");
        return 0;
    }

    rand = getFirstTwo(num);
    c = count(num);

    if ((c == 15) && ((rand == 34) || (rand == 37))) {
        printf("AMEX\n");
    }
    else if ((c == 13) || (c == 16)) {
        if ((rand == 51) || (rand == 52) || (rand == 53) || (rand == 54) || (rand == 55)) {
            printf("MASTERCARD\n");
        }
        else {
            printf("VISA\n");
        }
    }
    else {
        printf("INVALID\n");
    }
    return 0;
}



int count(long num) {
    int count = 0;

    while (num != 0) {
        num /= 10;
        count += 1;
    }

    return count;
}

int getFirstTwo(long num) {

    while (num > 100) {
        num /= 10;
        //1300 / 10 = 130
        //gets first digit
    }

    return num;
}

int checksum(long num) {
    int remain, even_total, odd_total, tmp, c;
    even_total = odd_total = 0;

    c = count(num);
    for (int i = 1; i <= c; i += 1) {
    //big for loop starts
    //1203
    remain = num % 10;
    num /= 10;
    if (i % 2 != 0) {
        odd_total += remain;
        //odd is stuff no add
    }
    else {
        remain = 2 * remain;
        //12
        if (remain % 10 > 0) {
            //true.
            tmp = remain % 10;
            //tmp = 2
            even_total += tmp;
            //tot + 2
            remain /= 10;
            //1
            even_total += remain;
        }
        else {
            even_total += remain;
        }
    }
    }

    if ((even_total + odd_total) % 10 == 0) {
        return 1;
    }
    else {
        return 0;
    }

}
