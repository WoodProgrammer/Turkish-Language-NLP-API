from __future__ import print_function
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import nltk

def Split_Sentence(sentence):
    verb=sentence.split()
    array=[]
    for i in range(0,len(verb)):
        if i+1<len(verb):
            verbs = verb[i]+" "+verb[i+1]
            array.insert(i,verbs)

    return array

def HowMamyVerbinText2(text):
    f = open('database', 'a')
    hm=0

    text = Split_Sentence(text)
    print (text)
    for i in range(0,len(text)):
        for j in range(0,len(text)):
            if text[i]==text[j]:
                hm+=1
        print (text[i]+" "+str(hm),file=f)
        hm=0

def HowMamyVerbinText(text):
    f = open('database', 'a')
    hm=0

    text = nltk.word_tokenize(text)
    print (text)
    for i in range(0,len(text)):
        for j in range(0,len(text)):
            if text[i]==text[j]:
                hm+=1
        print (text[i]+" "+str(hm),file=f)
        hm=0


text = """The Eurovision Song Contest has hit a major road bump, after 21 top level staff organising the event resigned.
The Ukrainian Eurovision team say they were stripped of major responsibilities in December, when a new boss was appointed to the organising committee.
According to their resignation letter, they were "completely blocked" from making decisions about the show.
The EBU, which founded Eurovision, told Ukraine's public broadcaster to "stick to the timeline" despite the upheaval.
It insisted the event would go ahead as planned in Kiev this May. Among the team members who resigned were two executive producers of this year's show.
All the staff were appointed by the Ukraine Public Broadcaster (UA:PBC), which is organising the contest after Ukrainian singer Jamala won last year's event with the song 1944.
In an open letter published by Strana, the team said: "Hereby we, the Eurovision team, for whom this contest has become not only part of our work but also part of our life, officially inform that we are resigning and stopping work on preparations for the organisation of the contest."
line break
Analysis: Is the contest in jeopardy?
Putting on the Eurovision Song Contest is a huge undertaking. In 2010, Norwegian broadcaster NRK had to ditch the World Cup because it couldn't afford to pay Fifa and foot the bill for Eurovision at the same time.
In Ukraine, the task has proved even more problematic. The decision over which city would host the show was delayed three times and there were even rumours the contest would be moved to Russia.
Now, with just three months to go, the core team has quit. They've been at loggerheads with their boss, who they claim has been blocking all of their decisions. They also say there have been problems finalising contracts with subcontractors. At worst, that could include the teams who build the stage.
The show must go on - and the EBU, which has organised the contest since 1956, has the financial and political muscle to make sure it does. But it will be interesting to see how close to the wire it gets.
line break use of it could
They said preparations "stopped for almost two months" after the appointment of Eurovision co-ordinator Pavlo Hrytsak last year, adding, "the work of our team was completely blocked".
In a statement, it added: "We have reiterated to UA:PBC the importance of a speedy and efficient implementation of plans already agreed, despite staff changes and that we stick to the timeline and milestones that have been established and approved by the Reference Group to ensure a successful Contest in May."
This year's Eurovision Song Contest final is due to take place in Kiev on 13 May.
Britain will be represented by former X  it could Factor contestant Lucie Jones in this year's competition. The Welsh singer was chosen by a public vote after performing her ballad, Never Give Up On You, on BBC Two's Eurovision: You Decide.
The song was co-written by Danish star Emmelie de Forest, who won the Eurovision Song Contest 2013 with the song Only Teardrops.
'Dancing on tombstone' ('use of', 1.0) it could
There has already been controversy over the decision to hold the Eurovision opening ceremony in the Saint Sophia complex, a well-known religious landmark which dates back to the 17th Century.
The use of the venue was called "blasphemy" by the Ukrainian Orthodox Church of Moscow Patriarchy.
" From all viewpoints, this is a very bad decision," Andrei Kurayev, a prominent deacon of the Russian Orthodox Church, was quoted as saying by Mosokovski Komsomolets. "Now, on the tombstone of [Mstislav I of Kiev], there will be dances."
Later, Zurab Alasania, head of Ukraine's national TV and radio company, resigned amidst reports that the country was having troubles financing the song contest.
it could"""
HowMamyVerbinText2(text)
HowMamyVerbinText(text)
