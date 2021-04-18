import os, time 



dir_list = os.listdir("files_to_sequence")

sequence_dir = os.path.join(os.getcwd(), 'files_to_sequence')

# f = open('my_file.txt', 'w')
# b = '1'
# f.write(b)
# f.close()


def check_last_modified(file):

    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(os.path.join(sequence_dir, file)) 

    print("last modified: %s" % ctime)

for x in range(len(dir_list)):
    check_last_modified(dir_list[x])

def inc_memfile():
    f = open("my_file.txt", "r")
    data = int(f.read())
    data_plus = data + 1
    f.close()

    f = open('my_file.txt', 'w')
    f.write(str(data_plus))
    
    # print(data)

# for _ in range(1000):
#     inc_memfile()

