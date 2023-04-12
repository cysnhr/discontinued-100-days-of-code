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

### Day 18: Jan 18, 2023

**Today's Progress**: Started on the new one. I didn't exactly reach one hour but I'll add it up tomorrow.

**Thoughts:** No more finals. For like one month. Yay. I do find myself coding quicker. A little I hope.

**Link to work:** [time calculator](./codingpractices/time_calculator.py)

### Day 19: Jan 19, 2023

**Today's Progress**: All that's left is debugging.

**Thoughts:** I didn't fail anything in the finals. How wonderful.

**Link to work:** [time calculator](./codingpractices/time_calculator.py)

### Day 20: Jan 20, 2023

**Today's Progress**: The code looks even more complicated.

**Thoughts:** I think the more I try to debug, the more I mess up my logic.

**Link to work:** [time calculator](./codingpractices/time_calculator.py)

### Day 21: Jan 21, 2023

**Today's Progress**: Done. Started on the next project and got a little confused about classes but kinda picked it up again?

**Thoughts:** It's not clean code but it works. And also there are a lot of rules in the requirements so I guess that makes up for excuses.

**Link to work:** [budget](./codingpractices/budget.py)

### Day 22: Jan 22, 2023

**Today's Progress**: More progress. Yay. 

**Thoughts:** Formatting output is frustrating. I'll do more on my flight tonight.

**Link to work:** [budget](./codingpractices/budget.py)

### Day 23: Jan 23, 2023

**Today's Progress**: Jet lagged.

**Thoughts:** I feel dead.

**Link to work:** the work is so tiny and wrong, even, for me to put it up.

### Day 24: Jan 24, 2023

**Today's Progress**: Debug tomorrow.

**Thoughts:** I feel better today but this code seems really memory usage inefficient and stuff. Also it doesn't pass the test so more debugging tmr.

**Link to work:** [budget](./codingpractices/budget.py)

### Day 25: Jan 25, 2023

**Today's Progress**: Caught that bug.

**Thoughts:** _A LOT_ of spacing problems that are just dumb (okay I can't blame anyone except for myself) and wrong approximation stuff, me being lazy and overlooking important things and all that.

**Link to work:** [budget mistakes](./mistakes/budget.md)

### Day 26: Jan 26, 2023

**Today's Progress**: Finished next project. I completely forgot  class inheritance.

**Thoughts:** Yay.

**Link to work:** [polygon area calculator](./codingpractices/polygon_area_calculator.py)

I had a fever and a lot of stuff happened. To recount them in detail may make me sound like I'm whining. But now I'm back in Taiwan and back here :)

### Day 27: Feb 06, 2023

**Today's Progress**: Struggling on final project.

**Thoughts:** I'm trying to pick up what coding feels like, after, what, a week away? Maybe failing but I'll get there eventually. I think this project is a little challenging.

**Link to work:** [probability calculator](./codingpractices/probability_calculator.py)

### Day 28: Feb 07, 2023

**Today's Progress**: Corrected the __init__ method. Turns out I misunderstood stuff.

**Thoughts:** HOW, how do I remove things from a list at random? (I think I got it (after an hour), corrected the draw method as well.)

**Link to work:** [notes on probability calculator](./mistakes/notes_prob_calculator.md)

I hope forgetting doesn't become a habit. I need to build my daily coding habit again :(

### Day 29: Feb 09, 2023

**Today's Progress**: I cannot believe that I did not know creating a variable that has its value assigned to another variable is only a new reference and not a new variable with a new memory address. 

```python
import copy

original = [1, 2, [3, 4]]
assigned = original
s_copy = original.copy()
d_copy = copy.deepcopy(original)

print(assigned, s_copy, d_copy)
>>> [1, 2, [3, 4]] [1, 2, [3, 4]] [1, 2, [3, 4]]
print(id(assigned))
>>> 4370730432
print(id(original))
>>> 4370730432
print(id(s_copy))
>>> 4418536192
print(id(d_copy))
>>> 4418518272
```

The value of shallow copies will be modified if the original variable is changed. Deep copies do not get affected.
BUT! If a variable is an integer and b = var, b is the same as var, but then when b undergoes an arithmetic operation, b becomes a new thing.
It's called **binding**, I learned.

**Thoughts:** I FINISHED THE COURSE. (The challenges, more like, and I didn't even write that perfect code BUT STILL.)

**Link to work:** HAHAHA I'm proud to put this on https://www.freecodecamp.org/certification/cysnhr/scientific-computing-with-python-v7. It's such a nice community, I must say, I got so much help from the forum even without posting a lot. I love how there's so much activity and no one is shy to ask questions.

### Day 30: Feb 10, 2023

**Today's Progress**: I was watching tutorials and it became 2/11.

**Thoughts:** I don't really get TKinter yet, let's see how long it's going to take for me.

**Link to work:** uh. youtube?


### Day 31: Feb 11, 2023

**Today's Progress**: Started on a productivity project.

**Thoughts:** Still don't get it.

**Link to work:** [time management project](./codingpractices/time_management.py)

### Day 32: Feb 12, 2023

**Today's Progress**: Started notetaking.

**Thoughts:** I tried to code but can't remember all the attributes and stuff so noted them down. However not coding seems like cheating and I don't want to spend so much of my 100 days notetaking like this. So now I will count two notetaking days as one. Also it's been a month, wow. Although not consecutive, stull impressive for me.

**Link to work:** [tkinter notes](./notes/tkinter.md) 

2/13 sorry I need to take a short break to get school stuff in order. School started today and I don't know why there are so many things to tend to. be back in a week at most.
2/22 Due to more unexpected issues in school, I must prioritize and halt the challenge. I will continue it, however, in the future. A few more weeks later, maybe? Does this count as failure, should I start a new project, a new round?

### halted 2/12
### started 3/19

### Day 33: Mar 19, 2023

**Today's Progress**: Finished that nagging palindrome question.

**Thoughts:** I love Youtube. So I've been reading about Carol Dweck's growth mindset. So I'm back. I know this challenge is meant for one to continue on the course on 100 days but I might miss a day or two because of the hectic schedule. Point is, I'm back, and I'm excited to see how I might end up like. (Hey but I'm only going to start with the easy problems first because I don't think I have a good basic. Also I want to try coding in C.)

**Link to work:** [palindrome](./mistakes/palindrome.md) 

### Day 33.5: Mar 20, 2023

**Today's Progress**: Started on roman to integer code.

**Thoughts:** Can't manage one hour per day. I'll cut up my days so I won't be taking advantage of this self evaluated challenge.

**Link to work:** [roman to integer](./mistakes/rm_to_int.md) 

### Day 34.0: Mar 21, 2023

**Today's Progress**: Tinkered with it in class.

**Thoughts:** Eek. (nonsensical sound)

**Link to work:** [roman to integer](./mistakes/rm_to_int.md) 

exam in two days. lemme take four days off

### Day 35: Mar 26, 2023

**Today's Progress**: I tinkered with my Raspberry Pi for three hours, successfully installing and setting up ssh and vnc which means I'm now able to access the device from my macbook, but I do look quite funny accessing a computer from another one. Also I finally learned how to make led lights from breadboards light up, though I'm still not exactly sure how those circuits work. I was so afraid it'd start melting everything down but fortunately it did not.

**Thoughts:** I think I have mistakenly written down my thoughts in the progress so.

**Link to work:** no link

graduation trip for four days

### Day 36: Apr 2, 2023

**Today's Progress**: More Raspberry Pi.

**Thoughts:** More failed attempts. Somehow I have only 1GB left on the disk and I can't install PyCharm. I spent a lot of time with ChatGPT trying to figure out how to empty my trash can.

**Link to work:** no link

### Day 37: Apr 3, 2023

**Today's Progress**: Went back to the Roman to Integer thing and solved it. Started on second FreeCodeCamp.org course with data structure thingys by Javascript. It said I finished 28% already :)

**Thoughts:** I was about to give up because I figured using for loops is too stupid. But then I looked at the previous codes I wrote and figured I could probably do it. It's still a dumb inefficient solution so I went to Youtube to check out what other people wrote. I'll make the notes in the link to work below.
I love how interactive the lessons FreeCodeCamp.org offers, like coding right next to the instructions.

**Link to work:** [roman to integer](./codingpractices/roman_to_integer.py) 

### Day 38: Apr 4, 2023

**Today's Progress**: I'M PROUDDDDDD

**Thoughts:** I finished that alarm project, finally! My eyes hurt and I love Stack Overflow and Chat GPT and Google.

**Link to work:** [Raspberry Pi alarm](./alarm.py) 

### Day 39: Apr 5, 2023

**Today's Progress**: Solved the binary search. I love YouTube coding tutorials (https://www.youtube.com/watch?v=9q0k3OyCKPY). Started on another thingy that requires sorting but I forgot all about these algorithms. 50% progress on javascript course.

**Thoughts:** Tomorrow after getting to school I'm going to borrow an algo book from a classmate. Meanwhile I don't think I understand the execution of the binary search 100%. Imma keep thinking until I understand it.

**Link to work:** [binary search](./mistakes/binary.c) 

### Day 39.1: Apr 6, 2023

**Today's Progress**: Went to the dentist tonight so didn't do anything. But I had someone write me the code for merge sort and I'm now staring at it in wonder.

**Thoughts:** From time to time I just have to be amazed at how weirdly cool programming is.

**Link to work:** ehhh I didn't do anything

### Day 40: Apr 8, 2023

**Today's Progress**: I found out that the code involved pointers and realized that I have such a terrible foundation so I'm going back to CS50. I'm going to get better at this I promise. (Like, a promise to myself.)
Wrote a bubble sort, passed all test cases but took too long.

**Thoughts:** I'm going to do the practice problem set, lab set, and problem set 3. I'm going to understand algorithms arhhghh I can do this.
Ooh also I was reading the README file for this challenge then realized it actually said to "push code onto GitHub" harharhar I'm not working on projects I'm just trying to grasp the basics. (sobs

**Link to work:** [buuble sort](./codingpractices/bubble.c) 

### Day 41: Apr 9, 2023

**Today's Progress**: Trying to understand that recursive thing and trying to download visual studio code and configure it properly. Failed both.
Also I finally figured out what is the difference between ++i and i++: 
`int i = 5;
int j = i++; // j will be assigned the value of i (5), and then i will be incremented to 6
`
`
int i = 5;
int j = ++i; // i will be incremented to 6 before j is assigned the new value of i (6)
`

**Thoughts:** Uhhhh nope my brain is not working now
1hr later
OKAY WAIT I FINALLY UNDERSTAND THE CONFIGURATION IS FOR EVERY DIFFERENT FILE I'm so sorry for yelling at ChatGPT in all caps I'm sorry but thank you so much for getting me out here. I've never coded with debugging ever before and this is one of the greatest inventions I've ever known. (yup finished the recursive thing

**Link to work:** [thinking abt atoi](./mistakes/atoi.md) / [done](./codingpractices/atoi.c) 

### Day 41.5: Apr 9, 2023

**Today's Progress**: 65% on Javascript intro.

**Thoughts:** i don't get vscode 

**Link to work:** uhhh no?

### Day 41.5: Apr 10, 2023

**Today's Progress**: I'm not going to lie but I really didn't do anything and I don't get how VSCode debugging works ahhhh

**Thoughts:** i don't get vscode still

im not going to bring my laptop home for three days straight because i need it there + it's too heavy + i need less distraction. I always end up watching Youtube after the hour of coding passes.