#이미지 넣어놓은 파일 불러오기
path = '/content/drive/MyDrive/객체탐지/add/'
file_list = os.listdir(path)
image_file_list_py2 = [file for file in file_list if file.endswith('.jpg')] 
image_file_list_py2.sort()
image_file_list_py2

#원본 이미지 파일에서 이미지를 불러다가 명도 조절해서 다른 파일
for i in range(len(image_file_list_py)):
  path = "/content/drive/MyDrive/객체탐지/add/"

  src = cv2.imread( path + image_file_list_py[i], cv2.IMREAD_GRAYSCALE)

  sub_dst = cv2.subtract(src, 50)
  sub_dst = cv2.resize(sub_dst, dsize=(500, 650), interpolation=cv2.INTER_CUBIC)

  cv2.imwrite("/content/drive/MyDrive/객체탐지/add2/" + image_file_list_py[i],sub_dst)
