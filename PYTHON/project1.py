from gensim.summarization.summarizer import summarize



paragraph = input ("Input a paragraph: ")


summ_words = summarize(paragraph) 
print("\n")
print("Summarized Paragraph: ") 
print(summ_words)