## How we built it

Backend- Flask
Frontend- Bootstrap5
Model Training- SageMaker + PyTorch
Storage- S3
LLM Models- Gemini 2.5 Pro, ChatGPT 5

## Challenges we ran into

Due to time constraints, we wanted to find a dataset that was already labeled. Labeling turned out to be quite a large issue in chest X-rays: the Kaggle description actually states "One major hurdle in creating large X-ray image datasets is the lack resources for labeling so many images." We found one dataset that was around 120k images and was labeled using Natural Language Processing (accuracy around 90%,) and initially had issue with uploading such a large amount of images into an S3 bucket. One of the AWS mentors suggested that we split the image uploads between all our computers, which helped, but we still ran into bandwidth issues.

Initially, we were planning to do an all-in-one model, but after doing analysis on the data set, we realized that:
a) some of the images had multiple diseases labeled together. 
b) a large amount of the scans (52%) were labeled as "No Finding," only leaving around 31k images that had both a single label and were not "No Finding."
After this realization we switched to a binary classification model with the goal of determining whether or not a scan was a specific disease, instead of trying to guess what it could be a combination of.

## Accomplishments that we're proud of

Despite it being our first time using SageMaker, on top of working with a limited data set, we were proud that we were able to successfully create a model, exporting it to S3 so that we could have an inference endpoint callable from our own backend.

Additionally, coming into the hackathon, we actually didn't do much planning and brainstorming. As soon as we came up with an idea however, we were extremely diligent in deciding a good project structure, and all the individual parts that we would need to flesh out.