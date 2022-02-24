# Political-Article-Generator
AI writer build with GRU

### Train data and models
All of the training data is collected from wikipedia. Links can be found in the file `politic_meta.txt`. Every article is hand-picked and is related to political concepts, history or economic background. Total train file size is about 3M and containes more than 6,000,000 words.
Word2Vec model is trained based on wikipedia dump (English version). The model is about 300M, contianing nearly 40,000 distinct words.

**All of the models are available in the release version.** I also provide train and test script in the format of ipython notebook.

## WARNING: Controversial content  
I can not control what the AI learn from those article
**Generated text may be controversial, offensive and biased. Use with your own caution.**

## Result Showcase (Web Application)

<img width="1346" alt="Screen Shot 2022-02-24 at 10 12 37 PM" src="https://user-images.githubusercontent.com/63455223/155540838-1e5e323c-f24a-43f6-9273-f27aceb8d2d6.png">

## Usage
<ul>
    <li> <b>Initial text</b>: AI will read these words and attempt to predict the rest of the article.
    <li> <b>Model Version</b>: The release includes 4 version of model. `v4` is the best one.
    <li> <b>Temperature</b>: The higher the more diversity the generated content will be. But may cause increase of grammer error rate. Personally I suggest it be set at least 0.4.  
    <li> <b>Randomness</b>: If temperature is not set to zero, every time `Gerenate` button is hit model will output a different article.
</ul>
