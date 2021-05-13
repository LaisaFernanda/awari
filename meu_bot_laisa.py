#importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp

#inicializar o whatsapp
wp = WhatsApp()

#esperar que enter seja pressionado
input("Pressione enter apos escanear o QR code  ")


#lista de nomes a serem pesquisados
#importante: o nome deve ser não ambiguo(por isso é melhor número), pois o bot vai pesquisar o primeiro nome 
nomes_palavras_chaves = ['Pedro_bot','Bot_w','Ana_bot','PrincesaRainha']

lista_produtos = ['manga','pera','uva','uva']

#lista dos nomes que vou referir a mensagem
primeiros_nomes = [n.split('_')[0] for n in nomes_palavras_chaves] 


#loop para mandar mensagem para os clientes
for primeiro_nome, nome_pesquisar, produtos in zip(primeiros_nomes, nomes_palavras_chaves,lista_produtos):

#pesquisar pelo contato e esperar um pouco 
    wp.search_contact(nome_pesquisar)
    sleep(2)
    
#mensagem que será enviada    
    mensagem = f"Olá {primeiro_nome}!, obrigada pela compra {produtos}!"
   
    
#enviar mensagem 
    wp.send_message(mensagem)

# esperar 10 segundos e fechar
sleep(10)
wp.driver.close()


