# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 18:17:04 2014

@author: swoop
"""

import keyptsummarizer as smrzr

#summarize directly from link
def sumItUp(url):    
    human_summary, key_points = smrzr.summarize_url(url, fmt="md")
    print human_summary
    print key_points

#provide text on your own
#text = u'''Europe has an estimated 421 million fewer birds than three decades ago, and current treatment of the environment is unsustainable for many common species, a study released on Monday said.\n\nThe population crash is related to modern farming methods and the loss and damage of habitats, according to the study published in science journal Ecology Letters.\n\n"This is a warning from birds throughout Europe. It is clear that the way we are managing the environment is unsustainable for many of our most familiar species," said Richard Gregory of the Royal Society for the Protection of Birds, which co-led the study.\n\n"The conservation and legal protection of all birds and their habitats in tandem are essential to reverse declines."\n\nThe study found that about 90 percent of the decline occurred in the most common bird species, including grey partridges, skylarks, sparrows and starlings.\n\nMeanwhile the population of some rarer birds had increased in recent years, likely due to conservation efforts and legal protections.\n\nSuch a decline in common birds is concerning as "it is this group of birds that people benefit from the most", according to University of Exeter researcher Richard Inger.\n\n"Significant loss of common birds could be quite detrimental to human society," Inger said.\n\nThe scientists estimated the loss of bird populations by analysing data on 144 species of European birds, collected from surveys in 25 countries, often by voluntary fieldworkers.\n\nResearchers urged increased conservation through large-scale environmental improvement, such as urban green space projects and environmental farmland schemes.'''
#key_points = smrzr.summarize_text(text, fmt="raw")
