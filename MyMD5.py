# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:44:44 2018

@author: utilisateur
"""
from math import floor,sin
import binascii

def dec2bin(d, nb=0):
    if(d == 0):
        b = "0"
    else:
        b = ""
        while(d != 0):
            b = "01"[d&1] + b
            d = d >> 1
    return b.zfill(nb)
    """dec2bin(d, nb=0): conversion nombre entier positif ou nul
    -> chaîne binaire (si nb>0, complète à gauche par des zéros)"""


def leftCircularShift(k,bits):
    bits = bits%32
    k = k%(2**32)
    upper = (k<<bits)%(2**32)
    result = upper | (k>>(32-(bits)))
    return(result)
    """decalage a gauche de bits"""
    
def blockDivide(block, chunks):
    result = []
    size = len(block)//chunks
    for i in range(0, chunks):
        result.append( int.from_bytes( block[i*size:(i+1)*size],byteorder="little" ))
    return(result)
    """renvoie une liste decoupe en un nombre de bits donne, en little-endian"""

def bitlen(bitstring):
    return(len(bitstring)*8)
    """longueur en bit d'une string"""

def fmt8(num):
    bighex = "{0:08x}".format(num)
    binver = binascii.unhexlify(bighex)
    result = "{0:08x}".format(int.from_bytes(binver,byteorder='little'))
    return(result)
    """formatage byte -> hexa"""
    
def md5(message):
    r=[7, 12, 17, 22, 7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
       5,  9, 14, 20, 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
       4, 11, 16, 23, 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
       6, 10, 15, 21, 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
    
    k=[]
    for i in range(64): k.append(int(floor(abs(sin(i + 1)) * 2**32)))
    
    #initialisation des variables    
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
   
    msgLen = bitlen(message) % (2**64)  
    """taille du message"""
    
    mes = message.encode() + b'\x80'
    """ajout du bit a 1 a la fin du message"""

    zeroPad = (448 - (msgLen + 8) % 512) % 512
    zeroPad //= 8
    mes = mes + b'\x00' * zeroPad
    """ ajout de bit a 0 jusqu'a ce que la longueur soit = 448(mod512)"""
    
        
    mes = mes + msgLen.to_bytes(8,byteorder='little')
    """ ajout de la taille du message codée en 64 bit little-endian"""
    
    blocs = [mes[i*64:(i+1)*64] for i in range(0, (bitlen(mes)//512))]
    """decoupage en bloc de 512 bits"""
    
    for bloc in blocs:
        w = blockDivide(bloc,16)
        """decoupage en 16 mots de 32 bits"""
        a = h0
        b = h1
        c = h2
        d = h3
        """Boucle principale :"""
        for i in range(64):
            if(i < 16 ):
                
                  f = (b & c) | ((~ b) & d)
                  g = i
                  
            elif(i < 32):
                
                  f = (d & b) | ((~ d) & c)
                  g = (5*i + 1) % 16
                  
            elif(i < 48 ):
                
                  f = b ^ c ^ d
                  g = (3*i + 5) % 16
                  
            elif(i < 64):
                
                f = c ^ (b | (~ d))
                g = (7*i) % 16
                
            temp = d
            d = c
            c = b
            b =leftCircularShift((a + f + k[i] + w[g]), r[i]) + b
            a = temp
            
        h0 = (h0 + a) % (2**32)
        h1 = (h1 + b) % (2**32)
        h2 = (h2 + c) % (2**32)
        h3 = (h3 + d) % (2**32)
        
    empreinte = fmt8(h0) + fmt8(h1) + fmt8(h2) + fmt8(h3)
    """concatenation apres formatage des 4 variables 32 bits"""

    return empreinte       
        
    
