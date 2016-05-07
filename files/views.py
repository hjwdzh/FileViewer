from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import os

def parse_path_url(path):
	print(path)
	names = path.split('/')
	start = 1
	url = '/'
	path_list = [{'name':'root','url':url}]
	for i in range(0,len(names)):
		if start+i>=len(names):
			break
		path_list.append({'name':names[start+i],'url':url+names[start+i]})
		url = url + names[start+i] + '/'
	return path_list

def index(request):
	template = loader.get_template('files/index.html')
	path = os.getcwd()
	path_list = parse_path_url(path)
	context = {'path_list':path_list}
	return HttpResponse(template.render(context, request))

def parse_files(path):
	suffixes = ['jpg','JPG','png','PNG','bmp','BMP','JPEG','jpeg']
	if (path[len(path)-1]!='/'):
		path=path+'/'
	files = os.listdir(path)
	regular_files = []
	directories = []
	for f in files:
		if os.path.isfile(path+f):
			flag = False
			for suffix in suffixes:
				if f.endswith(suffix):
					flag = True
					break
			if flag:
				regular_files.append(f)
		else:
			directories.append(f)
	regular_files.sort()
	directories.sort()
	return regular_files, directories

def imageview(request,path):
	image_data = open(path, "rb").read()
	if path.endswith('jpg') or path.endswith('JPG'):
		return HttpResponse(image_data, content_type="image/jpeg")
	elif path.endswith('png') or path.endswith('PNG'):
		return HttpResponse(image_data, content_type="image/png")
	elif path.endswith('jpeg') or path.endswith('JPEG'):
		return HttpResponse(image_data, content_type="image/jpeg")
	elif path.endswith('bmp') or path.endswith('BMP'):
		return HttpResponse(image_data, content_type="image/bmp")
	
def fileview(request, path):
	template = loader.get_template('files/index.html')
	path_list = parse_path_url(path)

	loop_num = 5
	regular_files, directories = parse_files(path)
	regular_chunks = []
	top = 0
	for i in range(len(regular_files)):
		if (top == 0):
			regular_chunks.append([])
		regular_chunks[len(regular_chunks)-1].append(regular_files[i])
		top += 1
		if (top == loop_num):
			top = 0
	if (len(regular_chunks) == 0):
		remain_num = 0
	else:
		remain_num = loop_num - len(regular_chunks[len(regular_chunks)-1])
	context = {'path_list':path_list, 'regular_files':regular_chunks, 'directories':directories, 'current_path': path, 'remain_num': remain_num}
	return HttpResponse(template.render(context, request))


