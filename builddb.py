from settings import *
from ArtObjectModel import *

import requests
import json
import datetime
import os
import shutil



def main():

    r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects')

    total = r.json()['total']
    olist = r.json()['objectIDs']

    print('There are {} objects.'.format(total))


    for i in olist[47001:49000]:
        ro = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(i))
        oj = ro.json()
        if ro.json()['culture'].find('China') != -1 and ro.json()['primaryImage'] and ro.json()['isPublicDomain']:
            if not ArtObject.exists(oj['objectID']):
                print('Found new object')
                mdate = oj['metadataDate'].split('.')[0]
                md = mdate[:-1] if mdate[-1].isalpha() else mdate
                ArtObject.add(oj['objectID'],
                            oj['isHighlight'],
                            oj['accessionNumber'],
                            oj['isPublicDomain'],
                            oj['primaryImage'],
                            oj['objectName'],
                            oj['culture'],
                            oj['objectDate'],
                            datetime.datetime.fromisoformat(md))

if __name__ == '__main__':
    main()