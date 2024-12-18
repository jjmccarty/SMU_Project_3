
#######################################################################
# The sentiment analysis script utilizes VADER to perform basic 
# sentiment analysis on an input string.  It will determine if the 
# overall sentiment is positive (POS), neutral (NEU) or negative (NEG).
#######################################################################

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to print sentiments
# of the sentence.
def sentiment_scores(string_value):
    """
    Analyze the sentiment of a passed string and return a dictionary of 
    sentiment values.  
    args:
        string_value: string
        - The string to run through the sentiment analyzer
    returns:
        dictionary of sentiment values as:
        neg --> the score of negative sentiment
        neu --> the score of positive sentiment
        pos --> the score of neutral sentiment
        compound --> the overall sentiment score.  More negative values indicate
        a more negative sentiment while more positive values indicate more 
        positive sentiment.
    """
    print(f'Evaluating sentiment for {string_value}')

    sid_obj = SentimentIntensityAnalyzer()
 
    #create a sentiment dictionary from polarity_scores.  This will product
    # pos, neg, neu and compound score.    
    sentiment_dict = sid_obj.polarity_scores(string_value)
     
    print(f"--- {sentiment_dict['neg']*100} % neg")
    print(f"ooo {sentiment_dict['neu']*100} % neu")
    print(f"+++ {sentiment_dict['pos']*100} % pos")
    
    return sentiment_dict

def score(string_value, negative=-0.05, positive=0.05):
    """
    Analyze the sentiment of a passed string and return a dictionary of 
    sentiment values.  
    args:
        string_value: string
        - The string to run through the sentiment analyzer
        negative: float
        - Represents the number after which a more negative score is tagged as 
          negative
        positive: float
        - Represents the number after which a more positive score is tagged as 
          positive
    returns:
        string representation of if the value is POS, NEU, or NEG
    """
    sentiment_dictionary = sentiment_scores(string_value) 
    if sentiment_dictionary['compound'] >= positive:
        return 'POS'
    elif sentiment_dictionary['compound'] <= negative:
        return 'NEG'
    else:
        return 'NEU' 
 
if __name__ == "__main__" :
 
    print('-------- Test statement 1 --------')
    print(f'Rate: {score("My dogs are the best dogs in the world.")}')
 
    print('-------- Test statement 2 --------')
    print(f'Rate: {score("Nothin unsual happened today.")}')
 
    print('-------- Test statement 3 --------')
    print(f'Rate: {score("This is the worst day ever.")}')