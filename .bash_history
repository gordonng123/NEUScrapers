git clone https://github.com/GoogleCloudPlatform/python-docs-samples
cd python-docs-samples/appengine/standard_python37/hello_world
cat main.py
cat app.yaml
virtualenv --python python3 ~/envs/hello_world
source ~/envs/hello_world/bin/activate
pip install -r requirements.txt
python main.py
git clone https://github.com/GoogleCloudPlatform/nodejs-getting-started
cd nodejs-getting-started/1-hello-world
ls
export PORT=8080 && npm install
cloudshell launch-tutorial /google/devshell/tutorials/custom-image-tutorial.md
npm start
wget google.com
wget tripadvisor.com
npm start
ls
cd envs
npm start
git init
git status
git status -v
git remote show
cloudshell launch-tutorial /google/devshell/tutorials/custom-image-tutorial.md
ls
clear 
ls
cd nodejs-getting-started
ls 
cd hello-world
ls
cd 1-hello-world
ls
npm start
ls
cd
ls
git remote add yaleproject https://github.com/gordonng123/NEUScrapers.git
cd envs
ls
git status
cd/
cd
ls
git init
ls
git status
cd envs
git status
cd
ls
git remote add yaleproject https://github.com/gordonng123/NEUScrapers.git
ls
git add all.
git add .
git -config
git add .
git add.
git add
git add .
git status
git remote show
git remote show -v
git remote -v
git commit -m '1st'
git config --global user.email "zhao.yi4@husky.neu.edu"
git config --global user.name "yaleduffy"
git commit -m 'lol'
git status
git push
git push yaleproject master
git pull
git pull yaleproject
git push yaleproject master
git pull
git merge yaleproject
git merge yaleproject master
git 
git status
git branch
git push --force yaleproject master
clear
Install-Package Google.Cloud.Language.V1 -Pre
clear 
export GOOGLE_APPLICATION_CREDENTIALS="/Users/yaleduffy/Desktop/YaleProject-d4b4a18b7f6e.json"
npm install --save @google-cloud/language
mkdir sent_python
cd sent_python
pip install --upgrade google-cloud-language
pip3 install --upgrade google-cloud-language
lds
ls
cd sent_python
ls
.test.py
python .test.py
clear
python test
clear
ls
python test.py
ls
export GOOGLE_APPLICATION_CREDENTIALS="/Users/yaleduffy/Desktop/YaleProject-d4b4a18b7f6e.json"
ls
python test.py
ls
export GOOGLE_APPLICATION_CREDENTIALS="/Users/yaleduffy/Desktop/YaleProject-d4b4a18b7f6e.json"
clear
export GOOGLE_APPLICATION_CREDENTIALS="/Users/yaleduffy/Desktop/YaleProject-d4b4a18b7f6e.json"
python test.py
python3 test.py
echo $CREDENTIALS
pwd
export GOOGLE_APPLICATION_CREDENTIALS="/home.yaleduffy/YaleProject-d4b4a18b7f6e.json"
export GOOGLE_APPLICATION_CREDENTIALS="/home/yaleduffy/YaleProject-d4b4a18b7f6e.json"
python3 test.py
pwd
clear 
gsutil cp gs://cloud-samples-tests/natural-language/sentiment-samples.tgz .
gunzip sentiment-samples.tgz
tar -xvf sentiment-samples.tar
ls
touch test2.py
ls
rm sentiment-samples.tar
ls
clear 
python test2.py reviews/bladerunner-neg.txt
touch test3.py
ls
clear 
python test3.py classify "Twitter declined to say why it has started showing more ads to its power users. But it appears to have made the change not long after introducing new ad targeting processes in August that reportedly caused some advertisers to pull spending. Affected users seem to have gone from seeing either no ads or very few ads to seeing about one for every eight or 10 tweets in their feed."
python test3.py classify "Google Home enables users to speak voice commands to interact with services through the Home's intelligent personal assistant called Google Assistant. A large number of services, both in-house and third-party, are integrated, allowing users to listen to music, look at videos or photos, or receive news updates entirely by voice. "
ls
clear
python test3.py index reviews
python test3.py index sent_python/reviews
python test3.py classify "I prided myself on being someone who could take care of the entire bill when going out with friends; going dutch was not a concept I grew up with. I never had to think twice about my purchases — and now I had to budget every dinner I ate, every event I attended, and every dollar I spent. The days of $8 oat milk matcha lattes were in the past. My FOMO was not one of fear but frustration."
python3 test3.py classify "I prided myself on being someone who could take care of the entire bill when going out with friends; going dutch was not a concept I grew up with. I never had to think twice about my purchases — and now I had to budget every dinner I ate, every event I attended, and every dollar I spent. The days of $8 oat milk matcha lattes were in the past. My FOMO was not one of fear but frustration."
python test3.py classify "I prided myself on being someone who could take care of the entire bill when going out with friends; going dutch was not a concept I grew up with. I never had to think twice about my purchases — and now I had to budget every dinner I ate, every event I attended, and every dollar I spent. The days of $8 oat milk matcha lattes were in the past. My FOMO was not one of fear but frustration."
ls
cd sent_python
ls
python test3.py classify "I prided myself on being someone who could take care of the entire bill when going out with friends; going dutch was not a concept I grew up with. I never had to think twice about my purchases — and now I had to budget every dinner I ate, every event I attended, and every dollar I spent. The days of $8 oat milk matcha lattes were in the past. My FOMO was not one of fear but frustration."
ls
cd
ls
pwd
cd sent_python
ls
export GOOGLE_APPLICATION_CREDENTIALS="/home/yaleduffy/YaleProject-d4b4a18b7f6e.json"
ls
python test3.py classify "I prided myself on being someone who could take care of the entire bill when going out with friends; going dutch was not a concept I grew up with. I never had to think twice about my purchases — and now I had to budget every dinner I ate, every event I attended, and every dollar I spent. The days of $8 oat milk matcha lattes were in the past. My FOMO was not one of fear but frustration."
python test3.py classify "Google Home enables users to speak voice commands to interact with services through the Home's intelligent personal assistant called Google Assistant. A large number of services, both in-house and third-party, are integrated, allowing users to listen to music, look at videos or photos, or receive news updates entirely by voice. "
python test3.py classify "oogle Home enables users to speak voice commands to interact with services through the Home's intelligent personal assistant called Google Assistant. A large number of services, both in-house and third-party, are integrated, allowing users to listen to music, look at videos or photos, or receive news updates entirely by voice. "
python test3.py classify "It’s situations like these that pediatrician Mark Hanna considered while walking to his job as a resident physician at Kings County Hospital in Brooklyn, New York. Hanna tells OneZero that he saw ambulances “struggling to get past” rush-hour traffic and wondered whether they’d actually reach patients before it was too late."
ls
cd sent_python
ls
python test3.py classify "It’s situations like these that pediatrician Mark Hanna considered while walking to his job as a resident physician at Kings County Hospital in Brooklyn, New York. Hanna tells OneZero that he saw ambulances “struggling to get past” rush-hour traffic and wondered whether they’d actually reach patients before it was too late."
export GOOGLE_APPLICATION_CREDENTIALS="/home/yaleduffy/YaleProject-d4b4a18b7f6e.json"
python test3.py classify "It’s situations like these that pediatrician Mark Hanna considered while walking to his job as a resident physician at Kings County Hospital in Brooklyn, New York. Hanna tells OneZero that he saw ambulances “struggling to get past” rush-hour traffic and wondered whether they’d actually reach patients before it was too late."
python test3.py index reviews
python test3.py classify "It’s situations like these that pediatrician Mark Hanna considered while walking to his job as a resident physician at Kings County Hospital in Brooklyn, New York. Hanna tells OneZero that he saw ambulances “struggling to get past” rush-hour traffic and wondered whether they’d actually reach patients before it was too late."
python test2.py
ls
cd sent_python
ls
python test2.py
python test2.py analyze reviews
python test2.py index reviews
python test2.py analyze reviews
python test2.py index reviews
python test2.py analyze reviews
python origin_sentiment.py reviews/bladerunner-pos.txt
export GOOGLE_APPLICATION_CREDENTIALS="/home/yaleduffy/YaleProject-d4b4a18b7f6e.json"
python origin_sentiment.py reviews/bladerunner-pos.txt
python test2.py analyze reviews
python origin_sentiment.py reviews/bladerunner-neutral.txt
python test2.py analyze reviews
python origin_sentiment.py reviews/bladerunner-neutral.txt
python origin_sentiment.py exp.json
python origin_sentiment.py lol
python origin_sentiment.py exp.json
with open(string) as f:
clear 
python json_sentiment.py 
cd
ls
git pull
python json_sentiment.py 
cd sent_python
ls
python json_sentiment.py 
python test4.py
cd
ls
git pull
git remote show
git remote show yaleproject
git remote d
git remote -d yaleproject
git remote remove yaleproject
git remote show yaleproject
git remote add https://github.com/nicholasmullikin/neu_scrapers.git
git remote add yp https://github.com/nicholasmullikin/neu_scrapers.git
git pull
git remote
git pull yp
git remote show ypp
git remote show yp
git pull
git pull yp
git pull yp master
git status
nano .gitignore
git status
nano .gitignore 
git status
rm node_modules/
rm -rf node_modules/
git status
nano .gitignore 
git status
rm package-lock.json 
nano .gitignore 
git status
git add .
git status
nano .gitignore 
git status
git rm .npm/*
git rm -r .npm/*
git rm -r .npm/
git rm -rf .npm/
git status
git add .
git pull
git pull origin
git pull yp
git pull yp mastert
git pull yp master
git add .
git commit -m "changes"
git pull 
git pull yp master
git pull yp master -f
git pull yp master --force
git pull yp master --f
git pull -f yp master
git checkout .bash_history yp master
git checkout yp master -- .bash_history
nano .gitignore 
git status
