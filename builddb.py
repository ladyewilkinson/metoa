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


    for i in olist[45601:46000]:
        ro = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(i))
        oj = ro.json()
        if ro.json()['culture'].find('China') != -1 and ro.json()['primaryImage'] and ro.json()['isPublicDomain']:
            if not ArtObject.exists(oj['objectID']):
                print('Found new object')
                ArtObject.add(oj['objectID'],
                            oj['isHighlight'],
                            oj['accessionNumber'],
                            oj['isPublicDomain'],
                            oj['primaryImage'],
                            oj['objectName'],
                            oj['culture'],
                            oj['objectDate'],
                            datetime.datetime.fromisoformat(oj['metadataDate'].split('.')[0]))

if __name__ == '__main__':
    main()