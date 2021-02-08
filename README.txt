# googleforms
Google Form Submitter
 This program is to automate the purpose of answering a google form on behalf of you
 now you can use this program to give more responses than usual 
 now u are able to answer it as much as u want
 
 
 
 about the google form i used:
 it had 5 questions with 6 multiple choice options each and therefore we use random to give random output each time
 number of check boxes = 6*5 = 30 therefore the number varies
 a = random.randint(0, 5)
 radiobuttons[a].click()
 b = random.randint(6, 11)
 radiobuttons[b].click()
 thats why we give values till 30 and for first question it is between 0-5 and second question 6-11
 
 then textboxes can be given list number accordingly
 if theres only one text box then 
  textboxes.click() is fine
 if theres more
 you can use textboxes[0],textboxes[1] etc
 
 same thing for submit button too
