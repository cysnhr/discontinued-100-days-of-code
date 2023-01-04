//20230104

#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    string text = get_string("Text: ");

    double let, word, sent, index;
    let = word = sent = 0;

    for (int i = 0; text[i] != '\0'; i++) {
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122)) {
            let ++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?') {
            sent ++;
        }
        else if (text[i] == ' ') {
            word ++;
        }
    }

    //for the last word
    word ++;

    //index = 0.0588 * L (av letters per 100 words) - 0.296 * S (av sentences per 100 words) - 15.8
    let = (let * 100) / word;
    sent = (sent * 100) / word;
    index = round(0.0588 * let - 0.296 * sent - 15.8);

    if (index < 1) {
        printf("Before Grade 1\n");
    }
    else if (index >= 16) {
        printf("Grade 16+\n");
    }
    else {
        printf("Grade %.0f\n", index);
    }
}

/*
Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.
*/
