import requests
import sys, os
import json
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

# Microsoft Azure Api
def get_links(query):
    subscription_key = "17900a16b2334f0ebfc58074f465c7ae"
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    # search_term = "puppies"

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

    params  = {"q": query, "license": "public", "imageType": "photo"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    image_count = 10 #len(search_results["value"])
    for i in range(0,image_count):
        try:
            os.chdir(os.getcwd()+"\\downloadedImages\\")
            f = open(str(i)+'.jpg','wb')
            f.write(requests.get(search_results["value"][i]["contentUrl"]).content)

            original = cv2.imread(str(i)+".jpg")
            image_to_compare = cv2.imread("0.jpg")
        
            # 1) Check if 2 images are equals
            if original.shape == image_to_compare.shape:
                #print("The images have same size and channels")
                difference = cv2.subtract(original, image_to_compare)
                b, g, r = cv2.split(difference)

            # 2) Check for similarities between the 2 images
            sift = cv2.xfeatures2d.SIFT_create()
            kp_1, desc_1 = sift.detectAndCompute(original, None)
            kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)    

            index_params = dict(algorithm=0, trees=5)
            search_params = dict()
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            #print(desc_1)
            matches = flann.knnMatch(desc_1, desc_2, k=2)

            good_points = []
            for m, n in matches:
                if m.distance < 0.6*n.distance:
                    good_points.append(m)

            # Define how similar they are
            number_keypoints = 0
            if len(kp_1) <= len(kp_2):
                number_keypoints = len(kp_1)
            else:
                number_keypoints = len(kp_2)

            #print("Keypoints 1ST Image: " + str(len(kp_1)))
            #print("Keypoints 2ND Image: " + str(len(kp_2)))
            #print("GOOD Matches:", len(good_points))
            similarity_index = len(good_points) / number_keypoints * 100
            print("How good it's the match "+str(i)+" : ", similarity_index)
            search_results["value"][i]["similarity_index"] = similarity_index
            f.close()
        except:
            print(i)
            search_results["value"][i]["similarity_index"] = 0
            continue

    return json.dumps(search_results["value"])

# Google Custom Search Api
# def get_links(query):
#     links = []
#     s = requests.Session()
#     print(s)
#     search = query
#     apiKey='AIzaSyBwztasUrFiro_qsE8pD-maCL_m8JrgMcQ'
#     cx='013994057420626416686:kihsqrvoppq'
#     body = s.get(f'https://www.googleapis.com/customsearch/v1?q={search}&key={apiKey}&cx={cx}&num=10&searchtype=image', params = {})
#     #print(body.content)
#     data=json.loads(body.content)
#     return data
#     # for img in data["items"]:
#     #     links.append(img["pagemap"]["cse_image"][0]["src"]) 
#     # return links