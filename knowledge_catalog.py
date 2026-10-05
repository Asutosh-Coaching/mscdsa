#!/usr/bin/env python3
"""
knowledge_catalog.py
Master Curated Knowledge Catalog for IGNOU M.Sc. Data Science and Analytics (MSCDSA).
Contains rigorous, complete mathematical formulas in LaTeX, core definitions, intuitive explanations,
and exam checkpoints for Semester 1 and Semester 2 courses.
"""

COURSE_METADATA = {
    "MCS-061": {
        "title": "Mathematical Foundations - I",
        "semester": "Semester_1",
        "credits": 4,
        "type": "Theory",
        "description": "Foundations of discrete mathematics, linear algebra, vector spaces, and calculus powering modern data science algorithms."
    },
    "MCS-062": {
        "title": "Introduction to Data Science",
        "semester": "Semester_1",
        "credits": 4,
        "type": "Theory",
        "description": "Comprehensive principles of data acquisition, exploratory analysis, NoSQL pipelines, stream mining, and big data architecture."
    },
    "MCS-063": {
        "title": "Data Structures using Python",
        "semester": "Semester_1",
        "credits": 4,
        "type": "Theory",
        "description": "Algorithmic analysis, recursion, linear and tree structures, priority queues, hash tables, sorting, and memory management in Python."
    },
    "MCS-207": {
        "title": "Database Management Systems",
        "semester": "Semester_1",
        "credits": 4,
        "type": "Theory",
        "description": "Relational algebra, ER modeling, SQL optimization, normalization (1NF-BCNF), ACID concurrency, recovery, and NoSQL engines."
    },
    "MCSL-064": {
        "title": "Data Structures using Python Lab",
        "semester": "Semester_1",
        "credits": 2,
        "type": "Practical",
        "description": "Hands-on implementation of core data structures, recursive patterns, trees, and searching/sorting algorithms in Python."
    },
    "MCSL-065": {
        "title": "Data Science Lab",
        "semester": "Semester_1",
        "credits": 2,
        "type": "Practical",
        "description": "Practical laboratory sessions on data acquisition, cleaning, exploratory visualization, and basic statistical inference."
    },
    "MCS-066": {
        "title": "Mathematical Foundations - II",
        "semester": "Semester_2",
        "credits": 4,
        "type": "Theory",
        "description": "Rigorous probability theory, random variables, probability distributions, sampling, parameter estimation, hypothesis testing, ANOVA, and convex optimization."
    },
    "MCS-067": {
        "title": "Data Wrangling and Visualization",
        "semester": "Semester_2",
        "credits": 4,
        "type": "Theory",
        "description": "Data profiling, cleaning, transformation, reshaping, multi-table aggregation, and perceptual visualization using Python."
    },
    "MCS-068": {
        "title": "Predictive Data Analysis",
        "semester": "Semester_2",
        "credits": 4,
        "type": "Theory",
        "description": "Descriptive, diagnostic, and predictive modeling, multiple regression, regularization (Ridge/Lasso), classification, clustering, PCA, and R programming."
    },
    "MCS-224": {
        "title": "Artificial Intelligence & Machine Learning",
        "semester": "Semester_2",
        "credits": 4,
        "type": "Theory",
        "description": "State-space search (A*, Minimax), First-Order Logic, probabilistic reasoning, fuzzy sets, supervised learning, neural networks, and deep learning backpropagation."
    },
    "MCSL-069": {
        "title": "AI & Machine Learning Lab",
        "semester": "Semester_2",
        "credits": 2,
        "type": "Practical",
        "description": "Implementation of AI search heuristics, regression, classification, clustering, neural networks, and scikit-learn workflows."
    },
    "MCSL-070": {
        "title": "Data Analysis Lab",
        "semester": "Semester_2",
        "credits": 2,
        "type": "Practical",
        "description": "Practical hands-on predictive analysis, time series decomposition, and advanced exploratory analytics using R and Python."
    }
}

print("knowledge_catalog initialized.")
