1. For this case study, i have created a new environment called "foodierasa" and below are the component details and its versions. 

2. I have also copied the screen shot form my testing and its available in the document StoriesScreenShots.docx 

3. Rasa version used for this case study is 2.0.0

4. Python version used for this case study is 3.7.9

5. Command used to train 

rasa train --force --config config.yml

6. Command used to test

rasa shell


(base) C:\WINDOWS\system32>cd..

(base) C:\Windows>cd..

(base) C:\>cd users

(base) C:\Users>cd phani

(base) C:\Users\phani>cd rasa

(base) C:\Users\phani\rasa>cd foodi*

(base) C:\Users\phani\rasa\foodiechatbot>activate foodierasa

(foodierasa) C:\Users\phani\rasa\foodiechatbot>pip freeze
absl-py==0.10.0
aiofiles==0.5.0
aiohttp==3.6.3
APScheduler==3.6.3
astunparse==1.6.3
async-generator==1.10
async-timeout==3.0.1
attrs==20.2.0
blis==0.4.1
boto3==1.15.18
botocore==1.18.18
cachetools==4.1.1
catalogue==1.0.0
certifi==2020.6.20
cffi==1.14.3
chardet==3.0.4
cloudpickle==1.4.1
colorclass==2.2.0
coloredlogs==14.0
colorhash==1.0.2
cryptography==3.1.1
cycler==0.10.0
cymem==2.0.3
decorator==4.4.2
dm-tree==0.1.5
dnspython==1.16.0
docopt==0.6.2
en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.2.5/en_core_web_md-2.2.5.tar.gz
fbmessenger==6.0.0
future==0.18.2
gast==0.3.3
google-auth==1.22.1
google-auth-oauthlib==0.4.1
google-pasta==0.2.0
grpcio==1.32.0
h11==0.9.0
h5py==2.10.0
httpcore==0.11.1
httplib2==0.18.1
httptools==0.1.1
httpx==0.15.4
humanfriendly==8.2
idna==2.10
importlib-metadata==2.0.0
jmespath==0.10.0
joblib==0.15.1
jsonpickle==1.4.1
jsonschema==3.2.0
kafka-python==2.0.2
Keras-Preprocessing==1.1.2
kiwisolver==1.2.0
Markdown==3.3.1
matplotlib==3.3.2
mattermostwrapper==2.2
multidict==4.7.6
murmurhash==1.0.2
networkx==2.5
numpy==1.18.1
oauth2client==4.1.3
oauthlib==3.1.0
opt-einsum==3.3.0
packaging==20.4
pika==1.1.0
Pillow==8.0.0
plac==1.1.3
preshed==3.0.2
prompt-toolkit==2.0.10
protobuf==3.13.0
psycopg2-binary==2.8.6
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
pydot==1.4.1
PyJWT==1.7.1
pykwalify==1.7.0
pymongo==3.10.1
pyparsing==2.4.7
pyreadline==2.1
pyrsistent==0.17.3
python-crfsuite==0.9.7
python-dateutil==2.8.1
python-engineio==3.13.2
python-socketio==4.6.0
python-telegram-bot==12.8
pytz==2020.1
PyYAML==5.3.1
questionary==1.5.2
rasa==2.0.0
rasa-sdk==2.0.0
redis==3.5.3
regex==2020.9.27
requests==2.24.0
requests-oauthlib==1.3.0
requests-toolbelt==0.9.1
rfc3986==1.4.0
rocketchat-API==1.9.1
rsa==4.6
ruamel.yaml==0.16.12
ruamel.yaml.clib==0.2.2
s3transfer==0.3.3
sanic==20.9.0
Sanic-Cors==0.10.0.post3
sanic-jwt==1.4.1
Sanic-Plugins-Framework==0.9.4
scikit-learn==0.23.2
scipy==1.5.3
sentry-sdk==0.17.8
six==1.15.0
sklearn-crfsuite==0.3.6
slackclient==2.9.2
sniffio==1.2.0
spacy==2.2.4
SQLAlchemy==1.3.20
srsly==1.0.2
tabulate==0.8.7
tensorboard==2.3.0
tensorboard-plugin-wit==1.7.0
tensorflow==2.3.1
tensorflow-addons==0.11.2
tensorflow-estimator==2.3.0
tensorflow-hub==0.9.0
tensorflow-probability==0.11.1
termcolor==1.1.0
terminaltables==3.1.0
thinc==7.4.0
threadpoolctl==2.1.0
tornado==6.0.4
tqdm==4.50.2
twilio==6.45.4
typeguard==2.10.0
typing-extensions==3.7.4.3
tzlocal==2.1
ujson==3.2.0
urllib3==1.25.10
wasabi==0.8.0
wcwidth==0.2.5
webexteamssdk==1.6
websockets==8.1
Werkzeug==1.0.1
wincertstore==0.2
wrapt==1.12.1
yarl==1.5.1
zipp==3.3.1

(foodierasa) C:\Users\phani\rasa\foodiechatbot>python
Python 3.7.9 (default, Aug 31 2020, 17:10:11) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>  