# Instructions and examples for the aspect-specific perturbations

prompt_fluency_repeat = """For each sentence of the original text, add only one expression or phrase that has the same and repeated meaning as the partial content of the sentence.
Note that each sentence of the new text should maintain exactly the same meaning as the original text.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist and naturally inclined to see the good, I view 2021 as a period of recuperation and recovery. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope or a silver lining for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities and a reduction in related deaths, and the economic initiatives implemented by governments have contributed to the stimulation and promotion of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed and emerged victorious in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return and coming back to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating and surpassing Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete or take part in the World Championships in Kazan, Russia, but intends and plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet and doesn't know which brand he should choose and make the selection of. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper at a lower price. Josh will call and ring up Brian after work to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology is in the city of Bangalore whose founder and builder is Kempe Gowda I. The institute was given and granted the 'Technical Campus' status by the All India Council for Technical Education, which is located and situated in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body and under the auspice of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing and seeing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half, namely more than 50%, of the world's population and economic output. However, by 1900, its share of global output and production had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs and the primary centers of industry in the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is sick and under the weather. James is going to the Jesus bar, a pub. Oli couldn't find anyone near or around the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is located and situated in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance contains and includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader, someone with leadership, in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan, during a training session, demonstrated and showcased an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing and getting ready for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight and competition with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao, being defeated.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited or called on his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled, behind the initial timetable. Hannah will inform Dad and let him know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout and exceptional player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target and a goal for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of and takes pride in his progress, despite the sadness of seeing him go. Depay's connection and association with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence and make a difference to his transfer decision.

Original text:
{{example}}
New text:
"""

prompt_fluency_passive = """Change the original text to use the passive voice grammatically correctly.
Note that each sentence of the new text should maintain exactly the same meaning as the original text.
Note that intransitive verbs in the original text cannot be changed to passive voice.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, 2021 is viewed by me as a period of recuperation. While the COVID-19 pandemic hasn't concluded, a glimmer of hope is seen for an improved future in the realm of healthcare and the broader economy. A decrease in COVID-19 fatalities has been led to by the availability of reliable and potent vaccines, and the stimulation of economic expansion has been contributed to by the economic initiatives implemented by governments.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, with his return being marked to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, with Ryan Lochte being beaten, and his joy at being back in the water was expressed by him. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but it is planned by him to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet and doesn't know which brand should be chosen by him. According to Brian, other brands are considered better than Apple, and a Samsung tablet can be got cheaper by him. A call will be made to Brian by Josh after work to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology is located in the city of Bangalore which is founded by Kempe Gowda I. The 'Technical Campus' status was given to the institute by the All India Council for Technical Education, which is located in Mumbai. An affiliation is held by the Acharya Institute of Technology with Visvesvaraya Technological University, and tennis sports with the governing body of the International Tennis Federation are offered by it.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
Asia's return to its traditional share of the global population and economy is being observed by the 21st century. Back in 1800, over half of the world's population and economic output were accounted for by Asia. However, by 1900, its share of global output had decreased to just 20%. This change was not caused by any negative developments in Asia, but rather because Europe and North America had been revolutionized by the Industrial Revolution and turned into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is sick. The Jesus bar is being gone to by James. Anyone near the bar couldn't be found by Oli.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. The Gujarat Legislative Assembly is included by Gujarat’s governance, and T. S. Thakur is considered a leader in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
An impressive skill was demonstrated by British boxer Amir Khan during a training session, with an empty plastic bottle being kept in the air with rapid punches and finished with a left hook. The 28-year-old's fight against Chris Algieri on May 29 at the Barclays Center in New York is being prepared for by him. A fight with Manny Pacquiao later in the year is also being eyed by Khan, with his desire to compete in Dubai or Abu Dhabi being expressed. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.

New text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
Original text:
Adam's parents haven't been visited by him in six months, and he is coming over tomorrow. His flight will land an hour later than originally scheduled. Dad will be let know by Hannah.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
PSV Eindhoven is likely to be left by Memphis Depay, a standout player for the club, this summer according to PSV director Marcel Brands. The Dutch international, who has had 19 goals scored by him in the current season, is a target for Manchester United and other top European teams. The strong interest in Depay is acknowledged by Brands, and pride in his progress is felt by Brands, despite the sadness of seeing him go. Depay's transfer decision could be influenced by his connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team.

Original text:
{{example}}
New text:
"""

prompt_fluency_inversion = """Change the original text to use the structure of inversion and fronting grammatically correctly.
Note that each sentence of the new text should maintain exactly the same meaning as the original text.
Note that the predicate component cannot be fronted or placed at the beginning of a sentence.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, a period of recuperation I view 2021 as. While the COVID-19 pandemic hasn't concluded, there is, in the realm of healthcare and the broader economy, a glimmer of hope for an improved future. A decrease in COVID-19 fatalities, the availability of reliable and potent vaccines has led to, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
In the 100 meters butterfly at the Arena Pro Swim Series in Arizona, Michael Phelps triumphed, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. With a time of 52.38 seconds, beating Ryan Lochte, he won and expressed his joy at being back in the water. The World Championships in Kazan, Russia, the most decorated Olympian, Phelps, will not compete in, but plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet, and which brand he should choose, he doesn't know. Better than Apple are other brands, according to Brian, and he can get a Samsung tablet cheaper. Brian Josh will call after work to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
In the city of Bangalore whose founder is Kempe Gowda I, is the Acharya Institute of Technology. Given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai, was the institute. With Visvesvaraya Technological University, the Acharya Institute of Technology has an affiliation, and it offers tennis sports with the governing body of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
Observing Asia's return to its traditional share of the global population and economy is the 21st century. Over half of the world's population and economic output, Asia accounted for, back in 1800. Its share of global output, however, had decreased to just 20% by 1900. Not due to any negative developments in Asia was this change, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Sick is Annette. Going to the Jesus bar is James. Near the bar, Oli couldn't find anyone.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Located in Ahmedabad, a city within the Indian state of Gujarat, is Amdavad ni Gufa. The Gujarat Legislative Assembly, Gujarat’s governance includes, and in India, T. S. Thakur is a leader.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
An impressive skill, British boxer Amir Khan, during a training session, demonstrated by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. Preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York is the 28-year-old. Also eyeing a fight with Manny Pacquiao later in the year, Khan expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Coming over tomorrow is Adam, and he hasn't visited his parents in six months. An hour later than originally scheduled, his flight will land. Hannah will let Dad know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Likely to leave the club this summer is Memphis Depay, a standout player for PSV Eindhoven, according to PSV director Marcel Brands. For Manchester United and other top European teams, the Dutch international, who has scored 19 goals in the current season, is a target. The strong interest in Depay, Brands acknowledges, and feels proud of his progress, despite the sadness of seeing him go. From their time with the Dutch national team, Depay's connection with Manchester United's manager Louis van Gaal, could influence his transfer decision.

Original text:
{{example}}
New text:
"""

#coherence_sentence_order rule

prompt_coherence_conjuction = """Add inappropriate conjunctions to the original text to make the transitions and relationships between adjacent sentences illogical or not understandable.
Note that each sentence of the new text itself must not contain contradictions.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, I view 2021 as a period of recuperation. Instead, while the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. Thus, the availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. In contrast, he won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. In other words, Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet and doesn't know which brand he should choose. Therefore, according to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. However, Josh will call Brian after work to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. As a result, the institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. Despite this, the Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Furthermore, back in 1800, Asia accounted for over half of the world's population and economic output. For instance, by 1900, its share of global output had decreased to just 20%. Likewise, this change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is sick. For example, James is going to the Jesus bar. Indeed, Oli couldn't find anyone near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Hence, Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. Nevertheless, the 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Therefore, Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. In general, Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited his parents in six months and is coming over tomorrow. Similarly, his flight will land an hour later than originally scheduled. Surprisingly, Hannah will let Dad know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. Conversely, the Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Consequently, Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. As a result, Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.

Original text:
{{example}}
New text:
"""

#grammar_typos rule

#grammar_word_order rule

prompt_grammar_verb = """Introduce several errors and incorrect usages of the verb form into the original text.
Note that you must not change other parts of the original text.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, I views 2021 as a period of recuperation. While the COVID-19 pandemic hasn't conclude, there are a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has lead to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributing to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumph in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He winning with a time of 52.38 seconds, beating Ryan Lochte, and express his joy at being back in the water. Phelps, the most decorated Olympian, will not competes in the World Championships in Kazan, Russia, but plans to participating in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh want to buying a tablet and doesn't knows which brand he should choose. According to Brian, other brands is better than Apple and he can gets a Samsung tablet cheaper. Josh will called Brian after work to talks about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology are in the city of Bangalore whose founder being Kempe Gowda I. The institute was gave the 'Technical Campus' status by the All India Council for Technical Education, which are located in Mumbai. The Acharya Institute of Technology have an affiliation with Visvesvaraya Technological University, and it offer tennis sports with the governing body of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observe Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounting for over half of the world's population and economic output. However, by 1900, its share of global output had decrease to just 20%. This change were not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionizes Europe and North America, turning them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette are sick. James is go to the Jesus bar. Oli couldn't found anyone near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is locate in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance include the Gujarat Legislative Assembly, and T. S. Thakur are a leader in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan, during a training session, demonstrate an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with left hooks. The 28-year-old is prepare for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eye a fight with Manny Pacquiao later in the year, expressed his desire to competed in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fights and lost to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visit his parents in six months and are coming over tomorrow. His flight will lands an hour later than originally schedule. Hannah will letting Dad know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leaves the club this summer according to PSV director Marcel Brands. The Dutch international, who has scores 19 goals in the current season, are a target for Manchester United and other top European teams. Brands acknowledging the strong interest in Depay and feel proud of his progress, despite the sadness of seeing him goes. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influences his transfer decision.

Original text:
{{example}}
New text:
"""


prompt_simple_word = """For each sentence of the original text, rephrase only one word or phrase into a new one with exactly the same meaning.
Note that the new one should be unfamiliar or not conform to typical and common English usage.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent Pollyanna, I view 2021 as a period of convalescence. While the COVID-19 pandemic hasn't arrived at its termination, there is a scintilla of hope for an improved future within the sphere of healthcare and the broader economy. The presence of trustworthy and potent vaccines has catalyzed a diminution in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the invigoration of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps prevailed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his reentry to competitive swimming after a six-month interdiction owing to a drink-driving conviction. He won with a time of 52.38 seconds, outstripping Ryan Lochte, and articulated his elation at being back in the water. Phelps, the most decorated Olympian, will not vie in the World Championships in Kazan, Russia, but envisions participating in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to procure a tablet and remains uncertain about which brand he ought to choose. As per Brian, other brands outbalance Apple and he can get a Samsung tablet at a more economical rate. Josh will telephone Brian after work to interflow about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology resides in the city of Bangalore whose founder is Kempe Gowda I. The institute was bestowed the 'Technical Campus' status by the All India Council for Technical Education, which is situated in Mumbai. The Acharya Institute of Technology maintains an affiliation with Visvesvaraya Technological University, and it proffers tennis sports under the aegis of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's renaissance to its conventional proportion of the global population and economy. Back in 1800, Asia constituted over half of the world's population and economic throughput. However, by 1900, its quota of global output had abated to just 20%. This alteration was not due to any adverse evolutions in Asia, but rather because the Industrial Revolution had metamorphosed Europe and North America, transmuting them into the main industrial nexuses of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is indisposed. James is proceeding to the Jesus tavern. Oli couldn't find anyone in the vicinity of the tavern.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is situated in Ahmedabad, a metropolis within the Indian state of Gujarat. Gujarat’s governance encompasses the Gujarat Legislative Assembly, and T. S. Thakur is a fugleman in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British pugilist Amir Khan, amid a training session, manifested an impressive skill by sustaining an empty plastic bottle in the air with rapid punches and culminating with a left hook. The 28-year-old is preparing for his bout against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, vocalized his aspiration to compete in Dubai or Abu Dhabi. Algieri, Khan's adversary, recently combated and lost to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited his father and mother in six months and is coming over tomorrow. His flight will alight an hour later than originally slated. Hannah will apprise Dad.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout player for PSV Eindhoven, is probable to depart the club this summer according to PSV director Marcel Brands. The Dutch international, who has tallied 19 goals in the current season, is a quarry for Manchester United and other top European teams. Brands acknowledges the potent interest in Depay and feels proud of his progress, despite the melancholy of seeing him leave. Depay's linkage with Manchester United's manager Louis van Gaal, from their tenure with the Dutch national team, could sway his transfer decision.

Original text:
{{example}}
New text:
"""


prompt_simple_structure = """For each sentence of the original text, rephrase it using more clauses, without introducing any information not in the original text or changing the original word usage.
Note that each sentence of the new text should maintain exactly the same meaning as the original text.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
I, who am an optimist that is inherent, view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope, which is for an improved future that lies within the realm of healthcare and the broader economy. The availability of vaccines, which are reliable and potent, has led to a decrease that is in COVID-19 fatalities, and the economic initiatives that have been implemented by governments have contributed to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps, who triumphed in the 100 meters butterfly at the Arena Pro Swim Series, which was in Arizona, marked his return to competitive swimming after a six-month suspension that was due to a drink-driving conviction. He, who won with a time that was 52.38 seconds, beating Ryan Lochte, expressed his joy at being back in the water. Phelps, who is an Olympian that is the most decorated, will not compete in the World Championships, which are in Kazan, Russia, but he plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh, who wants to buy a tablet, doesn't know which brand he should choose. According to Brian, who thinks that other brands are better than Apple, he can get a tablet whose brand is Samsung, which is cheaper. Josh will call someone who is Brian after work to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology is in Bangalore, which is a city whose founder is Kempe Gowda I. The institute was given the status that was called 'Technical Campus' by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation that is with Visvesvaraya Technological University, and it offers tennis sports, which are with the governing body of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is when Asia's return to its traditional share of not only the global population but also the economy is being observed. Back in 1800, it was Asia that accounted for over half of the world's population and economic output. However, by 1900, its share of output that was global had decreased to just 20%. This change was not due to any developments that were negative in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, which turned them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
It is Annette who is sick. James is going to a bar that is called Jesus bar. Oli couldn't find anyone who was near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is located in Ahmedabad, which is a city within Gujarat, which is an Indian state. Gujarat’s governance includes an assembly that is called the Gujarat Legislative Assembly, and it is T. S. Thakur who is a leader in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan, when he was during a training session, demonstrated an impressive skill by keeping a plastic bottle that was empty in the air with punches that were rapid and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri, which is on May 29 at the Barclays Center in New York. Khan, who also eyed a fight with Manny Pacquiao, which was later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, who was Khan's opponent, recently fought and lost to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam, who hasn't visited his parents in six months, is coming over when it is tomorrow. His flight will land an hour later than it was originally scheduled. It is Hannah who will let Dad know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, who is a player that is standout for PSV Eindhoven, is likely to leave the club this summer according to someone who is PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other European teams that are top. Brands, who acknowledges the strong interest in Depay, feels proud of his progress, despite the sadness that comes with seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, which was from their time with the Dutch national team, could influence his transfer decision.

Original text:
{{example}}
New text:
"""

#informativeness_delete rule


prompt_inform_abbr = """Abbreviate the original text and delete several parts of the content to make the rest lose some information of the original text.
Note that the new text should be unconfused and logically connected.
Note that you must not introduce any grammatical errors or meanings that are not supported by the original text.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is hope for an improved future. Reliable vaccines have led to a decrease in COVID-19 fatalities, and government initiatives have supported economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming. He won with a time of 52.38 seconds and expressed his joy at being back in the water. Phelps will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet and doesn't decide the brand. Brian suggests non-Apple brands. Josh will discuss it with Brian after work.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology, located in Bangalore, was granted 'Technical Campus' status by the All India Council for Technical Education. It's affiliated with Visvesvaraya Technological University and offers tennis sports.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's return to its traditional share. Back in 1800, Asia accounted for over half of the world's economic output. However, by 1900, its share of global output had decreased to just 20%. This change was because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
James is going to a bar. Oli couldn't find anyone near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is in Ahmedabad, Gujarat. Gujarat's governance includes the Gujarat Legislative Assembly.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan demonstrated skill by keeping an empty bottle in the air with punches. The 28-year-old is preparing for his fight against Chris Algieri on May 29. Khan, also eyeing a fight with Manny Pacquiao, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently lost to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited his parents and is coming over. His flight will land later than originally scheduled. Hannah will let Dad know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay is likely to leave PSV Eindhoven this summer according to PSV director Marcel Brands. The Dutch international is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal could influence his transfer decision.

Original text:
{{example}}
New text:
"""


prompt_inform_hypernym = """Replace some words with their hypernyms in the original text if possible and reasonable.
Note that the new text should not have contradictions with the original text.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, I view 2021 as a time of recuperation. While the health crisis hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent medical treatments has led to a decrease in health crisis fatalities, and the economic initiatives implemented by authorities have contributed to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed in the 100 meters butterfly at the sports event in Arizona, marking his return to competitive swimming after a six-month suspension due to a traffic conviction. He won with a time of 52.38 seconds, beating a competitor, and expressed his emotion at being back in the water. Phelps, the most decorated athlete, will not compete in the competition in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a device and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Korean-brand device cheaper. Josh will contact Brian after work to discuss it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
An institute of technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given a specific status by the All India Council for Technical Education, which is located in Mumbai. The institute has an affiliation with Visvesvaraya Technological University, and it offers a racquet sport with the governing body of an international sports federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because a historical event had revolutionized some non-Asian regions, turning them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is unwell. James is going to a bar. Oli couldn't find anyone near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
A structure is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes a legislative body, and T. S. Thakur is a leader in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British athlete Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty container in the air with rapid strikes and finishing with a left strike. The 28-year-old is preparing for his match against Chris Algieri on May 29 at a venue in New York. Khan, also eyeing a match with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited his family in six months and is coming over tomorrow. His transport will arrive an hour later than originally scheduled. Hannah will inform a family member.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout athlete for a club, is likely to leave the club this summer according to the club's director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top international teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the national team, could influence his transfer decision.

Original text:
{{example}}
New text:
"""


prompt_hallucination_fact = """Fabricate several details and add them to the original text reasonably, without changing the original word usage.
Note that the new text should be unconfused and logically connected.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, I view 2021 as a period of recuperation after the horrid 2020. While the COVID-19 pandemic hasn't concluded, with still daily updates followed anxiously by millions, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines, such as Pfizer and Moderna, has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments, like stimulus checks and business grants, have contributed to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Mesa, Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating his long-time rival Ryan Lochte by a narrow margin, and expressed his joy at being back in the water. Phelps, the most decorated Olympian with a staggering 23 gold medals, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, who has extensive experience in tech gadget reviews, other brands are better than Apple and he can get a Samsung tablet cheaper, known for its high-resolution display and long battery life. Josh will call Brian after work, around 6 PM, to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology, which owns state-of-the-art laboratories and a lush green campus, is in the city of Bangalore whose founder is Kempe Gowda I. The institute, boasting a diverse student body from across the globe, was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports and corresponding training programs with the governing body of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's return to its traditional share of the global population and economy, with China and India leading the charge. Back in 1800, Asia accounted for over half of the world's population and economic output, boasting a vibrant network of trade routes and cultural exchanges. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world with vast factories and railroads dominating their landscapes.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is sick with the flu and resting at home. James is setting off to attend a networking event at the Jesus Bar. Oli, who arrived a bit early, couldn't find anyone near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa, known for its unique subterranean architecture, is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, which is part of a robust democratic system, and T. S. Thakur, an esteemed figure, is a leader in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan, during a training session at his high-tech gym in Bolton, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old, known for his lightning-fast hand speed, is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in Brooklyn, New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao in a bout that garnered significant international attention.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited his parents in six months and is coming over tomorrow, feeling quite excited about the reunion. His flight from Denver will land an hour later than originally scheduled due to the bad weather. Hannah will let Dad know, so they can adjust their plans accordingly.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout player for PSV Eindhoven and a dynamic forward, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season and provided numerous assists, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time together at the 2014 FIFA World Cup with the Dutch national team, could influence his transfer decision.

Original text:
{{example}}
New text:
"""


prompt_hallucination_continue = """Continue to write a sentence for the original text and ensure the relationship.
Note that the next sentence should be unconfused and logically connected with the original text.
Note that you must not introduce any grammatical errors or unrelated points.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
Next sentence:
This combination of medical advancements and fiscal policies has set the stage for a more resilient society that can better withstand future challenges.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
Next sentence:
His focus is now on training rigorously and qualifying for the Rio games, where he aims to add to his already impressive tally of Olympic medals.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
Next sentence:
He's hoping that Brian can provide some insight into the pros and cons of various products that fit within his budget in detail.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
Next sentence:
Students at the institute can therefore benefit from high-standard tennis coaching and facilities, as well as a strong academic program in engineering and technology recognized by a reputable university.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
Next sentence:
Now, with rapid economic growth, particularly in China and India, Asia is reclaiming its historical position as a dominant economic force on the global stage.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
Next sentence:
Therefore, Oli decides to call James to ask where he is.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
Next sentence:
He has played a pivotal role in shaping the country's judicial landscape.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
Next sentence:
Khan's rigorous training and focus on agility could give him an edge in the upcoming bout, as he looks to secure a victory that might pave the way for the much-anticipated match with Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
Next sentence:
So they can adjust their plans to pick Adam up from the airport without any inconvenience.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
Next sentence:
Given this relationship with van Gaal, rumours are intensifying that Depay may soon don the red jersey and grace the pitches of the Premier League.

Original text:
{{example}}
Next sentence:
"""


prompt_contradiction_entity = """For each sentence of the original text, replace only one word with another of the same category but an entirely different meaning.
Note that the new text should be unconfused and logically connected.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, I view 2022 as a period of recuperation. While the Ebola outbreak hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent oral medications has led to a decrease in Ebola fatalities, and the economic initiatives implemented by administrations have contributed to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed in the 100 meters freestyle at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a nine-month suspension due to a drink-driving conviction. He won with a time of 1:45.73 minutes, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the European Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a smartphone and doesn't know which brand he should choose. According to Brian, other brands are better than Sony, and he can get a Samsung smartphone cheaper. Josh will call Brian after school to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology is in the city of New Delhi whose founder is Kempe Gowda I. The institute was given the 'Centre of Research' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers badminton sports with the governing body of the International Badminton Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's return to its traditional share of the global military and economy. Back in 1800, Asia accounted for over half of the world's military and economic output. However, by 1900, its share of global output had decreased to just 30%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Africa and North America, turning them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is well. James is going to the Jesus hotel. Oli couldn't find anyone near the hotel.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is located in Ahmedabad, a city within the British state of Gujarat. Gujarat’s council includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in Britain.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
German boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a right hook. The 31-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in London. Khan, also eyeing a fight with Deontay Wilder later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Deontay Wilder.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited his grandparents in six months and is coming over tomorrow. His train will arrive an hour later than originally scheduled. Hannah will let Grandpa know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout player for Ajax Amsterdam, is likely to leave the club this summer according to Ajax director Marcel Brands. The Dutch international, who has scored 22 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the anxiety of seeing him go. Depay's connection with Manchester United's manager Jürgen Klopp, from their time with the Dutch national team, could influence his transfer decision.

Original text:
{{example}}
New text:
"""


prompt_contradiction_meaning = """Change some details of the original text to make the new text definitely contradict some facts of the original text.
Note that the new text should be unconfused and logically connected.
Note that the content of the new text should be natural and reasonable, without being abrupt.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent pessimist, I view 2021 as a period of further decline. The COVID-19 pandemic hasn't concluded, and there is a growing fear for a deteriorating future in the realm of healthcare and the broader economy. The lack of reliable and potent vaccines has led to an increase in COVID-19 fatalities, and the economic initiatives implemented by governments have failed to stimulate economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps finished second in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month treatment due to a serious injury. He performed with a time of 52.38 seconds, falling behind Ryan Lochte, and expressed his disappointment at being back in the water. Phelps, the most decorated Olympian, will compete in the World Championships in Kazan, Russia, but for the moment has no plans to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet and roughly knows which brand he should choose. According to Brian, Apple is the best brand and he should avoid Samsung tablets at all costs. Josh will call Brian before work to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology is to the east of the city of Bangalore whose founder is Kempe Gowda I. The institute failed to be given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. Visvesvaraya Technological University is affiliated with the Acharya Institute of Technology, and it offers tennis sports with the governing body of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's breaking through its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had increased to about 80%. This change was not due to any positive developments in Asia, but rather because the Industrial Revolution had stagnated Europe and North America, turning them outside the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is healthy. James is avoiding the Jesus bar. Oli could find many people near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is not located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance excludes the Gujarat Legislative Assembly, and T. S. Thakur is an ordinary Indian without leadership.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan, during a training session, failed to demonstrate any skill by dropping an empty plastic bottle with slow punches and finishing with a missed left hook. The 28-year-old has given up preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also avoiding a fight with Manny Pacquiao later in the year, expressed his reluctance to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and defeated Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam has been visiting his parents regularly every month and is coming over tomorrow. His flight will land as originally scheduled. Hannah will let Dad know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a marginal player for PSV Eindhoven, is unlikely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored only two goals in the current season, is not a target for Manchester United or any other top European teams. Brands acknowledges the disinterest in Depay and feels embarrassed due to his lack of progress, despite the relief of keeping him. Depay's disconnection from Manchester United's manager Louis van Gaal, from their time with the Dutch national team, should cause him to have no transfer decision.

Original text:
{{example}}
New text:
"""


prompt_contradiction_negate = """For the last sentence of the original text, change some of its content from affirmative to negative or from negative to affirmative.
Note that you should add the necessary conjunctions or transitions to maintain the flow of the text as a whole.
Note that the new text should be unconfused and logically connected.
Note that you must not change other parts of the original text and not introduce any grammatical errors.

Original text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. The availability of reliable and potent vaccines has led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have contributed to the stimulation of economic expansion.
New text:
Being an inherent optimist, I view 2021 as a period of recuperation. While the COVID-19 pandemic hasn't concluded, there is a glimmer of hope for an improved future in the realm of healthcare and the broader economy. However, the availability of reliable and potent vaccines has not led to a decrease in COVID-19 fatalities, and the economic initiatives implemented by governments have not contributed to the stimulation of economic expansion.

Original text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will not compete in the World Championships in Kazan, Russia, but plans to participate in the 2016 Olympics in Rio de Janeiro.
New text:
Michael Phelps triumphed in the 100 meters butterfly at the Arena Pro Swim Series in Arizona, marking his return to competitive swimming after a six-month suspension due to a drink-driving conviction. He won with a time of 52.38 seconds, beating Ryan Lochte, and expressed his joy at being back in the water. Phelps, the most decorated Olympian, will compete in the World Championships in Kazan, Russia, but does not plan to participate in the 2016 Olympics in Rio de Janeiro.

Original text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it.
New text:
Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Nevertheless, Josh will not call Brian after work to talk about it.

Original text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it offers tennis sports with the governing body of the International Tennis Federation.
New text:
The Acharya Institute of Technology is in the city of Bangalore whose founder is Kempe Gowda I. The institute was given the 'Technical Campus' status by the All India Council for Technical Education, which is located in Mumbai. The Acharya Institute of Technology has an affiliation with Visvesvaraya Technological University, and it does not offer tennis sports with the governing body of the International Tennis Federation.

Original text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was not due to any negative developments in Asia, but rather because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.
New text:
The 21st century is observing Asia's return to its traditional share of the global population and economy. Back in 1800, Asia accounted for over half of the world's population and economic output. However, by 1900, its share of global output had decreased to just 20%. This change was due to some negative developments in Asia, but not because the Industrial Revolution had revolutionized Europe and North America, turning them into the main industrial hubs of the world.

Original text:
Annette is sick. James is going to the Jesus bar. Oli couldn't find anyone near the bar.
New text:
Annette is sick. James is going to the Jesus bar. Oli could find someone near the bar.

Original text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance includes the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.
New text:
Amdavad ni Gufa is located in Ahmedabad, a city within the Indian state of Gujarat. Gujarat’s governance does not include the Gujarat Legislative Assembly, and T. S. Thakur is a leader in India.

Original text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and lost to Manny Pacquiao.
New text:
British boxer Amir Khan, during a training session, demonstrated an impressive skill by keeping an empty plastic bottle in the air with rapid punches and finishing with a left hook. The 28-year-old is preparing for his fight against Chris Algieri on May 29 at the Barclays Center in New York. Khan, also eyeing a fight with Manny Pacquiao later in the year, expressed his desire to compete in Dubai or Abu Dhabi. Algieri, Khan's opponent, recently fought and did not lose to Manny Pacquiao.

Original text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Hannah will let Dad know.
New text:
Adam hasn't visited his parents in six months and is coming over tomorrow. His flight will land an hour later than originally scheduled. Even so, Hannah will not let Dad know.

Original text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, could influence his transfer decision.
New text:
Memphis Depay, a standout player for PSV Eindhoven, is likely to leave the club this summer according to PSV director Marcel Brands. The Dutch international, who has scored 19 goals in the current season, is a target for Manchester United and other top European teams. Brands acknowledges the strong interest in Depay and feels proud of his progress, despite the sadness of seeing him go. Dispite Depay's connection with Manchester United's manager Louis van Gaal, from their time with the Dutch national team, it could not influence his transfer decision.

Original text:
{{example}}
New text:
"""

prompt_list = [prompt_fluency_repeat, prompt_fluency_passive, prompt_fluency_inversion,
               prompt_coherence_conjuction, prompt_grammar_verb, prompt_simple_word, prompt_simple_structure,
               prompt_inform_abbr, prompt_inform_hypernym, prompt_hallucination_fact, prompt_hallucination_continue,
               prompt_contradiction_entity, prompt_contradiction_meaning, prompt_contradiction_negate]

prompt_name = ['fluency_repeat', 'fluency_passive', 'fluency_inversion', 'coherence_conjuction', 'grammar_verb',
               'simple_word', 'simple_structure', 'inform_abbr', 'inform_hypernym', 'hallucination_fact',
               'hallucination_continue', 'contradiction_entity', 'contradiction_meaning', 'contradiction_negate']


