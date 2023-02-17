# A program that uses the Spacy library to compute the similarity between different words and tokens.
# Overall, this code demonstrates how to use Spacy to compute the similarity between words and tokens, and how to loop through tokens 
# to compute their pairwise similarities.

print('MD Module: ')

# Import spacy 
import spacy 

# The spacy.load('en_core_web_md') loads the pre-trained medium-sized English language model from Spacy.
nlp = spacy.load('en_core_web_md')

# use the nlp function above and pass a string into it then save it in a variable
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("carrot")

# The similarity() function is called on these word objects to compute their similarities with each other and print to the console
print(f"{word1} similarity with {word2} is: {word1.similarity(word2)}")
print(f"{word3} similarity with {word2} is: {word3.similarity(word2)}")
print(f"{word3} similarity with {word1} is: {word3.similarity(word1)}")
print(f"{word4} similarity with {word4} is: {word4.similarity(word1)}")
print(f"{word4} similarity with {word4} is: {word4.similarity(word2)}")
print(f"{word4} similarity with {word4} is: {word4.similarity(word3)}")

tokens = nlp('cat apple monkey banana') 

# calling similarity() on each pair to compute their similarities. The results are printed to the console.
for token1 in tokens :              
    for token2 in tokens:                   
        print(f'The similarity between {token1.text} and {token2.text} is: {token1.similarity(token2)}')



#### Comments for spacy.load('en_core_web_md')
# The en_core_web_md model might be sufficient for some use cases because of higher similarity as compared with that of en_core_web_sm model which has low similarity.
# It is observed that the similarity in en_core_web_md model with tokenized words have higher similarity than en_core_web_sm

# Cat with Monkey has similarity of     0.5929930274321619
# Banana with Monkey has similarity of  0.40415016164997786
# Banana with Cat has similarity of     0.22358825939615987
# Carrot with Cat has similarity of     0.3252276336665523
# Carrot with Monkey has similarity of  0.3993978676521539
# Carrot with Banana has similarity of  0.6909409498647585
# ### Its Tokenized part are
# Cat Cat              1.0
# Cat Carrot           0.32522761821746826  0.3252276336665523  very similar
# Cat Monkey           0.5929930210113525   0.5929930274321619  very similar
# Cat Banana           0.2235882580280304   0.22358825939615987  very similar

# Carrot Cat           0.32522761821746826  0.3252276336665523  very similar
# Carrot Carrot        1.0
# Carrot Monkey        0.3993978500366211   0.3993978676521539  very similar
# Carrot Banana        0.6909409761428833   0.6909409498647585  very similar

# Monkey Cat           0.5929930210113525   0.5929930274321619  very similar
# Monkey Carrot        0.3993978500366211   0.3993978676521539  very similar
# Monkey Monkey        1.0
# Monkey Banana        0.4041501581668854   0.40415016164997786  very similar

# Banana Cat           0.2235882580280304   0.22358825939615987  very similar
# Banana Carrot        0.6909409761428833   0.6909409498647585   very similar
# Banana Monkey        0.4041501581668854   0.40415016164997786  very similar
# Banana Banana        1.0







print('SM Module: ')

# The spacy.load('en_core_web_md') loads the pre-trained small-sized English language model from Spacy.
nlp = spacy.load('en_core_web_sm')

# use the nlp function above and pass a string into it then save it in a variable
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("carrot")


print(f"{word1} similarity with {word2} is: {word1.similarity(word2)}")
print(f"{word3} similarity with {word2} is: {word3.similarity(word2)}")
print(f"{word3} similarity with {word1} is: {word3.similarity(word1)}")
print(f"{word4} similarity with {word4} is: {word4.similarity(word1)}")
print(f"{word4} similarity with {word4} is: {word4.similarity(word2)}")
print(f"{word4} similarity with {word4} is: {word4.similarity(word3)}")

tokens = nlp('cat carrot monkey banana') 

# calling similarity() on each pair to compute their similarities. The results are printed to the console.
for token1 in tokens :              
    for token2 in tokens:                   
        print(f'The similarity between {token1.text} and {token2.text} is: {token1.similarity(token2)}')


### Comments for spacy.load('en_core_web_sm')
# Cat with Monkey has similarity of    0.6770565478895127 
# Banana with Monkey has similarity of 0.7276309976205778
# Banana with Cat has similarity of    0.6806929391210822
# Carrot with Cat has similarity of    0.7283041452688714
# Carrot with Monkey has similarity of 0.7042034740658057
# Carrot with Banana has similarity of 0.6254266136312152

# ### Its Tokenized part are
# Cat Cat              1.0
# Cat Carrot           0.7093684673309326   0.7283041452688714  similar
# Cat Monkey           0.6735064387321472   0.6770565478895127  similar
# Cat Banana           0.24448759853839874  0.6806929391210822  not similar

# Carrot Cat           0.7093684673309326   0.7283041452688714  similar
# Carrot Carrot        1.0
# Carrot Monkey        0.7869552969932556   0.7042034740658057  similar
# Carrot Banana        0.3652842044830322   0.6254266136312152 not similar

# Monkey Cat           0.6735064387321472   0.6770565478895127  similar
# Monkey Carrot        0.7869552969932556   0.7042034740658057  similar
# Monkey Monkey        1.0
# Monkey Banana        0.38246291875839233  0.7276309976205778  not similar

# Banana Cat           0.24448759853839874  0.6806929391210822  not similar
# Banana Carrot        0.3652842044830322    0.6254266136312152 not similar
# Banana Monkey        0.38246291875839233   0.7276309976205778  not similar
# Banana Banana        1.0



#### Comments spacy.load('en_core_web_sm')
# The en_core_web_sm model might be slightly not sufficient for some use cases because of disparity in their values of similarity as compared with that of en_core_web_md model.
# It is observed that the similarity in en_core_web_sm model with tokenized words might not give accurate description in most cases.


# The module (en_core_web_sm) uses the small-sized English language model from Spacy, instead of the medium-sized (en_core_web_md) model. 
# The main difference between the small (en_core_web_sm) and medium-sized (en_core_web_md) models is that
# the medium-sized one includes more word vectors and has better accuracy than the small one. Therefore, the similarity scores computed 
# with the en_core_web_md model might be more accurate than those computed with the en_core_web_sm.
# In practice, the choice of model depends on the specific task and the available resources.