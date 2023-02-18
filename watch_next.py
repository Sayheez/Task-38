# A python program that uses the Spacy library ('en_core_web_md') to predict next movie for users/viewers to watch based on the vector similarity of the description of the movie.
# Overall, this code demonstrates how to use Spacy to predicts the next movie to watch using for loop, if statements, lists, variables, reading from a file.

# import spacy module, sys and os
import spacy, sys, os

nlp = spacy.load('en_core_web_md')

# define a variable with movie description
description = """Will he save their world or destroy it? When the hulk becomes
                 too dangerous for the Earth, the illuminati trick hulk into a shuttle and launch him
                 into space to a planet where he can live in peace. Unfortunately, Hulk lands on the
                 planet Sakaar where he is sold into slavery and trained as a gladiator."""


current_working_directory = os.getcwd()    # Return a string representing the current working directory.
print('Current working directory: {}'.format(current_working_directory))
# Make sure it's an absolute path.
abs_working_directory = os.path.abspath(current_working_directory)
print('Current working directory (full path): {}'.format(abs_working_directory))
print()

filename = 'movies.txt'
# Check whether file exists.
if not os.path.isfile(filename):
    # Stop with leaving a note to the user.
    print('It seems file "{}" does not exists in directory: "{}"'.format(filename, current_work_directory))
    sys.exit(1)
else:
    print('file exists here')


# Create a function to find next word
def watch_next(description):
    # To read from the file named movies.txt of descriptions
    file = open(filename, 'r')

    contents = ""
    for line in file:
        contents += line           # all file contents loaded as strings
    print('contents', contents)

    # Split it into a list of each line
    lines = contents.split("\n")
    print('lines', lines)

    # call the nlp method with the parameter 'description' and store in a variable 
    nlp_description = nlp(description)

    # create an empty list that will holds string text from the file when the lines list is loop over
    nlp_list = []
    for index in range(len(lines)):
        nlp_list.append(nlp(lines[index]))


    # create an empty list that will holds similarity texts in the description
    similarity_list = []

    # Loop through the nlp_list and use similarity method on each indices in the nlp_list
    # then append each indices to the empty similarity_list
    for index in range(len(nlp_list)):
        val = nlp_list[index].similarity(nlp_description)
        similarity_list.append(val)

    # finding the most similar movie
    most_similar_index = similarity_list.index(max(similarity_list))    # best match values

    # Use the most_similar_index as an index on the list named lines to obtain the matched movie
    matched_movie = lines[most_similar_index]

    print(f"The movie that best matched the given movie is --> {matched_movie}")

    # close the file
    file.close()
    

def main():
    watch_next(description)

main()

