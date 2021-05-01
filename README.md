# Interpreter for Typed arithmetic expressions.

This project aims to create an interpreter for Typed arithmetic expressions using python language. The line input by the user is tokenized and converted into a nested list where each component list represents a step of derivation tree (left to right in list : root to leaf in tree). If the term in typable, predefined rules of the language is applied in the reverse order (right to left in list : leaf to root in tree) recursively until a value is produced.

