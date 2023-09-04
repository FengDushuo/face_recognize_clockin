# -*- coding: utf-8 -*-
import face_recognition
import cv2
import datetime
import glob2 as gb
import os


def Mfacerecognition(db_path,predict_path):
    path=gb.glob(predict_path)
    dirs=os.listdir(path[0])
    qiandao=cv2.imread(path[0]+r"\\"+dirs[-1])#读入签到图片
    img_path = gb.glob(db_path+'\\*.jpg')
    known_face_names = []
    known_face_encodings = []

    for i in img_path:
        picture_name = i.replace(db_path+'\\*.jpg', '')
        picture_newname = picture_name.replace('.jpg', '')
        picture_newname = picture_newname.replace(db_path+'\\', '')
        someone_img = face_recognition.load_image_file(i)
        someone_face = face_recognition.face_encodings(someone_img)
        if len(someone_face)>0:
            someone_face_encoding = someone_face[0]
            known_face_names.append(picture_newname)
            known_face_encodings.append(someone_face_encoding)
            someone_img = []
            someone_face_encoding = []
        else:
            someone_img = []
            someone_face_encoding = []      

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    small_frame = cv2.resize(qiandao, (0, 0), fx=1, fy=1)
    rgb_small_frame = small_frame[:, :, ::-1]
    echo=len(face_recognition.face_locations(rgb_small_frame))

    #for i in range(echo):

        #small_frame = cv2.resize(qiandao, (0, 0), fx=1, fy=1)
        #rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        attendid_list=[]
        for i in face_encodings:
            match = face_recognition.compare_faces(known_face_encodings, i, tolerance=0.10)
            print(match)
            if True in match:
                match_index = match.index(True)
                name = "match"
                # To print name and time
                cute_clock = datetime.datetime.now()
                print(known_face_names[match_index] + ',' + str(cute_clock))
                attendid_list.append(known_face_names[match_index])
            else:
                name = "unknown"
            face_names.append(name)

    process_this_frame = not process_this_frame
    

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(qiandao, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(qiandao, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(qiandao, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('qiandao', qiandao)

    cv2.destroyAllWindows() 

    return attendid_list

