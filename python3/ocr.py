#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:25:26 2024

@author: mike
"""

from subprocess import CalledProcessError
import subprocess 
from django.conf import settings
from datetime import datetime
import logging
from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/mike/Documents/prestoch-ae89fcfa026f.json"    

# copied from: /var/lib/jenkins/workspace/chequeli/01-Login
# originally from https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/detect/detect.py
# needs export GOOGLE_APPLICATION_CREDENTIALS=/home/mike/Documents/presto-bites/prestoch-ae89fcfa026f.json
# [START vision_text_detection_gcs]
def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web."""
    startTime = datetime.now()
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
        
    logger.info('detect_text_uri(): ' + str(datetime.now() - startTime) + ' taken to process ' + uri + ' extracted: ' + str(len(texts[0].description))) 
    return texts[0].description;
# [END vision_text_detection_gcs]

# ContextualVersionConflict: (google-api-core 2.17.1 (/home/mike/anaconda3/lib/python3.10/site-packages), Requirement.parse('google-api-core[grpc]<2.0.0dev,>=1.14.0'), {'google-cloud-vision'})

# ImportError: cannot import name 'image_annotator' from 'google.cloud.vision_v1.types' (/home/mike/anaconda3/lib/python3.10/site-packages/google/cloud/vision_v1/types.py)

detect_text_uri('https://bochenek.ch/media/20240202_153004.jpg')
