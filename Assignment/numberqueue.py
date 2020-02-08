'''
Student:Coco
Assistant:Peter
Scores:98
Time:2020.2.8
Attention:Such a great progress for your coding and remain concern about data structure in the later work!
'''

#得到数字拆分后的list


def temp_list(number,size):
    str_list = list(str(number))
    return str_list


number = str(19991031)
size = len(number)
str_list = temp_list(number, size)

# 实现队列


def queue():
    num_queue = []
    front = -1
    rear = -1
    for i in range(0, size):  # step1：queue
        num_queue.append(str_list[i])
        rear = rear + 1  # step2: push
    print("".join(num_queue))
    '''for i in range(0,size):
        num_queue.append(num_queue.pop(front-i+1))
        front = front + 1
        rear = rear + 1
        print("".join(num_queue))'''
    ############################################
    #----------modify---------------------------
    a time-optimal method but have a great impact on space complexity!
    for i in range(0,size):
        num_queue.append(num_queue[front+1])
        front = front + 1
        rear = rear + 1
        for i in range(front, rear):
            print(num_queue[i], end='')
        print()
    ############################################



queue()
print(queue)




