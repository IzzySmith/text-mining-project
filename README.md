# text-mining-project

### Summary

The drug experience website https://erowid.org/experiences/ is mined with bs to gain an insight into whether there are gender disparities regarding drug use, and if there are common themes among drug users. 

### Introduction

Psychoactive, or psychadelic drugs, such as mushrooms and LSD, are believed by many users to enhance conciousness, giving practitioners a spiritual, or even religious, experience (Letcher, 2007. Watts, 1968). Entrenched in indigenous culture, the use and popularity of these drugs is growing globally, despite prohibition, (Letcher, 2007. Rager, 2013). According to Letcher, practitioners experiences' with these drugs are "weighted", meaning that many people encounter similar hallucinations whilst on these drugs.  According to my own research, psychadelic drugs are amongst the most popular recreational drugs across both genders (see figure 1). What is it about the experiences people have on these drugs that make them so popular? Do people have shared or similar experiences? Is there a common goal or experience that these drug users strive for?

In order to answer these questions I will datamine the Erowid experience vaults. This database is built on drug users documenting their own personal experiences, and therefore provides valuable insights into the popularity and the appeal of such substances. 

### Methods

Each of the experiences were downloaded, and processed using beautiful soup. Initially a dict was created in the form of:

```
{experience_id {drug: gender}}
```

The genders were seperated into male and female, and charts made to compare whether drug use differed across users:

![female_drugs](https://github.com/IzzySmith/text-mining-project/blob/master/female_top5.png "Female drugs")

![male drugs](https://github.com/IzzySmith/text-mining-project/blob/master/maledrugs_cropped2.png)

As you can see the differences are not substantial. Mushrooms and LSD are amongst the most popular drugs used, and therefore highlights the relevance of my research question. 

The next step was to find all the reports which related to Mushrooms and LSD, and a count of the most frequent words was made. The text was lowered and stopwords removed, however more text processing could be done here to improve results:

print word_count(tokenised).most_common(30)

[('like', 115720), ('would', 85580), ('felt', 84980), ('could', 69560), ('one', 65020), ('time', 64560), ('back', 61120), ('around', 52980), ('trip', 47460), ('started', 47440), ('get', 46260), ('really', 44680), ('got', 42820), ('went', 40700), ('feel', 40300), ('looked', 39840), ('thought', 39520), ('still', 38980), ('me.', 38760), ('go', 38640), ('seemed', 38000), ('going', 36560), ('see', 35500), ('began', 35440), ('everything', 35360), ('feeling', 34460), ('much', 32760), ('first', 32560), ('decided', 32080), ('even', 32000)]

As you can see the majority of the 30 most common words can be discarded, and if there is time, more work will be done to improve this. 

Finally, a (initially small) selection of words associated with spiritualism (as taken from wikipedia) and there subsequent word frequencies were found, and graphed:

```
spiritual_words = ['god', 'spirit', 'heaven', 'hell', 'universe','magic','atheist', 'creation', 'concious', 'exist']
```

![spirit word graph](https://github.com/IzzySmith/text-mining-project/blob/master/spriritwords_cropped.png)

### Conclusion
The initial text processing needs to be refined in order to improve results. However the word frequencies suggest that evidence can be found to suggest that there is spiritualism within the modern use of psychoactive drugs.

The project can be improved/ expanded upon by adding further drug experience webites, and looking at psychoactive drugs other than LSD and Mushrooms. 

There are also problems with the data, for example, misspelled words may be missed from the search. 
