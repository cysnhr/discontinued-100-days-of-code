# 100 Days Of Code - Log

### Day 1: Jan 1, 2023

**Today's Progress**: Came across LeetCode and did one question before bed.

**Thoughts:** I keep making dumb mistakes like messing up variable names or forgetting commas. I don't know why I rely on for loops so much, to the extent of implementing a double for loop here. I wish as I go further into these 100 days I'd stop doing it. Even though it doesn't really matter that much right now because the list is short.
an alternative for linear search is `if (something) in (something)`

**Link to work:** https://leetcode.com/problems/two-sum/submissions/869137150/

### Day 2: Jan 2, 2023

**Today's Progress**: Got stumped on data structures. Arghh it's a mess and me coding for one hour basically consists of 5 minutes staring at the question 5 minutes writing code 50 minutes figuring out what dumb mistake I made. 

**Thoughts:** Today I tried to code a linked list problem (see below) but I don't think I really get what they're about. Even after staring at the solutions other people are offering. I need to actually learn linked lists. Fortunately I found a great source which is Coderbyte but I still have so much homework I haven't finished.

**Link to work:** https://leetcode.com/problems/add-two-numbers/description/ (It's only the description because I'm not finished and the progress looks really bad.)

### Day 3: Jan 3, 2023

**Today's Progress**: Learned about linked lists on [Coderbyte](https://coderbyte.com/video/the-basics-of-linked-lists). Wrote code for CS50 Problem Set 1 but is missing one tiny part where I can't identify Mastercards. Will probably finish it off tomorrow.
(update 1hr later) YESSS I FINISHED IT they're little mistakes that I'm going to comment in the [code section](./codingpractices/credit.c).

**Thoughts:** I wrote something which is better than nothing...? Also coding while eating dinner is probably not so good for digestion because I felt and it's not because of the constant errors. But all this took wayyy too much time, like, I just forget time passing when I'm writing this, and I need to manage my time better--should try the pomodoro technique. 

**Link to work:** the code section up there and [https://cs50.harvard.edu/x/2023/psets/1/credit/](https://cs50.harvard.edu/x/2023/psets/1/credit/)

### Day 4: Jan 4, 2023

**Today's Progress**: Finished another assignment from CS50 -- [readability](./codingpractices/credit.c). 

**Thoughts:** I made less stupid mistakes today and timed myself. Honestly, before starting this challenge I thought coding for an hour was difficult to excede, but how I'm wrong. It makes me forget time :) I know it's probably easier but I felt better after coding this. Okay I'll start to learn about linked lists again tomorrow.

**Link to work:** the code section up there and [https://cs50.harvard.edu/x/2023/psets/1/credit/](https://cs50.harvard.edu/x/2023/psets/2/readability/)

### Day 5: Jan 5, 2023

**Today's Progress**: Eek I was trying to code linked lists but things aren't really working out that well. I don't know why they're only giving me memory addresses and forgot to create a list instance first which led to a lot of wasted time. But I did find out more about linked lists which is pretty nice.

**Thoughts:** I have coded for more than two hours and I figured it is the effort that counts, and I need to go study now. Let's see if I'll come to some grand realization tomorrow.

**Link to work:** [linked_list](./codingpractices/linked_list.py)

### Day 6: Jan 6, 2023

**Today's Progress**: Gosh I just found out how objects really worked. Still haven't figured out why that linked list keeps passing in NoneTypes so frankly not a great deal of progress today.

```
>>> class Random:
      def __init__(self, value):
          self.value = value

        
>>> Random(24)
output: <__main__.Random object at 0x103d91f30>

>>> Random(24).value
output: 24
```
When you ask for an object, it only gives you an address. I felt foolish for not knowing this but I'm glad I do now.
(update: it's way past my sleep time and I have gotten the correct output much thanks to https://www.youtube.com/watch?v=FSsriWQ0qYE this lovely creator but I still don't know why and I'm going to try finding out tomorrow. Also I worry that the code might be too similar (yup because I'm super bad at this apparently) so I'd better try writing it again tomorrow. Is there a problem with plagarizing code while citing the creator?)

**Thoughts:** I'm getting frustrated with myself and I need to force myself to code only during a certain time. Also I asked a lot of people but they didn't know either so. I guess. I'm not exactly alone in the world.

**Link to work:** err, no work? just a nice fun day of failed debugging. still I tried really hard to figure out the problem so here it is. [linked list debug 1](/codingpractices/linked_list_debug_1.py). ([correct ver](/codingpractices/linked_list_debug_2.py)) Also I tried looking up other people's 100 days of code log but it looks like I'm the only one with this much useless stuff to talk about.  

### Day 7: Jan 7, 2023

**Today's Progress**: Not much. Bawled over the linked list again without a conclusion. 

**Thoughts:** Maybe I should try another way although not knowing why I'm wrong stresses me out. And this whole thing is taking up wayy too much time.

**Link to work:** [linked list debug](./codingpractices/linked_list_debug.md)

### Day 8: Jan 8, 2023

**Today's Progress**: I spent four and a half hour taking a CS test and my eyes hurt.

**Thoughts:** There's one question I was unable to get right even though I think I made a lot of sense. Argh. Confirmation bias. Blind to my own blindness. (it's not meant to sound this cynical)

**Link to work:** [that for loop](./codingpractices/for_loop.py)


### Day 9: Jan 9, 2023

**Today's Progress**: I picked up a piece of code from a long time ago that looked for prime factors.

**Thoughts:** Can I just laugh at myself for a moment. Also there's a math test tomorrow and somehow I can't hit enter in replit so I don't have the patience to work with my computer like that. Though I did reach the one hour benchmark even if I didn't finish the code. (Like, spent 40 minutes staring at what I've written and laughing at it.)

**Link to work:** [prime factor](./codingpractices/prime_factor.py)

### Day 10: Jan 10, 2023

**Today's Progress**: I was finally able to get the correct prime numbers but unable to format them accordingly. (It's asking for the `a ^ b * c` kind of format. And lists are just.)

**Thoughts:** Time's up and I've gotta move because I fear I'd fail stuff. Also I decided to organize my mistakes into a new directory. Aaand yes I do remember the linked list.
(update 1 hr later) (I keep doing this don't I) Ahhh I figured it out and wrote an add function + repr all by myself. So proud.

**Link to work:** [prime factor mistakes collection](./mistakes/prime_factor.md)

### Day 11: Jan 11, 2023

**Today's Progress**: Ooh I made the prime factor thing work. 

**Thoughts:** Happy. I'll be thinking about the linked list. How do I make it go backwards?

**Link to work:** [prime factor mistakes collection](./mistakes/prime_factor.md), [prime factor](./codingpractices/prime_factor.py)

### Day 12: Jan 12, 2023

**Today's Progress**: I wrote a clear function for the linked list, and picked up that leetcode question where I left it off, believing I have newfound knowledge for the data structure.

**Thoughts:** Except the input is a whole class of itself and everything I did, writing my own linked list, didn't really help the question except got me to understand linked lists better. I ended up turning list nodes into lists then lists into nodes again. Stuck on the last part. Aaaand let's see if I'll be able to finish studying physics today, doubtful.

**Link to work:** [add two numbers](./mistakes/add_two_numbesr.py)

### Day 13: Jan 13, 2023

**Today's Progress**: Decided to put linked lists aside for now. I don't think converting them to lists and back again is how it's supposed to work.

**Thoughts:** My brain physically hurts and I'm nowhere near the level of a programmer looking for a job so let's start smaller. I'm gonna get back into that python course that invited me to the world of programming but I never got to finish.

**Link to work:** [add two numbers](./mistakes/add_two_numbesr.py)

### Day 14: Jan 14, 2023

**Today's Progress**: Learned about recursions, space complexity, auxiliary space. Attempted another LeetCode question.

**Thoughts:** Ow. My ego is hurt by my own stupidity.

**Link to work:** [palindrome](./mistakes/palindrome.md)

### Day 15: Jan 15, 2023

**Today's Progress**: Tried scientific computing with python course on freecodecamp.org but got stuck on booleans harharhar. More debugging to do tomorrow.

**Thoughts:** Finals the day after tomorrow. I'm proud of myself for being here.

**Link to work:** [arithmetic operator](./codingpractices/arithmetic_formatter.py)

### Day 16: Jan 16, 2023

**Today's Progress**: It ran fine on another replit file but couldn't pass the test. I posted a question on the forum which I see as something to be proud of because I'm scared of humans.

**Thoughts:** Finals tomorrow.

**Link to work:** [arithmetic operator mistakes](./mistakes/arithmetic_formatter.md)

### Day 17: Jan 17, 2023

**Today's Progress**: Solved it, was a little mistake. Started a little on Tkinter. I'll go do more of that scientific course tomorrow.

**Thoughts:** More finals tomorrow.

**Link to work:** [arithmetic operator mistakes](./mistakes/arithmetic_formatter.md)

