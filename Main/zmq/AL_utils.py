import binascii
from scapy.all import *
import string


def list_to_string(vector):
    temp = [str(x) for x in vector]
    return ''.join(temp)


def bit_flip(vector,i):
    temp = vector[:]
    if temp[i] == 0:
        temp[i] = 1
    elif temp[i] == 1:
        temp[i] = 0
    else:
        print 'not a bit string'
    return temp


def bin_to_hex(bin_string):
    bin_list = list(bin_string)
    hex_list = []
    for i in range(len(bin_list)/4):
        if bin_list[4*i:4*(i+1)] == ['0','0','0','0']:
            hex_list.append('0')
        if bin_list[4*i:4*(i+1)] == ['0','0','0','1']:
            hex_list.append('1')
        if bin_list[4*i:4*(i+1)] == ['0','0','1','0']:
            hex_list.append('2')
        if bin_list[4*i:4*(i+1)] == ['0','0','1','1']:
            hex_list.append('3')
        if bin_list[4*i:4*(i+1)] == ['0','1','0','0']:
            hex_list.append('4')
        if bin_list[4*i:4*(i+1)] == ['0','1','0','1']:
            hex_list.append('5')
        if bin_list[4*i:4*(i+1)] == ['0','1','1','0']:
            hex_list.append('6')
        if bin_list[4*i:4*(i+1)] == ['0','1','1','1']:
            hex_list.append('7')
        if bin_list[4*i:4*(i+1)] == ['1','0','0','0']:
            hex_list.append('8')
        if bin_list[4*i:4*(i+1)] == ['1','0','0','1']:
            hex_list.append('9')
        if bin_list[4*i:4*(i+1)] == ['1','0','1','0']:
            hex_list.append('a')
        if bin_list[4*i:4*(i+1)] == ['1','0','1','1']:
            hex_list.append('b')
        if bin_list[4*i:4*(i+1)] == ['1','1','0','0']:
            hex_list.append('c')
        if bin_list[4*i:4*(i+1)] == ['1','1','0','1']:
            hex_list.append('d')
        if bin_list[4*i:4*(i+1)] == ['1','1','1','0']:
            hex_list.append('e')
        if bin_list[4*i:4*(i+1)] == ['1','1','1','1']:
            hex_list.append('f')
    hex_str = ''.join(hex_list)
    return hex_str


def reconstruct_packet(pkt,vector,stage_number,packet_index):
    '''
    :param vector: whole payload of four stages
    :param stage_number: stage1:1;stage2:2;stage3:3;stage4:4
    :param packet_index: 12_50:1;12_40:2;12_28:3;10_40:4
    :return:
    '''
    len_12_50 = 256
    len_12_40 = 176
    len_12_28 = 80
    len_10_40 = 176
    stage_length = 688
    whole = binascii.hexlify(bytes(pkt))
    payload = binascii.hexlify(bytes(pkt[Raw]))
    temp = string.replace(whole,payload,"")
    stage_vector = vector[(stage_number-1)*stage_length:stage_number*stage_length]
    if packet_index == 1:
        packet_vector = stage_vector[:len_12_50]
    if packet_index == 2:
        packet_vector = stage_vector[len_12_50:len_12_50+len_12_40]
    if packet_index == 3:
        packet_vector = stage_vector[len_12_50+len_12_40:len_12_50+len_12_40+len_12_28]
    if packet_index == 4:
        packet_vector = stage_vector[len_12_50+len_12_40+len_12_28:len_12_50+len_12_40+len_12_28+len_10_40]
    packet_vector = map(int,packet_vector)
    pktnew = list_to_string(packet_vector)
    pktnew = pktnew
    a = time.time()
    pktnew = bin_to_hex(pktnew)
    return temp+pktnew
