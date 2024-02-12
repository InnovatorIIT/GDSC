# Sentiment Analysis
  Sentiment analysis is a natural language processing (NLP) technique used to determine the sentiment or emotional tone expressed in a piece of text. It involves     analyzing the text to identify whether it conveys positive, negative, or neutral sentiment.Sentiment analysis has numerous applications across various domains, including social media monitoring, customer feedback analysis, brand reputation management, market research, and more. It helps organizations understand public opinion, customer sentiment, and trends, allowing them to make data-driven decisions and take appropriate actions based on the insights gained from analyzing text data.

# About Problem Statement
We have been provided with a dataset on which we have to design a Machine Learning Algorithm which can perform sentiment analysis Accurately. The data provided was skewed in many sense, due to which intial accuracy of Machine Learning model is supposed to be of high bias and low variance. Hence the model works good enough only in training data, and tends to underfit on new data. The data provided was of about 27000 with three classes of Positive, Negative and Neutral.

* There were 11k instances for neutral class
* There were 8.5k instances for positive class
* There were 7.7k instances for negative class

# Approach
I have used two python programs to solve this PS. One for preprocessing the given data and one model which runs of preprocessed data.

## Preprocessing
The data had many demerits to consider for before making it fit to train. Some of them where:
* Mispelt Words
* Contracted Word
* Modern lingo
* Mismatched text cases

To address this issues we first converted all the text to lower case for uniformity, after which a spell checker was called. I have tried using two methods for spell checker:
* Using Language ToolBox
* Using TextBlob

The Language ToolBox library gave better results and also significantly improved the grammatical accuracy of the dataset. But it was computational intensive and took more than 2s/text time duration. So trading off accuracy with time, I decided to go for TextBlob library which was doing pretty well in spell recitification. Though it wasnt giving the desired output, it improved the given dataset significantly. I have even explored two other ways for spell checking. One was probabilistic approach in which a mispelt word would be checked for in a "grammatically accurate and vocabulary rich" text file, comparing which the program would give us the most closest correct word. Another was using a GingerIt module for grammtical and vocabulary accuracy.

Contracted Words and Modern Lingo were rectified by pre-defining a set of Stopwords which would be expanded to modern english format whenever a token in the set of stopwords is encountered. Also Stemming is used along with removal of stopwards and punctuations from the text. Upon Preprocessing what we could get was a refined dataset of keywords which would be meaningful for the sentiment analusis model.

## Using Google-BERT Model for Analysis.

  

