import face_recognition
import pickle
import cv2
import os
from imutils import paths
import sys

def main(image):

        path = os.path.dirname(os.path.realpath(__file__)) 
        # load the known faces and embeddings
        print("[INFO] loading encodings...")
        data = pickle.loads(open(path + '\\encoding.pickle', "rb").read())

        image = cv2.imread(img)
        boxes = face_recognition.face_locations(image,model='hog')
        encodings = face_recognition.face_encodings(image, boxes)
        # initialize the list of names for each face detected
        print(img)
        names = []
        # loop over the facial embeddings
        for encoding in encodings:
                # attempt to match each face in the input image to our known encodings
                matches = face_recognition.compare_faces(data["encodings"],encoding,tolerance = 0.45)
                name = "Unknown"

                # check to see if we have found a match
                if True in matches:
                        # find the indexes of all matched faces then initialize a
                        # dictionary to count the total number of times each face
                        # was matched
                        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}

                        # loop over the matched indexes and maintain a count for
                        # each recognized face face
                        for i in matchedIdxs:
                                name = data["names"][i]
                                counts[name] = counts.get(name, 0) + 1

                        # determine the recognized face with the largest number of
                        # votes (note: in the event of an unlikely tie Python will
                        # select first entry in the dictionary)
                        name = max(counts, key=counts.get)

                # update the list of names
             names.append(name)
             print(names)

if __name__ == '__main__':
        main()
