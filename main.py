import os
import fnmatch
import sys
import shutil
import time

pasta_original = r'C:\Users\Julia\Desktop\Conversor Video Python\Pasta_Original'
pasta_saida = r'C:\Users\Julia\Desktop\Conversor Video Python\Nova pasta'


def menu():
    print('\nOlá. O que você gostaria de realizar?\n')
    print('\t1 - Mover todos os arquivos para outra pasta. ')
    print('\t2 - Copiar todos os arquivos para outra pasta. ')
    print('\t3 - Deletar todos os arquivos de uma pasta.')
    print('\t4 - Listar todos os arquivos de uma pasta.')
    print('\t5 - Encontrar arquivo(s) em uma pasta:')
    print('\t6 - Converter todos os arquivos de vídeo para outro formato / melhor qualidade.')
    print('\t7 - Sair\n')



def menu2():
    print('\n\nOperação realizada com sucesso. Digite 1 para retornar ao menu ou 2 para finalizar: ')

    flag = True
    while flag:
        op = input('Opção: ')
        if op == '1':
            inicio()
            flag = False

        elif op == '2':
            print('\n\n*** PROGRAMA ENCERRADO ***')
            exit()
            flag = False

        else:
            print('Opção inválida. Tente novamente...')


def crono():
    num_of_secs = 3
    while num_of_secs:
        print('.')
        time.sleep(1)
        num_of_secs -= 1
    print()


def mover():
    crono()
    caminho_original = input('\nDigite o local da sua pasta: ')
    caminho_saida = input('\nDigite o novo local para onde seus arquivos serão movidos: ')
    try:
        os.mkdir(caminho_saida)
    except FileExistsError as e:  # se a pasta com mesmo nome já existir
        print(f'Pasta {caminho_saida} já existe.')

    for root, dirs, files in os.walk(caminho_original):  # raiz, diretorio, arquivos
        for file in files:
            old_file_path = os.path.join(root, file)  # pegando o caminho antigo (caminho_original)
            new_file_path = os.path.join(caminho_saida, file)  # pegando o caminho novo (caminho_novo)

            shutil.move(old_file_path, new_file_path)

            print(f"Arquivo '{file}' copiado com sucesso para '{caminho_saida}'")

    menu2()


def copiar():
    crono()
    caminho_original = input('\nDigite o local da sua pasta: ')
    caminho_saida = input('\nDigite o novo local para onde seus arquivos serão movidos: ')
    try:
        os.mkdir(caminho_saida)
        print()
    except FileExistsError as e:
        print(f'Pasta {caminho_saida} já existe.\n')

    for root, dirs, files in os.walk(caminho_original):  # raiz, diretorio, arquivos
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_saida, file)

            shutil.copy(old_file_path, new_file_path)

            print(f"Arquivo '{file}' copiado com sucesso para '{caminho_saida}\n'")

    menu2()


def deletar():
    crono()
    caminho_original = input('\nDigite o local da sua pasta: ')

    for root, dirs, files in os.walk(caminho_original):  # raiz, diretorio, arquivos3
        for file in files:
            file_path = os.path.join(caminho_original, file)

            os.remove(file_path)

            print(f"Arquivo '{file}' foi deletado com sucesso.\n")

    menu2()


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2  # base elevado a 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:  # se o tamanho é menor que kilo é Byte, se é menor que mega é Kbyte, menor que giga é Megabyte
        texto = 'B'
    elif tamanho < mega:
        tamanho = tamanho / kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho = tamanho / mega
        texto = 'M'
    elif tamanho < tera:
        tamanho = tamanho / giga
        texto = 'G'
    elif tamanho < peta:
        tamanho = tamanho / tera
        texto = 'T'
    else:
        tamanho = tamanho / peta
        texto = 'P'

    tamanho = round(tamanho, 2)  # fazendo ter duas casas decimais
    return f'{tamanho}{texto}'.replace('.', ',')


def listar():
    crono()
    cont = 0
    caminho_original = input('\nDigite o local da sua pasta: ')
    print()

    print('\n******** LISTA DOS ARQUIVOS *********\n')

    for root, dirs, files in os.walk(caminho_original):  # raiz, diretorio, arquivos
        for file in files:
            cont += 1
            print(file)


    print(f"\n\nForam listados {cont} arquivos da pasta '{caminho_original}'.\n")

    op = input(
        '\nDeseja ver os arquivos com informações completas? Digite 1 para Sim ou qualquer tecla para continuar: ')
    print()
    crono()

    print('\n******** LISTA DOS ARQUIVOS *********\n')

    cont = 0
    if op == '1':
        for raiz, diretorios, arquivos in os.walk(caminho_original):
            for arquivo in arquivos:
                try:
                    cont += 1
                    caminho_original = os.path.join(raiz, arquivo)
                    nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                    tamanho_arquivo = os.path.getsize(caminho_original)

                    print()
                    print('Nome do arquivo:', arquivo)
                    print('Caminho:', caminho_original)
                    print('Nome:', nome_arquivo)
                    print('Extensão:', ext_arquivo)
                    print('Tamanho:', tamanho_arquivo)
                    print('Tamanho formatado:', formata_tamanho(tamanho_arquivo))

                except PermissionError as e:
                    print(f'Sem permissões para acessar o arquivo. Error -> {e}')
                except FileNotFoundError as e:
                    print(f'Arquivo não foi encontrado. Error -> {e}')
                except Exception as e:
                    print(f'Erro desconhecido. Error -> {e}')

    print(f"\n\nForam listados {cont} arquivos da pasta '{caminho_original}' com informaçoes completas.\n")

    menu2()


def encontrar():
    crono()
    caminho_procura = input('\nDigite o local da sua pasta: ')
    termo_a_procurar = input('Digite um termo a procurar: ')
    contador = 0

    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            if termo_a_procurar in arquivo:
                try:
                    contador += 1
                    caminho_completo = os.path.join(raiz, arquivo)
                    nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                    tamanho_arquivo = os.path.getsize(caminho_completo)

                    print()
                    print('Encontrei o arquivo:', arquivo)
                    print('Caminho:', caminho_completo)
                    print('Nome:', nome_arquivo)
                    print('Extensão:', ext_arquivo)
                    print('Tamanho:', tamanho_arquivo)
                    print('Tamanho formatado:', formata_tamanho(tamanho_arquivo))

                except PermissionError as e:
                    print(f'Sem permissões para acessar o arquivo. Error -> {e}')
                except FileNotFoundError as e:
                    print(f'Arquivo não foi encontrado. Error -> {e}')
                except Exception as e:
                    print(f'Erro desconhecido. Error -> {e}')

    print(f'\n{contador} arquivo(s) encontrado(s) com a palavra chave {termo_a_procurar}')
    input('\nDigite qualquer tecla para continuar...')
    menu2()


def converter():
    contador = 0
    if sys.platform == 'linux':
        comando_ffmpeg = 'ffmpeg'
    else:
        comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

    codec_video = '-c:v libx264'
    crf = '-crf 23'  # entre 15 e 28 ta com boa qualidade. 18 é melhor. 28 a pior
    preset = '-preset ultrafast'
    codec_audio = '-c:a aac'
    bitrate_audio = '-b:a 320k'
    debug = '-ss 00:00:00 -to 00:00:10'

    caminho_original = input('\nDigite o local da sua pasta: ')
    caminho_saida = input('\nDigite o novo local para onde seus arquivos serão movidos: ')

    for raiz, pastas, arquivos in os.walk(caminho_original):
        for arquivo in arquivos:
            if not fnmatch.fnmatch(arquivo, '*.mp4'):
                continue

            caminho_completo = os.path.join(raiz, arquivo)
            nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
            caminho_legenda = nome_arquivo + '.srt'
            contador += 1

            print(nome_arquivo)

            if os.path.isfile(caminho_legenda):
                print('Legenda existe.')
                input_legenda = f'-i "{caminho_legenda}"'
                map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
            else:
                print('Sem legenda!')
                input_legenda = ''
                map_legenda = ''

            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

            arquivo_saida = f'{caminho_saida}/{nome_arquivo}_NOVO{extensao_arquivo}'

            comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                      f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                      f'{map_legenda} "{arquivo_saida}"'

            print(comando)

            os.system(comando)  # comando de execução

        print(f'\n{contador} arquivos foram convertidos.')
        input('\nDigite qualquer tecla para continuar...')
        menu2()


def inicio():
    flag = True
    while flag:
        print('\n\n\t*****  CONVERTOR DE VÍDEO (v1.0) *****\n')
        menu()
        op = input('Digite sua opção: ')

        if op == '1':
            mover()

        elif op == '2':
            copiar()

        elif op == '3':
            deletar()

        elif op == '4':
            listar()

        elif op == '5':
            encontrar()

        elif op == '6':
            converter()

        elif op == '7':
            print('\n\n*** PROGRAMA ENCERRADO ***')
            exit()
            flag = False

        else:
            print('\nOpção inválida. Tente novamente...')
            input('\nDigite qualquer tecla para continuar...')


inicio()
