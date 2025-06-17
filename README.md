# animerecommandation
comet set in model training 
  self.experiment = comet_ml.Experiment(
            api_key="8zz4haNEY0Hsrz7C43UskfuPN",
            project_name="animep",
            workspace="Bhati90"
        )
        logger.info("Model Training & COMET ML initialized..")
    


dvc set up in gcp
dvc init
dvc add raw weights artifacts 
dvc add remote gs:// bucket-name
dvc remote modify myremote credentialpath address to recom.json
push

Anime Recommendation System
Project Overview
This project is an Anime Recommendation System that provides personalized anime suggestions based on user preferences and content similarity. It uses a hybrid approach combining collaborative filtering (user-based) and content-based recommendation techniques to deliver accurate and diverse recommendations.

Features
Hybrid Recommendation Engine: Combines user preferences and anime content features for balanced recommendations.

Content-Based Filtering: Recommends anime similar to ones the user has watched or liked.

User-Based Filtering: Suggests anime enjoyed by users with similar tastes.

Genre Analysis: Visualizes user preferences using a word cloud of favorite genres.

Detailed Anime Information: Provides synopses, genres, and ratings for recommended anime.

Project Structure
text
.dvc
.gitignore
config/
artifacts/
model.dvc
model_checkpoint.dvc
processed.dvc
raw.dvc
weights.dvc
config/
__pycache__/
__init__.py
config.yaml
paths_config.py
custom_jenkins/
Dockerfile
notebook/
anime.ipynb
weights.weights.h5
pipeline/
__pycache__/
__init__.py
prediction_pipeline.py
training_pipeline.py
src/
__pycache__/
__init__.py
base_model.py
custom_exception.py
data_ingestion.py
data_processing.py
helpers.py
logger.py
model_training.py
static/
style.css
templates/
index.html
utils/
__pycache__/
__init__.py
common_functions.py
.dvcignore
.gitignore
Dockerfile
Jenkinsfile
README.md
application.py
readme.md
requirements.txt
setup.py
tester.py
Key Components
Data Processing:

Handles large datasets (5M+ ratings)

Normalizes ratings and encodes user/anime IDs

Splits data into training and test sets

Model Architecture:

Embedding layers for users and anime

Dot product similarity calculation

Dense layers with sigmoid activation

Batch normalization for stability

Recommendation Methods:

find_similar_animes(): Content-based recommendations

find_similar_users(): Finds users with similar tastes

hybrid_recommendation(): Combines both approaches

Usage
To get recommendations for a user:

python
recommendations = hybrid_recommendation(user_id=11880, 
                                      user_weight=0.5, 
                                      content_weight=0.5)
Requirements
Python 3.7+

TensorFlow 2.x

Pandas, NumPy

WordCloud (for visualization)

DVC (for data versioning)

Results
The system successfully recommends popular anime like:

Code Geass

Death Note

Steins;Gate

Attack on Titan

Fate/Zero

With balanced weighting between user preferences and content similarity.

Future Improvements
Add more sophisticated feature engineering

Implement real-time updates to user preferences

Develop a web interface for easier interaction

Incorporate more anime metadata for better recommendations
