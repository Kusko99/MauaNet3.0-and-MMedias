# -*- coding: utf-8 -*-
"""Mmedias.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BP8AwfRUupIZJkmJZ5AamWTx4hPDUUSP
"""

def arrumar_peso():
  peso_prova = int(input("digite o peso de prova: "))
  if peso_prova > 1:
    peso_prova = peso_prova/10
  peso_trab = peso_prova-1

p1 = int(input("digite a nota da p1: "))
t1 = int(input("digite a nota da t1: "))
arrumar_peso()
media = (((p1)/2)*peso_prova + ((t1+10)/2)*peso_trab)
if (media<6):
  p2 = (((6-((t1+10)/2)*peso_trab)/peso_prova)*2)-p1
  if (p2>10):
    print("Po cara vai se sub mesmo")
  p_sub = (((6-((t1+10)/2)*peso_trab)/peso_prova)*2)-p1
  if (p1<p_sub):
    p_sub = (((6-((t1+10)/2)*peso_trab)/peso_prova)*2)/2
  print(f"Considerando a nota do T2 = 10 a Nota da P2 = {p2}")
  print(f"Considerando que a nota da P2 nao foi a esperada vc precisa tirar {p_sub} na p_sub")
elif(media>=6):
   t2 = (((6-(p1/2)*peso_prova)/peso_trab)*2)-t1
   print(f"Podendo zerar a P2, tire {t2} na T2")