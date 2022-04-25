# Stylometer - writing style analyzer
This package analyzes the style of a given writing sample using "involved" and "informational" linguistic features. Paper related to this package: `arxiv.org...`

The main objective of "involved" features is to build a relationship with a reader, engage or involve a reader in a text; they include pronouns, non-phrasal coordination ("and"), and questions. The main objective of "informational" features is to convey facts and draw attention to the factual information in a text rather than build a relationship with a reader; they include determiners (such as "the", "which", "both", etc.), past tense verbs, and numbers. 

The package calculates the number of "involved" and "informational" features and prints out an "involved-informational ratio". The higher the "involved-informational ratio", the more "involved" a given writing sample. 

These linguistic features are based on the work of Biber (1988), Argamon et al. (2003), Pennebaker (2011).

References:
1. Biber, Douglas. (1988). Variation across Speech and Writing. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511621024
2. Argamon, Shlomo Engelson et al. (2003). “Gender, genre, and writing style in formal written texts.” Third Text 23 (2003): 321-346.
3. Pennebaker, J. W. (2011). The secret life of pronouns: What our words say about us. New York: Bloomsbury Press.
  
# Installation
Install from <a href="https://pypi.org/project/test-updated/">PyPi</a>:
`pip install stylometer`

# Usage examples
Please see a notebook with usage examples `Example.ipynb`

