Sentiment Analysis 
==================

Sentiment Analysis of Electronic Products

## Input
 
Users' online reviews from two technological websites: www.techcrunch.com and www.cnet.com for iPhone 5 which was 
release in Sep. 2012.

## Output

People opinions sentiments for new iPhone 5

## Dependencies

For running this code you need to have Python 2.7 and install PycURL & BeautifulSoup packages on your machine. Check link below for more details:
	
	www.crummy.com/software/BeautifulSoup/
	pycurl.sourceforge.net/


## Technical Description

The goal of this project was to mine/analyze people opinions about the new iPhone 5 which has been released on Spetember 12, 2012 [1] by mining relevent websites.

## The code consists of two steps

A- Crawling online comments from web, cleaning up data and extracting important information from html content:

We developed a Python web crawler to pull out people's comments from techcrunch.com and cnet.com websites where they discussed th new released iPhone. This crawler downloads all reviews posted by people. Next, Beautiful Soup Python library was used to extract important data from HTML contents [2].

B- Running sentiment analysis using PycURL and text-processing API:

For the second step, we used a machine learning algortihm for sentiment analysis to find out what people think about the iPhone 5. We found an available API for the sentiment analysis implemented by Python NLTK [3]. Thus, we used this website API in order to analyze the polarities of posted comments. For sending HTTP requests to text-processing website, we used a Python library called PycURL. PycURL is a Python interface to libcurl [4].

## Results

For techcrunch.com, we collected 79 comments in total where 10 of them were labeled neutral, 13 positive, and 56 of them were labelled 
negative respect to the topic (iPhone 5). Below is the details:

	pos=16.4%
	neutral=12.6%
	neg=71%

For cnet.com, we collected 37 comments in total where 5 of them were labeled neutral, 7 positive, and 25 of them were labelled negative. 
Below is the details:

	pos=19%
	neutral=13.5
	neg=67%

Even if our dataset is limited, our results are relatively consistent across both websites. The average results considering the data from 
both websites are:

	pos=17.7%
	neutral=13.05%
	neg=69%

## Observations

Above results show how people thought about the new iPhone release after its demo on September 12, 2012 and it does not reflect 
the developer's opinion.
 
If you have any question regard to this project, please drop me a note @ "k DOT jahanbakhsh AT gmail DOT com".

## Refs

[1] www.cnet.com/iphone-5/
[2] www.crummy.com/software/BeautifulSoup/
[3] text-processing.com/demo/sentiment/
[4] pycurl.sourceforge.net/
