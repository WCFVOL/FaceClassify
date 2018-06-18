from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from TwoFace.deepid_gen.deepid_generate import deepid_generate
from TwoFace.facetemp import get_face
from TwoFace.retrieval.retrieve import judge_two_face
from TwoFace.vector_img import vector_img


def get_file(upfile):
    f = None
    for chunk in iter(lambda: upfile.read(4096), b""):
        if f is None:
            f = chunk
        else:
            f = f + chunk
    return f


@csrf_exempt
def two_face(request):
    if request.method == 'POST':
        post = request.POST
        token = post.get('token')
        if token != 'qqwrv':
            return JsonResponse({'ok': 0, 'msg': 'token错误'})
        face1 = request.FILES.get('face1')
        face2 = request.FILES.get('face2')
        if face1 is None or face2 is None:
            return JsonResponse({'ok': 0, 'msg': '需要两张图片'})
        face1 = np.asarray(bytearray(face1.read()), dtype="uint8")
        face2 = np.asarray(bytearray(face2.read()), dtype="uint8")

        face_list_1 = get_face(face1)
        face_list_2 = get_face(face2)
        if len(face_list_1) == 0 :
            return JsonResponse({'ok': 2, 'msg': '1图片人脸数目为0'})
        if len(face_list_2) == 0 :
            return JsonResponse({'ok': 3, 'msg': '2图片人脸数目为0'})
        if len(face_list_1) != 1:
            return JsonResponse({'ok': 0, 'msg': '1图片人脸数目不唯一'})
        if len(face_list_2) != 1:
            return JsonResponse({'ok': 0, 'msg': '2图片人脸数目不唯一'})
        face_vector_1 = vector_img(face_list_1[0], (3, 55, 47))
        face_vector_2 = vector_img(face_list_2[0], (3, 55, 47))
        deepid_face_1 = deepid_generate(face_vector_1)
        deepid_face_2 = deepid_generate(face_vector_2)
        result = judge_two_face(deepid_face_1, deepid_face_2)
        return JsonResponse({'ok': 1, 'result': result})
    else:
        return JsonResponse({'ok': 0, 'msg': 'need POST and two image '})


@csrf_exempt
def judge_face(request):
    if request.method == 'POST':
        post = request.POST
        token = post.get('token')
        if token != 'qqwrv':
            return JsonResponse({'ok': 0, 'msg': 'token错误'})
        face = request.FILES.get('face')
        if face is None:
            return JsonResponse({'ok': 0, 'msg': '需要图片'})
        face = np.asarray(bytearray(face.read()), dtype="uint8")
        face_list = get_face(face)
        return JsonResponse({'ok': 1, 'face_num': len(face_list)})
    else:
        return JsonResponse({'ok': 0, 'msg': 'need POST and an image '})
