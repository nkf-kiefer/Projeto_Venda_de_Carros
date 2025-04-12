#import openai_api

#def get_car_ai_bio(model,brand,year):
    #prompt = ''''
    #Me mostre uma descrição de venda para o carro {}{}{} em apenas 250 caracteres. Fale coisas especificas desse modelo
    #'''
    #openai_api.key = ''
    #vai substituir o prompt com esses parametros
    #prompt = prompt.format(brand, model, year)
    #manda um prompt e salva nessa variavel response
    #response = openai_api.Completion.create(
       # model = 'text-davinci-003'
        #prompt=prompt,
        #max_tokens=1000,
    #)
    #formato padrão da api
    #return response['choices'][0]["text"]