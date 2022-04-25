#!/usr/bin/env python
# coding: utf-8


import spacy

try:
	nlp = spacy.load("en_core_web_lg")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")
    print('spaCy language model is now downloaded')


class Text():

    '''This class helps to understand how involved or engaging a given text is, i.e. how many interactional 
    linguistic features are used that engage, "involve" the reader, in the text. "Informational" features' main objective
    is to convey facts, while "involved" features' main objective is to build a relationship with a reader,
    engage/involve the reader in the text.

    References: 
    1. Biber, Douglas. (1988). Variation across Speech and Writing. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511621024
    2. Argamon, Shlomo Engelson et al. (2003). “Gender, genre, and writing style in formal written texts.” Third Text 23 (2003): 321-346.
    3. Pennebaker, J. W. (2011). The secret life of pronouns: What our words say about us. New York: Bloomsbury Press.'''

    def __init__(self,input_file):
        # Read in an input text file
        text_file = open(input_file).read()
        # Change to string
        
        # Tokenize and analyze text with spaCy 
        doc = nlp(text_file)
        
        # Get pronouns
        pronouns_list = ['PRP','PRP$', 'WP', 'WP$']
        get_pronouns = []
        for token in doc:
            for feature in pronouns_list:
                if feature == token.tag_:
                    get_pronouns.append(token.text)
        self.pronouns = get_pronouns
        self.n_pronouns = len(get_pronouns)
        
        # Get questions
        get_questions = []
        for token in doc:
            if '?' == token.text.lower():
                get_questions.append('?')  
        self.questions = get_questions
        self.n_questions = len(get_questions)

        # Get "and" coordination
        get_and_coordination = []
        for token in doc:
            if 'and' == token.text.lower():
                get_and_coordination.append('and')  
        self.and_coordination = get_and_coordination
        self.n_and_coordination = len(get_and_coordination)

        # Get determiners
        determiners_list = ['PDT', 'WDT', 'DT']
        get_determiners = []
        for token in doc:
            for feature in determiners_list:
                if feature == token.tag_:
                    get_determiners.append(token.text)
        self.determiners = get_determiners
        self.n_determiners = len(get_determiners)

        # Get past tense
        past_tense_list = ['VBD', 'VBN']
        get_past_tense = []
        for token in doc:
            for feature in past_tense_list:
                if feature == token.tag_:
                    get_past_tense.append(token.text)
        self.past_tense = get_past_tense
        self.n_past_tense = len(get_past_tense)

        # Get cardinal numbers
        get_cardinal_numbers = []
        for token in doc:
            if token.tag_ == 'CD':
                get_cardinal_numbers.append(token.text)
        self.cardinal_numbers = get_cardinal_numbers
        self.n_cardinal_numbers = len(get_cardinal_numbers)

        # Get total involved features
        self.involved_features = get_pronouns + get_questions + get_and_coordination
        self.n_involved_features = len(get_pronouns) + len(get_questions) + len(get_and_coordination)
        
        # Get total informational features
        self.info_features = get_determiners + get_past_tense + get_cardinal_numbers
        self.n_info_features = len(get_determiners) + len(get_past_tense) + len(get_cardinal_numbers)

        # Calculate involved-informational ratio
        self.ratio = round(self.n_involved_features/self.n_info_features, 2)
    
    def summary(self):
        print("Total number of involved features:", self.n_involved_features)
        print("Number of pronouns:", self.n_pronouns)
        print("Number of questions:", self.n_questions)
        print("Number of 'and' coordination:", self.n_and_coordination)
        print("-----------------------------------------------")
        print("Total number of informational features:", self.n_info_features)
        print("Number of determiners:", self.n_determiners)
        print("Number of past tense verbs:", self.n_past_tense)
        print("Number of cardinal numbers:", self.n_cardinal_numbers)
        print("-----------------------------------------------")
        print("Involved-informational ratio:", round(self.n_involved_features/self.n_info_features, 2))

