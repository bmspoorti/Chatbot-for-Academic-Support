import pandas as pd

ADSA_data = {
    "Question": [
        "What are the core subjects in the Applied Data Science and Analytics course at SRH Hochschule Heidelberg?",
        "Is there a required textbook for the Machine Learning module in Applied Data Science at SRH?",
        "What is the deadline for submitting assignments in the Data Visualization module at SRH Hochschule Heidelberg?",
        "What is the last date to withdraw from the Applied Data Science course at SRH without a penalty?",
        "How do I apply for an extension on a project in the Applied Data Science course at SRH?",
        "What is the exam retake policy for the Applied Data Science and Analytics course at SRH Hochschule Heidelberg?",
        "Can you explain the concepts of machine learning used in the Applied Data Science and Analytics course at SRH Hochschule Heidelberg?",
        "I need tips on how to handle big data projects for the Applied Data Science course at SRH.",
        "What advanced analytics techniques are taught in the second year of the Applied Data Science and Analytics course at SRH?",
        "What software tools do I need to master for the Applied Data Science course at SRH?",
        "Are there internship opportunities linked with the Applied Data Science and Analytics course at SRH?",
        "What are the thesis requirements for graduating from the Applied Data Science and Analytics program?",
        "How can I connect with alumni from the Applied Data Science and Analytics course at SRH?",
        "Are there any upcoming guest lectures or workshops related to big data in the Applied Data Science course?",
        "Are there study abroad options available for students in the Applied Data Science and Analytics course?",
        "How are the final exams structured in the Applied Data Science and Analytics course at SRH?",
    ] * 15,
    "Answer": [
        "Core subjects include Machine Learning, Statistical Analysis, Data Management, and Big Data Technologies.",
        "Yes, the recommended textbook is 'Machine Learning Yearning' by Andrew Ng.",
        "Assignments in the Data Visualization module are due by the end of the 8th week of the semester.",
        "You can withdraw without penalty within the first six weeks of the semester.",
        "Project extensions can be requested via the academic office, subject to approval by the course coordinator.",
        "Students may retake exams if they score below a C grade, with a maximum of two retakes allowed.",
        "The course covers a variety of machine learning topics, including supervised and unsupervised learning, neural networks, and reinforcement learning.",
        "For big data projects, focus on efficient data storage, using frameworks like Hadoop, and practice scalable machine learning techniques.",
        "The second year includes advanced topics like Deep Learning, Natural Language Processing, and Time Series Analysis.",
        "Key tools include R, Python, SQL, TensorFlow, and Tableau.",
        "Yes, the program partners with local tech companies to offer internships in data analytics and machine learning.",
        "The thesis should demonstrate practical application of data analytics techniques, and is typically 15,000-20,000 words long.",
        "Alumni networking is facilitated through the university's annual meet and LinkedIn groups specifically for data science graduates.",
        "Yes, the course frequently invites industry experts to conduct workshops on the latest trends in big data and machine learning.",
        "Students have the option to participate in exchange programs with partner universities in the US and Europe.",
        "Exams typically include a combination of practical project work and written exams focusing on theory and application.",
    ] * 15
}

# Expanding the dataset length
ADSA_data["Question"] = ADSA_data["Question"][:100]
ADSA_data["Answer"] = ADSA_data["Answer"][:100]

# Creating a DataFrame
ADSA_QA_df = pd.DataFrame(ADSA_data)

ADSA_file_path = 'Expanded_Academic_Support_Chatbot_Data_SRH.csv' 
ADSA_QA_df.to_csv(ADSA_file_path, index=False)

ADSA_file_path





   