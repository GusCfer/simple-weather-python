import requests
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkImage
from PIL import Image, ImageTk
import io

#definindo a função que comunica com a api e retorna as informações
def clima(namecity):
    #toda configuração para trazer e armazenar os dados da requisição em variaveis
    global dados,icon,localizacao,temperatuura,condicoes,city_name
    city_name = namecity
    api_key = 'PREENCHA COM A API AQUI'
    link = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    requisicao = requests.get(link)
    data = requisicao.json()
    dados = data['current']
    localizacao = data['location']
    temperatura = dados['temp_c']
    temperaturaf = dados['temp_f']
    condicoes = dados['condition']
    icon = condicoes['icon']
    situacao = condicoes['text']
    uconsulta = dados['last_updated']
    pais = localizacao['country']

   #WIDGETS DO CLIMA
    #chamando a requisição para buscar imagem do clima e inserindo na tela
    image = ("https:" + icon)
    requisicaoimagem = requests.get(image)
    image_data = requisicaoimagem.content
    image_pillow = Image.open(io.BytesIO(image_data))  
    image_ctk = ctk.CTkImage(light_image=image_pillow, size=(image_pillow.width, image_pillow.height))
    #chamando widgets da imagem 
    imagelabel = ctk.CTkLabel(master=root,image=image_ctk,text='')
    imagelabel.place(relx=0.33,rely=0.33)
    #chamando os dados do clima e colocando na tela
    temp = ctk.CTkLabel(root,text='Temperatura c°',font=('Arial',10),text_color='#418c9a')
    temp.place(relx=0.1,rely=0.5)
    tempcity = ctk.CTkLabel(root,text=temperatura,font=('Arial',10))
    tempcity.place(relx=0.1,rely=0.56)
    #EM F
    temp2 = ctk.CTkLabel(root,text='Temperatura f°',font=('Arial',10),text_color='#418c9a')
    temp2.place(relx=0.55,rely=0.5)
    tempcity2 = ctk.CTkLabel(root,text=temperaturaf,font=('Arial',10))
    tempcity2.place(relx=0.55,rely=0.56)
    #status
    temp = ctk.CTkLabel(root,text='Status',font=('Arial',10),text_color='#418c9a')
    temp.place(relx=0.1,rely=0.62)
    tempcity = ctk.CTkLabel(root,text=situacao,font=('Arial',10))
    tempcity.place(relx=0.1,rely=0.68)
    #country
    temp = ctk.CTkLabel(root,text='Pais',font=('Arial',10),text_color='#418c9a')
    temp.place(relx=0.55,rely=0.62)
    tempcity = ctk.CTkLabel(root,text=pais,font=('Arial',10))
    tempcity.place(relx=0.55,rely=0.68)
    #ultimaconsulta
    temp = ctk.CTkLabel(root,text='Ultima consulta',font=('Arial',10),text_color='#418c9a')
    temp.place(relx=0.1,rely=0.74)
    tempcity = ctk.CTkLabel(root,text=uconsulta,font=('Arial',10))
    tempcity.place(relx=0.1,rely=0.81)
    
#configuração padrão da janela
root= ctk.CTk()
root.geometry('200x300')
root.resizable(False,False)
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

#widgets padrão
label1 = ctk.CTkLabel(root,text='Digite a Cidade:',font=('Arial',15))
label1.place(relx=0.23,rely=0.02)
#campo para entrada de texto
selectioncity = ctk.CTkEntry(root,width=160,height=10)
selectioncity.place(relx=0.1,rely=0.13)
selectioncity.insert(ctk.END,'')

#botão para chamar as informações
button = ctk.CTkButton(root,width=100,height=30,text='Pesquisar',fg_color='#418c9a',command=lambda: clima(selectioncity.get()))
button.place(relx=0.25,rely=0.23)

root.mainloop()