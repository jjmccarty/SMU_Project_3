
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    #create a sentiment dictionary from polarity_scores.  This will product
    # pos, neg, neu and compound score.
    # TODO - not sure what compound score is - look that up
    
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    print("Sentiment Dictionary : ", sentiment_dict)
    print(f'Sentence to evaluate:{sentence}')
    print(f"---", sentiment_dict['neg']*100, "% neg")
    print(f"---", sentiment_dict['neu']*100, "% neu")
    print(f"---", sentiment_dict['pos']*100, "% pos")
 
    print("Sentence Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("pos")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("neg")
 
    else :
        print("neu")
 
 
if __name__ == "__main__" :
 
    print("\n1st statement :")
    sentence = "My dogs are the best dogs in the world."
 
    # function calling
    sentiment_scores(sentence)
 
    print("\n2nd Statement :")
    sentence = "Nothin unsual happened today."
    sentiment_scores(sentence)
 
    print("\n3rd Statement :")
    sentence = "This is the worst day ever."
    sentiment_scores(sentence)