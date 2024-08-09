import json

score_prompt = """You will be given an example of the source content and target text. The target text is generated from the source content according to the corresponding task type.

Your task is to rate the target text according to the evaluation criterion on a Likert scale from 1 to 5. Please make sure you read and understand these instructions carefully.

Task Type Description:
{task_des}

Evaluation Criterion:
{asp_des}


Example:

Source Content ({source_name}):
{source}

Target Text:
{target}


Evaluation Form:
Answer by starting with "Analysis:" to analyze the given example regarding the evaluation criterion as concisely as possible, and then give the numeric rating on the next line by "Rating:".

Your Answer:
"""

task_type = {
"news": """News Summary
The source content is a news article, and the target text is the summary of that news. The summary should include the important content of the news article and should not contain information not mentioned in the news.""",
"dial": """Dialogue Summary
The source content is a daily dialogue, and the target text is the summary of that dialogue. The summary should include the important content of the dialogue and should not contain information not mentioned in the dialogue.""",
"table": """Table Description
The source content is a table, and each row of the table has three elements separated by "|", representing the subject, predicate, and object of an event. The target text is a textual description equivalent to the table and should correctly include all the events from the table without containing information not mentioned in the table.""",
"para": """Paragraph Rewriting
The source content is a paragraph, and the target text is a synonym rewrite of that paragraph. The target text should include all the information from the paragraph and should not contain information beyond the paragraph."""
}

task_type_replace = {
"news": ["source news", "target text"],
"dial": ["source dialogue", "target text"],
"table": ["source table", "target text"],
"para": ["source paragraph", "target text"]}

source_key = {"news": "article", "dial": "dialogue", "table": "table", "para": "source"}

task_type_brief = {"news": "News", "dial": "Dialogue", "table": "Table", "para": "Paragraph"}

prompt_name = ['new_ref', 'fluency_repeat', 'fluency_passive', 'fluency_inversion', 'coherence_conjuction',
               "coherence_order", 'grammar_verb', "grammar_order", "grammar_typo", 'simple_word', 'simple_structure',
               'inform_abbr', 'inform_hypernym', "inform_delete", 'hallucination_fact', 'hallucination_continue',
               'contradiction_entity', 'contradiction_meaning', 'contradiction_negate']


description = json.load(open("aspect_criteria.json", encoding='utf-8'))
data = json.load(open("data_all.json", encoding='utf-8'))

for j in ["Fluency", "Coherence", "Grammaticality", "Simplicity", "Readability", "Faithfulness", "Non-contradiction", "Non-hallucination", "Informativeness", "Adequacy", "Overall_quality"]:
    for i in ["Detailed", "Gold", "List", "Term", "Simplified", "Selection1", "Selection2", "Selection3"]:
        if i not in description[j]:
            continue

        for cur_name in prompt_name:
            for id_, v in data.items():
                for d in v:

                    prompt = score_prompt.replace("{task_des}", task_type[id_]).replace("{asp_des}", description[j][i].replace("{S}", task_type_replace[id_][0]).replace('{T}', task_type_replace[id_][1]))
                    prompt = prompt.replace("{source_name}", task_type_brief[id_]).replace("{source}", d[source_key[id_]]).replace("{target}", d[cur_name])



