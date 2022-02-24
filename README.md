# Political-Article-Generator
AI writer build with GRU

### Train data
All of the training data is collected from wikipedia. Links can be found in the file `politic_meta.txt`.
Word2Vec model is trained based on wikipedia dump (English version).

## WARNING: Controversial content  
**Generated text may be controversial, offensive and biased. Use with your own caution.**

## Result Showcase (Web Application)

<img width="1433" alt="Screen Shot 2022-02-24 at 9 37 41 PM" src="https://user-images.githubusercontent.com/63455223/155537071-5524eaf6-4bbe-43d7-8e1a-1edc0529fd37.png">

## Usage
<ul>
    <li> <b>Initial text</b>: AI will read these words and attempt to predict the rest of the article.
    <li> <b>Model Version</b>: The release includes 4 version of model. `v4` is the best one.
    <li> <b>Temperature</b>: The higher the more diversity the generated content will be. But may cause increase of grammer error rate. Personally I suggest it be set at least 0.4.  
    <li> <b>Randomness</b>: If temperature is not set to zero, every time `Gerenate` button is hit model will output a different article.
</ul>
