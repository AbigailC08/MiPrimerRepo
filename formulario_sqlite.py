import tkinter as tk
from tkinter import messagebox 
import sqlite3

#creacion de base de datos
def crear_db():
    conexion=sqlite3.connect('personas.db')
    cursor=conexion.cursor()
    cursor.execute('''
    CREATE TABIE IF NOT EXISTS personas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NO NULL,
                   edad INTEGER NO NULL)''')