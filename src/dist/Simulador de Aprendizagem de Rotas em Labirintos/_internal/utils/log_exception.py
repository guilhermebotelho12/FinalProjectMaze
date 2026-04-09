import os
import traceback

def log_exception(exception):
    try:
        # Determinar o caminho para a pasta raiz do projeto
        project_root = os.path.dirname(os.path.abspath(__file__))
        log_file = os.path.join(project_root, "error_log.txt")
        
        # Obter a mensagem da exceção e o traceback
        exception_message = ''.join(traceback.format_exception(None, exception, exception.__traceback__))
        
        # Escrever a exceção no arquivo de log
        with open(log_file, 'a') as file:
            file.write(exception_message)
                
    except Exception as log_error:
        print(f"Falha ao registrar o erro: {log_error}")