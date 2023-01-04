//20230103

#include <cs50.h>
#include <stdio.h>
#include <math.h>

int count(long num);
int first_two(long num);
//for verifying type of credit card
int checksum(long num);
//luhn's algorithm

int main(void)
{
    int c, rand;
    long num = get_long("Number: ");
    //a function in the cs50 library

    rand = checksum(num);
    //true or false, 1 or 0
    if (rand != 1) {
        printf("INVALID\n");
        return 0;
        //ends main
    }

    rand = first_two(num);
    c = count(num);

    if ((c == 15) && ((rand == 34) || (rand == 37))) {
        //american express features
        printf("AMEX\n");
    }
    else if ((c == 13) || (c == 16)) {
        if ((rand >= 51) && (rand <= 55)) {
            //not all cases but still
            printf("MASTERCARD\n");
        }
        else if ((rand < 50) && (rand > 39)) {
            printf("VISA\n");
        }
        else {
        printf("INVALID\n");
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
        //cancels last digit.
        count += 1;
    }

    return count;
}

int first_two(long num) {

    while (num > 100) {
        num /= 10;
        //gets the 
        digits less than 100 after multiple divisions with 10
    }

    return num;
}

int checksum(long num) {
    int remain, even_total, odd_total, tmp, c;

    even_total = odd_total = 0;
    c = count(num);

    for (int i = 1; i <= c; i += 1) {
        //gets first digit counting from the end assigned to remain
        remain = num % 10;
        num /= 10;

        //remember indent if you want this to be in the loop!!
        if (i % 2 != 0) {
            odd_total += remain;
            //odd is stuff no add
        }
        else {
            remain = 2 * remain;
            if (remain % 10 >= 0) {
                //for seperating the two digits
                tmp = remain % 10;
                //gets the second digit
                even_total += tmp;
                remain /= 10;
                even_total += remain;
                //adds both digits to the total
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
