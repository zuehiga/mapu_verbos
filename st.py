import streamlit as st #LIBRERIA DE STREAMLIT
import pandas as pd    #LIBRERIA DE PANDAS PARA MANEJO DE EXCEL
from PIL import Image  
import base64          #LIBRERIA PARA TRABAJAR CON LOS FONDOS

#Hola MUNDO: Iremos paso por paso en la creación de esta app:

####1 ER PASO: Debemos extraer las tablas de datos de nuestra hoja EXCEL 'mapudungun.xlsx'
#TABLA PARA CONSONANTE:
datos_kon=pd.read_excel('mapudungun.xlsx',sheet_name='kon')
#TABLA PARA TERMINACIÓN EN 'AEOU':
datos_tripa=pd.read_excel('mapudungun.xlsx',sheet_name='tripa')
#TABLA PARA TERMINACIÓN EN 'I':
datos_pi=pd.read_excel('mapudungun.xlsx',sheet_name='pi')
####2 DO PASO: Ahora debemos crear diccionarios para poder acceder a cada una de las combinaciones, en este caso tomaremos la columna
####'persona' como índice
#CREANDO DICCIONARIO PARA TERMINACIÓN EN CONSONANTE:
D_kon=datos_kon.set_index('persona').to_dict(orient='index')
#CREANDO DICCIONARIO PARA TERMINACIÓN EN 'AEOU':
D_tripa=datos_tripa.set_index('persona').to_dict(orient='index')
#CREANDO DICCIONARIO PARA TERMINACIÓN EN 'I':
D_pi=datos_pi.set_index('persona').to_dict(orient='index')
#3 ER PASO: 
#st.title("¡Bienvenidos al conjugador de verbos en Mapudungun! :smile:")
import streamlit as st

st.markdown('<h1 style="color: black;">Conjugador de verbos en Mapudungun</h1>', unsafe_allow_html=True)


## informacion adicional sobre la lengua mapudungun

#st.write('La lengua mapudungun es una lengua aislante y aglutinante.'
#'Esto significa que los sufijos indican diferentes aspectos gramaticales.'
#'Esta lengua tiene tres personas gramaticales: primera, segunda y tercera, en singural, dual y plural.'
#'Por ejemplo, se tiene la raiz am- que significa hablar y amün; yo hablo.'

#'Aquí encontrarás formas para conjugar los verbos en modo indicativo. ')

import streamlit as st

import streamlit as st

texto = """
El mapudungun es una lengua hablada por el pueblo mapuche. Es una lengua rica y fascinante que refleja su grandiosa cultura y cosmovisión.

En el mapudungun, los verbos se conjugan en diferentes formas. Veamos algunos ejemplos de conjugación en modo indicativo del verbo "am" que significa "hablar":

- Singular:
  - Amu: Yo hablo
  - Amulei: Tú hablas
  - Amuwe: Él/Ella habla

- Dual:
  - Amutu: Nosotros dos hablamos
  - Amuleiñ: Ustedes dos hablan
  - Amutulei: Ellos/Ellas dos hablan

- Plural:
  - Amulen: Nosotros hablamos
  - Amuleiñ: Ustedes hablan
  - Amulen: Ellos/Ellas hablan

Estos ejemplos ilustran cómo los verbos en mapudungun se conjugan de acuerdo a las personas gramaticales (primera, segunda y tercera) y al número (singular, dual y plural). La conjugación de los verbos en mapudungun es una característica importante de esta hermosa lengua.

Explora más sobre la lengua mapudungun y disfruta de su riqueza cultural y lingüística.

¡Bienvenidos al mundo del mapudungun! :smile:
"""

st.markdown(f'<p style="color: black;">{texto}</p>', unsafe_allow_html=True)

import streamlit as st

def mostrar_verbos():
    verbos = {
        "am-": "hablar",
        "pewk-": "cantar",
        "melih-": "correr",
        "w-": "ver",
        "ley-": "dormir",
        "kutx-": "comer",
        "ray-": "andar",
        "pay-": "ir",
        "metx-": "escuchar",
        "ruk-": "entrar",
        "lawen-": "amar",
        "ralün-": "caminar",
        "eymi-": "sentir",
        "kaxo-": "caer",
        "fe-": "hacer",
        "welu-": "existir",
        "lafken-": "nadar",
        "kisu-": "saber",
        "anum-": "construir",
        "trawün-": "pensar"
    }

    st.write("**Aquí te dejo algunos verbos en Mapudungun y su traducción al español :**")

    for verbo, traduccion in verbos.items():
        st.write(f"- {verbo}: {traduccion}")

mostrar_verbos()


#i=Image.open('DICT.png')
#st.image(i)

#####4 TO PASO: Estableciendo FONDO DE LA APP:
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('fondo.jpg')    

####5 TO PASO: LÓGICA DEL PROGRAMA
palabra=st.text_input("Ingresar verbo a conjugar")
numero=st.selectbox("Seleccionar un número gramatical", ["singular","dual","plural"])
persona=st.selectbox("Seleccionar una persona gramatical",[1,2,3])

if palabra== '': 
    palabra='hola'
else:
    palabra=palabra
ultima_letra=palabra[-1]
if ultima_letra not in 'aeiou':
    palabra_transformada=palabra+' '+D_kon[persona][numero]
elif ultima_letra in "aeou":
    palabra_transformada=palabra+' '+D_tripa[persona][numero]
elif ultima_letra == 'i':
    palabra_transformada=palabra+' '+D_pi[persona][numero]

if st.button('Conjugar'):
    st.write('El verbo se conjuga de esta manera:')
    st.write(palabra_transformada)
    
    
    
    
import streamlit as st

def mostrar_mensaje_final():
    mensaje = """
        <div style="text-align: center; font-size: 18px; color: #333333;">
            <p>Gracias por visitarnos. Seguiremos trabajando para contribuir con el aprendizaje y la difusión de más lenguas valiosas.</p>
        </div>
    """
    st.markdown(mensaje, unsafe_allow_html=True)



# Al final de tu aplicación, después de mostrar los resultados
mostrar_mensaje_final()

