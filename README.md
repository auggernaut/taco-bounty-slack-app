# Taco Bounty
A slack app that lets users create taco bounties.

## Credit
Based on the Reflect Slack App by Will Larson  
A simple example of a Slack application to go along with work-in-progress blog post at  
https://lethain.com/creating-slack-app-python/

## Setup
### Install Google Cloud CLI:
https://cloud.google.com/sdk/docs/install

### Set Env
mv the service_account.json file to `reflect` directory  
update `reflect/env.yaml` with slack credentials

### Test locally
Set env variable `export GOOGLE_APPLICATION_CREDENTIALS="[PATH_TO_JSON]"`  
open a virtual env `source ../venv/bin/activate`  
install `pip install google-cloud-firestore==1.6.0`  
poke around  
```
>>> from google.cloud import firestore
>>> db = firestore.Client()
>>> doc = db.collection('users').document('lethain')
>>> doc.set({'name': 'lethain', 'team': 'ttttt'})
```

### Deploy scripts to gcloud
`cd reflect`  
`gcloud functions deploy dispatch --env-vars-file env.yaml --runtime python37 --trigger-http`
